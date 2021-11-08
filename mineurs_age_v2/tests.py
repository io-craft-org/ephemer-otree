from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):
        if self.subsession.round_number == 1:
            yield (pages.IdentificationPage, {'identifiant': "PlayerBot" + str(self.player.id_in_subsession)})
            if self.player.treatment == Constants.c_treatments[0]:
                yield (pages.E1WithImpactInfoPage)
                yield (pages.E2WithImpactInfoPage)
            if self.player.treatment == Constants.c_treatments[1]:
                yield (pages.E1WithoutImpactInfoPage)
                yield (pages.E2WithoutImpactInfoPage)
            yield (pages.InstructionsPage)
        yield (pages.GeneralCaseInfoPage)
        yield (pages.PicturePage, {'age': random.randint(12, 24),
                                   'confidence_level': random.randrange(start=0, stop=101, step=5)})
        yield (pages.Page_0, {'age': random.randint(12, 24),
                              'confidence_level': random.randrange(start=0, stop=101, step=5)})
        yield (pages.Page_1, {'age': random.randint(12, 24),
                              'confidence_level': random.randrange(start=0, stop=101, step=5)})
        yield (pages.Page_2, {'age': random.randint(12, 24),
                              'confidence_level': random.randrange(start=0, stop=101, step=5)})
        #??? No NextButton on MerciPage: yield (pages.MerciPage)
