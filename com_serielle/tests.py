from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):
        #GroupingWaitPage(WaitPage)
        if self.subsession.round_number == 1:
            yield(pages.ConsignePage)
        if self.subsession.round_number == self.player.rank_in_chain:
            yield (pages.MessagingPage,
                   {'message': "Message from group " + str(self.group.id_in_subsession)
                               + " for round " + str(self.subsession.round_number)
                    })
        # SynchroWaitPage(WaitPage)
        if self.subsession.round_number == Constants.num_rounds:
            yield(pages.IdentificationPage, {
                'gender': random.choice(["un homme", "une femme"]),
                'age': random.randint(20, 80),
            })
            # yield(pages.MerciPage)
