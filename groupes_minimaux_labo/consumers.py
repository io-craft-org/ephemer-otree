from channels import Group as channelsGroup
from channels.sessions import channel_session
import random
from .models import Group as OtreeGroup, Subsession as OtreeSubsession, Constants
import json
import channels
import logging

from otree import constants_internal
import django.test
from otree.common_internal import (get_admin_secret_code)

from threading import Event
import time

client = django.test.Client()
ADMIN_SECRET_CODE = get_admin_secret_code()


#############################################
#############################################
# Connected to websocket.connect
def ws_winnerpage_connect(message):
    print("*********CONNECTWINNERPAGE************")
    channelsGroup("WINNERPAGE").add(message.reply_channel)

# Connected to websocket.receive
def ws_winnerpage_message(message):
    print("*********RECEIVEWINNERPAGE************")

# Connected to websocket.disconnect
def ws_winnerpage_disconnect(message):
    print("*********DISCONNECTWINNERPAGE************")
    channelsGroup("WINNERPAGE").discard(message.reply_channel)


#############################################
#############################################
# Connected to websocket.connect
def ws_admin_connect(message):
    print("*********CONNECT************")
    channelsGroup("adminreport").add(message.reply_channel)


# Connected to websocket.receive
def ws_admin_message(message):
    print("*********RECEIVE************")
    # Decrypt the url: No info in the url in this app
    # Decrypt the received message
    jsonmessage = json.loads(message.content['text'])
    subsession_pk = jsonmessage['subsession_pk']
    mysubsession = OtreeSubsession.objects.get(pk=subsession_pk)
    if 'order' in jsonmessage:
        order = jsonmessage['order']
        if order == "push_all_players_on_page":
            page_name = jsonmessage['page_name']
            round_nb = jsonmessage['round_nb']
            for p in mysubsession.get_players():
                if ((str(p.participant._current_page_name) == page_name)
                        & (p.participant._round_number == round_nb)):
                    # This player is one of those who needs to be advanced
                    try:
                        if p.participant._current_form_page_url:
                            resp = client.post(
                                p.participant._current_form_page_url,
                                data={
                                    constants_internal.timeout_happened: True,
                                    constants_internal.admin_secret_code: ADMIN_SECRET_CODE
                                },
                                follow=True
                            )
                        else:
                            resp = client.get(p.participant._start_url(), follow=True)
                    except:
                        logging.exception("Failed to advance participant.")
                        raise

                    assert resp.status_code < 400
                    p.participant.vars['participant_was_pushed'] = 'True'
                    p.participant.save()
                    channels.Group(
                        'auto-advance-{}'.format(p.participant.code)
                    ).send(
                        {'text': json.dumps(
                            {'auto_advanced': True})}
                    )
        elif order == "push_active_players_on_page":
            group_pk = jsonmessage['group_pk']
            mygroup = OtreeGroup.objects.get(pk=group_pk)
            page_name = jsonmessage['page_name']
            round_nb = jsonmessage['round_nb']
            for p in mygroup.get_players():
                if ((str(p.participant._current_page_name) == page_name)
                        & (p.participant._round_number == round_nb)
                        & (p.participant.vars['active_flag'] != 'Inactive')):
                    # This player is one of those who needs to be advanced
                    try:
                        if p.participant._current_form_page_url:
                            resp = client.post(
                                p.participant._current_form_page_url,
                                data={
                                    constants_internal.timeout_happened: True,
                                    constants_internal.admin_secret_code: ADMIN_SECRET_CODE
                                },
                                follow=True
                            )
                        else:
                            resp = client.get(p.participant._start_url(), follow=True)
                    except:
                        logging.exception("Failed to advance participant.")
                        raise

                    assert resp.status_code < 400
                    p.participant.vars['participant_was_pushed'] = 'True'
                    p.participant.save()
                    channels.Group(
                        'auto-advance-{}'.format(p.participant.code)
                    ).send(
                        {'text': json.dumps(
                            {'auto_advanced': True})}
                    )
        elif order == "push_inactive_players_on_page":
            group_pk = jsonmessage['group_pk']
            mygroup = OtreeGroup.objects.get(pk=group_pk)
            page_name = jsonmessage['page_name']
            round_nb = jsonmessage['round_nb']
            for p in mygroup.get_players():
                if ((str(p.participant._current_page_name) == page_name)
                        & (p.participant._round_number == round_nb)
                        & (p.participant.vars['active_flag'] == 'Inactive')):
                    # This player is one of those who needs to be advanced
                    try:
                        if p.participant._current_form_page_url:
                            resp = client.post(
                                p.participant._current_form_page_url,
                                data={
                                    constants_internal.timeout_happened: True,
                                    constants_internal.admin_secret_code: ADMIN_SECRET_CODE
                                },
                                follow=True
                            )
                        else:
                            resp = client.get(p.participant._start_url(), follow=True)
                    except:
                        logging.exception("Failed to advance participant.")
                        raise

                    assert resp.status_code < 400
                    p.participant.vars['participant_was_pushed'] = 'True'
                    p.participant.save()
                    channels.Group(
                        'auto-advance-{}'.format(p.participant.code)
                    ).send(
                        {'text': json.dumps(
                            {'auto_advanced': True})}
                    )
        elif order == "deactivate_all_group_on_page":
            group_pk = jsonmessage['group_pk']
            mygroup = OtreeGroup.objects.get(pk=group_pk)
            page_name = jsonmessage['page_name']
            round_nb = jsonmessage['round_nb']
            for p in mygroup.get_players():
                if ((str(p.participant._current_page_name) == page_name)
                        & (p.participant._round_number == round_nb)):
                    p.participant.vars['active_flag'] = 'Inactive'
                    p.participant.save()
        elif order == "reactivate_all_group_on_page":
            group_pk = jsonmessage['group_pk']
            mygroup = OtreeGroup.objects.get(pk=group_pk)
            page_name = jsonmessage['page_name']
            round_nb = jsonmessage['round_nb']
            for p in mygroup.get_players():
                if ((str(p.participant._current_page_name) == page_name)
                        & (p.participant._round_number == round_nb)):
                    p.participant.vars['active_flag'] = 'Playing_No_Change_Game'
                    p.participant.save()
        elif order == "StartMonitoring":
            # Start it only if it's not currently running:
            date_time = mysubsession.session.vars['last_monitoring_time']
            if date_time != 'not_yet_started':
                pattern = '%d.%m.%Y %H:%M:%S'
                epoch = float(time.mktime(time.strptime(date_time, pattern)))
                if epoch < (float(time.time() - Constants.c_inactive_monitoring_period_in_seconds)):
                    Constants.c_stopping_event_monitoring.clear()
                    my_live_manager_thread = LiveManagementThread(mysubsession.pk,
                                                                  Constants.c_stopping_event_monitoring)
                    my_live_manager_thread.start()
            else:
                Constants.c_stopping_event_monitoring.clear()
                my_live_manager_thread = LiveManagementThread(mysubsession.pk,
                                                              Constants.c_stopping_event_monitoring)
                my_live_manager_thread.start()
        elif order == "StartPushing":
            # Start it only if it's not currently running:
            date_time = mysubsession.session.vars['last_pushing_time']
            if date_time != 'not_yet_started':
                pattern = '%d.%m.%Y %H:%M:%S'
                epoch = float(time.mktime(time.strptime(date_time, pattern)))
                if epoch < (float(time.time() - Constants.c_pushing_period_in_seconds)):
                    Constants.c_stopping_event_pushing.clear()
                    my_live_pusher_thread = LivePusherThread(mysubsession.pk,
                                                             Constants.c_stopping_event_pushing)
                    my_live_pusher_thread.start()
            else:
                Constants.c_stopping_event_pushing.clear()
                my_live_pusher_thread = LivePusherThread(mysubsession.pk, Constants.c_stopping_event_pushing)
                my_live_pusher_thread.start()
        elif order == "StopMonitoring":
            Constants.c_stopping_event_monitoring.set()
        elif order == "StopPushing":
            Constants.c_stopping_event_pushing.set()

    #############################################
    # Give feedback
    channelsGroup("adminreport").send({'text': json.dumps(
        {"order": "refresh"})}
    )


# Connected to websocket.disconnect
def ws_admin_disconnect(message):
    print("*********DISCONNECT************")
    channelsGroup("adminreport").discard(message.reply_channel)
