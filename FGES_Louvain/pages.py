from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage

from .models import Constants


class ConsignesPage(Page):
      def vars_for_template(self):
        return {'perso': self.player.perso}

class Test1_Page(Page):
    form_model = 'player'
    form_fields = ['test1_answer']

class Test2_Page(Page):
    form_model = 'player'
    form_fields = ['test2_answer']

class Test3_Page(Page):
    form_model = 'player'
    form_fields = ['test3_answer']

class Test4_Page(Page):
    form_model = 'player'
    form_fields = ['test4_answer']

class Test5_Page(Page):
    form_model = 'player'
    form_fields = ['test5_answer']


class PersonalityResultsPage(Page):
    def vars_for_template(self):
        return {'perso': self.player.perso}


#################################################
# Questions page
#################################################
class Questions_Page(Page):
    form_model = 'player'
    form_fields = ['appreciate_focal', 'identify_to_focal',
                   'appreciate_holi', 'identify_to_holi']
    def vars_for_template(self):
        return {'perso': self.player.perso}

class Matrices_1(Page):
    form_model = 'player'
    form_fields = ['matrix1_response',]
    def vars_for_template(self):
        return {'perso': self.player.perso}

class Matrices_2(Page):
    form_model = 'player'
    form_fields = ['matrix2_response',]
    def vars_for_template(self):
        return {'perso': self.player.perso}

class ConsignesGroupeFictif(Page):
    pass

class GroupfictExample(Page):
    form_model = 'player'
    form_fields = ['group_fict_example_1', 'group_fict_example_2', 'slider_fictex_1', 'slider_fictex_2']
    def vars_for_template(self):
        return {'perso': self.player.perso}


class WaitPage_1(Page):
    pass

class WaitPage_2(Page):
    pass

class GroupfictFeedback1(Page):
    pass

class GroupfictFeedback2(Page):
    form_model = 'player'
    form_fields = ['group_fict_real_1', 'group_fict_real_2', 'group_fict_real_3']

    def hello(self):
        self.vars_for_template()

class GroupfictFeedback3(Page):
    def vars_for_template(self):
        return {'perso': self.player.perso}

class Questions_Page_phase4_focalises(Page):
    form_model = 'player'
    form_fields = ['nous_groupe', 'nous_similaires', 'vision_commune', 'travail_ensemble', 'mots_nouveaux',
                   'amelioration', 'appreciate_self', 'identify_to_self', 'heureux',
                   'faisant_partie', 'meilleurs', 'sentiment_membre', 'satisfait', 'appartenance']
    def is_displayed(self):
        return self.player.perso == 'focal'

class Questions_Page_phase4_holistiques(Page):
    form_model = 'player'
    form_fields = ['nous_groupe', 'nous_similaires', 'vision_commune', 'travail_ensemble', 'mots_nouveaux',
                   'amelioration', 'appreciate_self', 'identify_to_self', 'heureux',
                   'faisant_partie', 'meilleurs', 'sentiment_membre', 'satisfait', 'appartenance']
    def is_displayed(self):
        return self.player.perso == 'holi'


class infos_page(Page):
    form_model = 'player'
    form_fields = ['sexe', 'age']


class fin(Page):
    pass

page_sequence = [ConsignesPage,
                 Test1_Page, Test2_Page, Test3_Page, Test4_Page, Test5_Page, PersonalityResultsPage,
                 Questions_Page,
                 Matrices_1, Matrices_2,
                 ConsignesGroupeFictif, GroupfictExample,
                 WaitPage_1,
                 GroupfictFeedback1, GroupfictFeedback2, GroupfictFeedback3,
                 Questions_Page_phase4_focalises, Questions_Page_phase4_holistiques,
                 infos_page, fin]
