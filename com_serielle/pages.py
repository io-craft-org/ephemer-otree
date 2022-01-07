from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


#################################################
#################################################
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.subsession.round_number == 1

    # def get_players_for_group(self, waiting_players):
    #     if len(waiting_players) >= Constants.players_per_group:
    #         # Create the new group
    #         new_group = []
    #         for index, player in enumerate(waiting_players):
    #             new_group.append(player)
    #             player.rank_in_chain = index + 1
    #         return new_group

    def after_all_players_arrive(self):
        self.group.set_initial_message()
        self.group.propagate_data()


#################################################
#################################################
class ConsignePage(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


#################################################
#################################################
class MessagingPage(Page):
    form_model = 'group'
    form_fields = ['message']

    def is_displayed(self):
        return self.subsession.round_number == self.player.rank_in_chain

    def vars_for_template(self):
        # For the message
        passed_message = ""
        if self.subsession.round_number == 1:
            passed_message = self.group.initial_message
        else:
            passed_message = self.group.in_round(self.subsession.round_number - 1).message
        # For the timer not to be re-initialised at refresh
        current_timeout = 0
        if self.player.field_maybe_none("expiration_time") is None:
            if self.player.rank_in_chain == 1:
                self.player.expiration_time = time.time() + Constants.c_firsttime_showing_message_in_seconds
                current_timeout = Constants.c_firsttime_showing_message_in_seconds
            else:
                self.player.expiration_time = time.time() + Constants.c_subsequenttime_showing_message_in_seconds
                current_timeout = Constants.c_subsequenttime_showing_message_in_seconds
        else:
            current_timeout = self.player.expiration_time - time.time()

        return {
            "passed_message": passed_message,
            "current_timeout": round(current_timeout),
        }

    def before_next_page(self):
        if self.timeout_happened:
            if self.subsession.round_number == 1:
                self.group.message = self.group.initial_message
            else:
                self.group.message = self.group.in_round(self.subsession.round_number - 1).message


class SynchroWaitPage(WaitPage):
    template_name = "com_serielle/SynchroWaitPage.html"


#################################################
#################################################
class IdentificationPage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


class MerciPage(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


page_sequence = [
    GroupingWaitPage,
    ConsignePage,
    MessagingPage,
    SynchroWaitPage,
    IdentificationPage,
    MerciPage,
]
