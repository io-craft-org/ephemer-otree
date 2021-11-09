from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from random import randint


class PlayerBot(Bot):

    def play_round(self):
        yield (views.InformationPage)
        yield (views.Pop1Nb1Page, {'pop1_nb1': randint(1,2)})
        yield (views.Pop1Nb2Page, {'pop1_nb2': randint(1,2)})
        yield (views.Pop1Nb3Page, {'pop1_nb3': randint(1,2)})
        yield (views.Pop2Nb1Page, {'pop2_nb1': randint(1,2)})
        yield (views.Pop2Nb2Page, {'pop2_nb2': randint(1,2)})
        yield (views.Pop2Nb3Page, {'pop2_nb3': randint(1,2)})
        yield (views.Pop3Nb1Page, {'pop3_nb1': randint(1,2)})
        yield (views.Pop3Nb2Page, {'pop3_nb2': randint(1,2)})
        yield (views.Pop3Nb3Page, {'pop3_nb3': randint(1,2)})
        yield (views.Pop4Nb1Page, {'pop4_nb1': randint(1,2)})
        yield (views.Pop4Nb2Page, {'pop4_nb2': randint(1,2)})
        yield (views.Pop4Nb3Page, {'pop4_nb3': randint(1,2)})
        yield (views.Pop5Nb1Page, {'pop5_nb1': randint(1,2)})
        yield (views.Pop5Nb2Page, {'pop5_nb2': randint(1,2)})
        yield (views.Pop5Nb3Page, {'pop5_nb3': randint(1,2)})
        yield (views.Pop6Nb1Page, {'pop6_nb1': randint(1,2)})
        yield (views.Pop6Nb2Page, {'pop6_nb2': randint(1,2)})
        yield (views.Pop6Nb3Page, {'pop6_nb3': randint(1,2)})
        yield (views.Pop7Nb1Page, {'pop7_nb1': randint(1,2)})
        yield (views.Pop7Nb2Page, {'pop7_nb2': randint(1,2)})
        yield (views.Pop7Nb3Page, {'pop7_nb3': randint(1,2)})
        yield (views.Pop8Leg1Page, {'pop8_leg1': randint(1,2)})
        yield (views.Pop8Leg2Page, {'pop8_leg2': randint(1,2)})
