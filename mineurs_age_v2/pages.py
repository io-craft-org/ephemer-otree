from otree.api import Currency as c, currency_range
from otree.models import player

from ._builtin import Page, WaitPage
from .models import Constants
import json
import time
import otree.models.player

#################################################
# Common Identification
#################################################


class InfosGeneralesPage(Page):
    # timeout_seconds = Constants.c_timeout_inseconds

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        pass
        #  # For automatic inactive pushing
        #  if self.timeout_happened is False:
        #      self.player.participant.vars['active_flag'] = time.time()
        #  # End-For automatic inactive pushing


class DeroulementPage(Page):
    # timeout_seconds = Constants.c_timeout_inseconds

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        pass
        #  # For automatic inactive pushing
        #  if self.timeout_happened is False:
        #      self.player.participant.vars['active_flag'] = time.time()
        #  # End-For automatic inactive pushing


#################################################
# Treatment
#################################################
class Instructions_impact_or_not(Page):
    # timeout_seconds = Constants.c_timeout_inseconds
    def vars_for_template(self):
        print(self.player.coupable)
        return {'coupable': self.player.coupable}

class Instructions_impact_or_not2(Page):
    # timeout_seconds = Constants.c_timeout_inseconds
    def vars_for_template(self):
        print(self.player.coupable)
        return {'coupable': self.player.coupable}

#################################################
# Common and fixed order
#################################################
class InfosG_asana(Page):
   def vars_for_template(self):
       linkim = 'mineurs_age_v2/IG_asana.png'
       return {'link': linkim}

    # def before_next_page(self):
    #     pass
    #     #  # For automatic inactive pushing
    #     #  if self.timeout_happened is False:
    #     #      self.player.participant.vars['active_flag'] = time.time()
    #     #  # End-For automatic inactive pushing

class Photo_asana(Page):
    form_model = 'player'
    form_fields = ['age_cas1_Photo', 'confidence_cas1_Photo']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Photo_asana.png'
        return {'link': linkim}

class Entretien_asana(Page):
    form_model = 'player'
    form_fields = ['age_cas1_Entretien', 'confidence_cas1_Entretien']
    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Entretien_asana.png'
        return {'link': linkim}

class Etat_civil_asana(Page):
    form_model = 'player'
    form_fields = ['age_cas1_Etat_civil', 'confidence_cas1_Etat_civil']
    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Etat_civil_asana.png'
        return {'link': linkim}

class test_osseux_asana(Page):
    form_model = 'player'
    form_fields = ['age_cas1_test_oss', 'confidence_cas1_test_oss']
    def vars_for_template(self):
        linkim = 'mineurs_age_v2/test_osseux_asana.png'
        return {'link': linkim}

class InfosG_diallo(Page):
    def vars_for_template(self):
       linkim = 'mineurs_age_v2/IG_diallo.png'
       return {'link': linkim}

    # def before_next_page(self):
    #     pass
    #     #  # For automatic inactive pushing
    #     #  if self.timeout_happened is False:
    #     #      self.player.participant.vars['active_flag'] = time.time()
    #     #  # End-For automatic inactive pushing


class Photo_diallo(Page):
    form_model = 'player'
    form_fields = ['age_cas2_Photo', 'confidence_cas2_Photo']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Photo_diallo.png'
        return {'link': linkim}


class Entretien_diallo(Page):
    form_model = 'player'
    form_fields = ['age_cas2_Entretien', 'confidence_cas2_Entretien']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Entretien_diallo.png'
        return {'link': linkim}


class Etat_civil_diallo(Page):
    form_model = 'player'
    form_fields = ['age_cas2_Etat_civil', 'confidence_cas2_Etat_civil']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Etat_civil_diallo.png'
        return {'link': linkim}


class test_osseux_diallo(Page):
    form_model = 'player'
    form_fields = ['age_cas2_test_oss', 'confidence_cas2_test_oss']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/test_osseux_diallo.png'
        return {'link': linkim}

class InfosG_jamal(Page):
    def vars_for_template(self):
       linkim = 'mineurs_age_v2/IG_jamal.png'
       return {'link': linkim}

    # def before_next_page(self):
    #     pass
    #     #  # For automatic inactive pushing
    #     #  if self.timeout_happened is False:
    #     #      self.player.participant.vars['active_flag'] = time.time()
    #     #  # End-For automatic inactive pushing


class Photo_jamal(Page):
    form_model = 'player'
    form_fields = ['age_cas3_Photo', 'confidence_cas3_Photo']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Photo_jamal.png'
        return {'link': linkim}


class Entretien_jamal(Page):
    form_model = 'player'
    form_fields = ['age_cas3_Entretien', 'confidence_cas3_Entretien']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Entretien_jamal.png'
        return {'link': linkim}


class Etat_civil_jamal(Page):
    form_model = 'player'
    form_fields = ['age_cas3_Etat_civil', 'confidence_cas3_Etat_civil']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Etat_civil_jamal.png'
        return {'link': linkim}


class test_osseux_jamal(Page):
    form_model = 'player'
    form_fields = ['age_cas3_test_oss', 'confidence_cas3_test_oss']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/test_osseux_jamal.png'
        return {'link': linkim}

class InfosG_amadou(Page):
    def vars_for_template(self):
       linkim = 'mineurs_age_v2/IG_amadou.png'
       return {'link': linkim}

    # def before_next_page(self):
    #     pass
    #     #  # For automatic inactive pushing
    #     #  if self.timeout_happened is False:
    #     #      self.player.participant.vars['active_flag'] = time.time()
    #     #  # End-For automatic inactive pushing

class Photo_amadou(Page):
    form_model = 'player'
    form_fields = ['age_cas4_Photo', 'confidence_cas4_Photo']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Photo_amadou.png'
        return {'link': linkim}


class Entretien_amadou(Page):
    form_model = 'player'
    form_fields = ['age_cas4_Entretien', 'confidence_cas4_Entretien']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Entretien_amadou.png'
        return {'link': linkim}


class Etat_civil_amadou(Page):
    form_model = 'player'
    form_fields = ['age_cas4_Etat_civil', 'confidence_cas4_Etat_civil']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Etat_civil_amadou.png'
        return {'link': linkim}


class test_osseux_amadou(Page):
    form_model = 'player'
    form_fields = ['age_cas4_test_oss', 'confidence_cas4_test_oss']

    def vars_for_template(self):
        if self.player.coupable == 'yes':
          linkim = 'mineurs_age_v2/test_osseux_amadou_A.png'
        else:
           linkim = 'mineurs_age_v2/test_osseux_amadou_B.png'
        return {'link': linkim}


class InfosG_aboubacar(Page):
    def vars_for_template(self):
       linkim = 'mineurs_age_v2/IG_aboubacar.png'
       return {'link': linkim}

    # def before_next_page(self):
    #     pass
    #     #  # For automatic inactive pushing
    #     #  if self.timeout_happened is False:
    #     #      self.player.participant.vars['active_flag'] = time.time()
    #     #  # End-For automatic inactive pushing

class Photo_aboubacar(Page):
    form_model = 'player'
    form_fields = ['age_cas5_Photo', 'confidence_cas5_Photo']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Photo_aboubacar.png'
        return {'link': linkim}


class Entretien_aboubacar(Page):
    form_model = 'player'
    form_fields = ['age_cas5_Entretien', 'confidence_cas5_Entretien']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Entretien_aboubacar.png'
        return {'link': linkim}


class Etat_civil_aboubacar(Page):
    form_model = 'player'
    form_fields = ['age_cas5_Etat_civil', 'confidence_cas5_Etat_civil']

    def vars_for_template(self):
        linkim = 'mineurs_age_v2/Etat_civil_aboubacar.png'
        return {'link': linkim}


class test_osseux_aboubacar(Page):
    form_model = 'player'
    form_fields = ['age_cas5_test_oss', 'confidence_cas5_test_oss']

    def vars_for_template(self):
        if self.player.coupable == 'yes':
          linkim = 'mineurs_age_v2/test_osseux_aboubacar_A.png'
        else:
           linkim = 'mineurs_age_v2/test_osseux_aboubacar_B.png'
        return {'link': linkim}

class MerciPage(Page):
    pass
     # def is_displayed(self):
     #     return self.subsession.round_number == Constants.num_rounds


#################################################
# page sequence
#################################################

page_sequence = [
    InfosGeneralesPage,
    DeroulementPage,
    Instructions_impact_or_not,
    InfosG_asana,
    Photo_asana,
    Entretien_asana,
    Etat_civil_asana,
    test_osseux_asana,
    InfosG_diallo,
    Photo_diallo,
    Entretien_diallo,
    Etat_civil_diallo,
    test_osseux_diallo,
    InfosG_jamal,
    Photo_jamal,
    Entretien_jamal,
    Etat_civil_jamal,
    test_osseux_jamal,
    Instructions_impact_or_not2,
    InfosG_amadou,
    Photo_amadou,
    Entretien_amadou,
    Etat_civil_amadou,
    test_osseux_amadou,
    InfosG_aboubacar,
    Photo_aboubacar,
    Entretien_aboubacar,
    Etat_civil_aboubacar,
    test_osseux_aboubacar,
    MerciPage]



