from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'voiture'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # ofi = open("./redirect/sessionState.txt", "w")
        # ofi.write("running")
        # ofi.close()
        for p in self.get_players():
            p.treatment = p.role()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField(choices = ['Conducteur', 'Decideur'])
    pop1_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop1_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop1_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop2_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop2_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop2_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop3_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop3_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop3_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop4_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop4_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop4_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop5_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop5_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop5_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop6_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop6_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop6_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop7_nb1 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop7_nb2 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop7_nb3 = models.IntegerField(choices=[0, 1, 2],
                                   initial=0)
    pop8_leg1 = models.IntegerField(choices=[0, 1, 2],
                                    initial=0)
    pop8_leg2 = models.IntegerField(choices=[0, 1, 2],
                                    initial=0)

    def role(self):
        return {0: 'Conducteur', 1: 'Decideur'}[(self.id_in_group)%2]
