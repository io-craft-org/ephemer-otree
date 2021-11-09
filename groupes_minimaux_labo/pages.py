from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import time
import random


#################################################
# Common
#################################################

class ConsignesPage(Page):
    pass

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



#################################################
# Treatment announcement
#################################################
class PersonalityResultsPage(Page):
    pass


#################################################
# Questions page
#################################################
class Questions_Page(Page):
    form_model = 'player'
    form_fields = ['appreciate_picturaux', 'identify_to_picturaux',
                   'appreciate_experientiels', 'identify_to_experientiels']


#################################################
# Matrices pages: fixed order, differentiated inside the template according to the treatment
#################################################

class Matrix1Page(Page):
    form_model = 'player'
    form_fields = ['matrix1_response']

class Matrix2Page(Page):
    form_model = 'player'
    form_fields = ['matrix2_response']



#################################################
# Representations questions randomized order
#################################################


class RepresentationsV2Page1(Page):
    form_model = 'player'

    def get_form_fields(self): # comme un formfields mais pour sortir une liste avec opérations dessus
        questions_list = ["studies_require_work", "studies_require_investment", "studies_give_knowledge",
                          "studies_prepare_future", "studies_imply_exams", "studies_imply_diplomas",
                          "studies_access_culture", "studies_long_term", "studies_university"]
        random.shuffle(questions_list)
        # ici petit ajout = on concatène la question_list avec des virgules en string pour le mettre dans player.order défini dans models
        self.player.order1 = ",".join(questions_list)
        return questions_list # pour créer une variable de sortie (équivalent aux var de sorties entre crochets sous matlab ([ici, ici] = func(x, y))


# ici fonction de validation une fois le bouton next appuyé à la fin de cette page
    # pour rappel les c_representations_v2_vhoices = ["+", "-", "non choisi"]
    # error message est une fonction django qui permet de ne pas valider la page si error message envoyé

    def error_message(self, values):
        answers = list(values.values())
        if (answers.count("Accord") != 3) \
                | (answers.count("Désaccord") != 3) \
                | (answers.count("Neutre") != 3):
            return "Vous devez sélectionner 3 propositions par catégorie (Accord, Désaccord, Neutre)."

    def is_displayed(self):
        from pprint import pprint
        print("SESSION CONFIG")
        pprint(self.session.config)
        return self.session.config['representation_or_imputation'] == "representation"


class RepresentationsV2Page2(Page):
    form_model = 'player'

    def get_form_fields(self):
        questions_list = ["ideal_group_no_cheaf", "ideal_group_positive_relations", "ideal_group_frequent_meetings",
                          "ideal_group_same_interests", "ideal_group_same_activities", "ideal_group_proximity",
                          "ideal_group_same_opinion", "ideal_group_same_background"]
        random.shuffle(questions_list)
        # ici petit ajout = on concatène la question_list avec des virgules en string pour le mettre dans player.order défini dans models
        self.player.order2 = ",".join(questions_list)
        return questions_list

    def error_message(self, values):
        answers = list(values.values())
        if (answers.count("Accord") != 3) \
                | (answers.count("Désaccord") != 3) \
                | (answers.count("Neutre") != 2):
            return "Vous devez sélectionner 3 propositions pour chacune des catégories 'Accord' et 'Désaccord', et 2 propositions pour la catégorie 'Neutre'."

    def is_displayed(self):
        return self.session.config['representation_or_imputation'] == "representation"


class ImputationPage1(Page):
    form_model = 'player'
    form_fields = ['experientiels_studies_1', 'experientiels_studies_2',
                   'experientiels_studies_3', 'experientiels_studies_4',
                   'picturaux_studies_1', 'picturaux_studies_2',
                   'picturaux_studies_3', 'picturaux_studies_4'
                   ]

    def is_displayed(self):
        return self.session.config['representation_or_imputation'] == "imputation"


class ImputationPage2(Page):
    form_model = 'player'
    form_fields = ['experientiels_ideal_friend_group_1', 'experientiels_ideal_friend_group_2',
                   'experientiels_ideal_friend_group_3', 'experientiels_ideal_friend_group_4',
                   'picturaux_ideal_friend_group_1', 'picturaux_ideal_friend_group_2',
                   'picturaux_ideal_friend_group_3', 'picturaux_ideal_friend_group_4'
                   ]

    def is_displayed(self):
        return self.session.config['representation_or_imputation'] == "imputation"

# CA PEUT SERVIR : relique de l'époque où on n'enregistrait pas le self_or_other dans les data, maintenant le système est inclu dans subsession dans model
    # def vars_for_template(self):
    #     return {
    #         'Self_or_other_first': random.choice(['self', 'other'])
    #     }


#################################################
#################################################
class IdentificationPage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age']


class MerciPage(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


#################################################
# Build of page sequence
#################################################


page_sequence = [
    ConsignesPage,
    Test1_Page,
    Test2_Page,
    Test3_Page,
    Test4_Page,
    Test5_Page,
    PersonalityResultsPage,
    Questions_Page,
    Matrix1Page,
    Matrix2Page,
    RepresentationsV2Page1,
    RepresentationsV2Page2,
    ImputationPage1,
    ImputationPage2,
    IdentificationPage,
    MerciPage
]

