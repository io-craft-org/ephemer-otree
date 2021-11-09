from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


##################################
class InformationPage(Page):
    def vars_for_template(self):
        # At the beginning of this first page, set the participant's URL so that he can stop and come back later
        parti = self.request.build_absolute_uri(self.player.participant._start_url())
        self.request.session["otree"] = parti
        self.request.session.set_expiry(18000)
        return {
            'role': self.player.role(),
        }


##################################
class Pop1Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop1_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop1Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop1_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop1Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop1_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }

# -------------------------------
class Pop2Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop2_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop2Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop2_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop2Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop2_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop3Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop3_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop3Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop3_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop3Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop3_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop4Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop4_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop4Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop4_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop4Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop4_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop5Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop5_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop5Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop5_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop5Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop5_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop6Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop6_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop6Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop6_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop6Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop6_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop7Nb1Page(Page):
    form_model = models.Player
    form_fields = ['pop7_nb1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop7Nb2Page(Page):
    form_model = models.Player
    form_fields = ['pop7_nb2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop7Nb3Page(Page):
    form_model = models.Player
    form_fields = ['pop7_nb3']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


# -------------------------------
class Pop8Leg1Page(Page):
    form_model = models.Player
    form_fields = ['pop8_leg1']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


class Pop8Leg2Page(Page):
    form_model = models.Player
    form_fields = ['pop8_leg2']

    def vars_for_template(self):
        return {
            'role': self.player.role(),
        }


##################################
class MerciPage(Page):
    pass


##################################
page_sequence = [
    InformationPage,
    Pop1Nb1Page,
    Pop1Nb2Page,
    Pop1Nb3Page,
    Pop2Nb1Page,
    Pop2Nb2Page,
    Pop2Nb3Page,
    Pop3Nb1Page,
    Pop3Nb2Page,
    Pop3Nb3Page,
    Pop4Nb1Page,
    Pop4Nb2Page,
    Pop4Nb3Page,
    Pop5Nb1Page,
    Pop5Nb2Page,
    Pop5Nb3Page,
    Pop6Nb1Page,
    Pop6Nb2Page,
    Pop6Nb3Page,
    Pop7Nb1Page,
    Pop7Nb2Page,
    Pop7Nb3Page,
    Pop8Leg1Page,
    Pop8Leg2Page,
    MerciPage
]
