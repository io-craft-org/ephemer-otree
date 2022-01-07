from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'com_serielle'
    players_per_group = 7
    num_rounds = players_per_group

    c_initial_messages = [
        u"L'incident s'est passé à Lund en Suède. Une femme de 46 ans qui apprenait à conduire à sa fille s'est "
        "retrouvée coincée par un bus lors du passage de deux à une voie.\n"
        "Furieuse, elle s'est mise à poursuivre le bus jusqu'à son prochain arrêt. Elle est alors sortie de sa voiture "
        "et s'est dirigée vers le conducteur. Et là, de colère, après une vive discussion, elle aurait écrasé une "
        "banane sur la figure du conducteur !\n\n"
        "Conséquence, de la banane sur le costume et la cravate ...mais aussi un décollement de la rétine, précise "
        "le site internet suédois d’information.\n"
        "Pour sa défense, la banane, à moitié mangée, aurait glissé de sa main quand elle a fait un geste brusque "
        "mais que ce n'était pas son intention de lui écraser sur le visage. Cependant un témoin qui se trouvait "
        "dans le bus à bien confirmé que le lancer était intentionnel et non accidentel !\n\n"
        "Elle a finalement été condamnée à une amende de 560 euros, plus 620 de dommage et intérêt pour le conducteur "
        "du bus, et 100 euros de frais de justice... soit en tout presque 1300 euros pour une attaque à la banane !\n\n"
        ]
    c_firsttime_showing_message_in_seconds = 2*60
    c_subsequenttime_showing_message_in_seconds = 1*60


class Subsession(BaseSubsession):

    def creating_session(self):
        # Initialise
        if self.round_number == 1:
            for g in self.get_groups():
                for p in g.get_players():
                    p.participant.vars['active_flag'] = 'active'

    def vars_for_admin_report(self):
        # Get the data in RAM
        all_subsession_players = self.get_players()
        all_subsession_groups = self.get_groups()
        # For advancement per player
        all_players_app_page = [(str(p.participant._current_app_name) + str(p.participant._round_number) + str(p.participant._current_page_name))
                                for p in all_subsession_players]
        nb_players_per_page_list =\
            [(PageClass.__name__,
              "Stop" in PageClass.__name__,
              all_players_app_page.count((str(self._meta.app_config.name) + str(self.round_number) + str(PageClass.__name__))))
             for PageClass in pages.page_sequence]
        # For advancement per group
        active_players_pergroup_app_page = [((str(p.participant._current_app_name)
                                              + str(p.participant._round_number)
                                              + str(p.participant._current_page_name)),
                                             p.group.id_in_subsession)
                                            for p in all_subsession_players
                                            if p.participant.vars['active_flag'] != 'inactive']
        inactive_players_pergroup_app_page = [((str(p.participant._current_app_name)
                                                + str(p.participant._round_number)
                                                + str(p.participant._current_page_name)),
                                               p.group.id_in_subsession )
                                              for p in all_subsession_players
                                              if p.participant.vars['active_flag'] == 'inactive']
        all_groups_per_page = [[g.id_in_subsession,
                                g.pk,
                                [(PageClass.__name__,
                                  "Wait" in PageClass.__name__,
                                  active_players_pergroup_app_page.count(
                                      (str(self._meta.app_config.name) + str(self.round_number) + str(PageClass.__name__), g.id_in_subsession)),
                                  inactive_players_pergroup_app_page.count(
                                      (str(self._meta.app_config.name) + str(self.round_number) + str(PageClass.__name__), g.id_in_subsession)))
                                 for PageClass in pages.page_sequence] ]
                               for g in all_subsession_groups]
        return {
            # For advancement in the pages, per player and per group
            'all_pages': [(PageClass.__name__, "Wait" in PageClass.__name__, "Stop" in PageClass.__name__) for PageClass in pages.page_sequence],
            'nb_players_per_page_list': nb_players_per_page_list,
            'all_groups_per_page': all_groups_per_page,
        }

    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) >= Constants.players_per_group:
            # Create the new group
            new_group = []
            for index, player in enumerate(waiting_players):
                new_group.append(player)
                player.rank_in_chain = index + 1
            return new_group


class Group(BaseGroup):
    initial_message = models.StringField()
    message = models.LongStringField(
        label="A présent, merci de réécrire le message que vous avez lu dans l’espace ci-dessous. "
              "Merci d’essayer d’évoquer toutes les informations dont vous parvenez à vous souvenir."
    )

    def set_initial_message(self):
        self.initial_message = Constants.c_initial_messages[self.id_in_subsession % len(Constants.c_initial_messages)]

    def propagate_data(self):
        for p in self.get_players():
            for pp in p.in_rounds(2, Constants.num_rounds):
                pp.rank_in_chain = p.rank_in_chain


class Player(BasePlayer):
    rank_in_chain = models.PositiveIntegerField()
    expiration_time = models.FloatField()
    # Data for identification questions
    gender = models.StringField(label="Vous êtes:",
                                choices=["un homme", "une femme"],
                                widget=widgets.RadioSelectHorizontal())
    age = models.PositiveIntegerField(label="Votre âge (merci d’indiquer votre âge en chiffres):",)


from . import pages
