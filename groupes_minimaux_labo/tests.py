from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.ConsignesPage)
        yield (pages.Test1_Page, {'test1_answer': random.choice(['A', 'B'])})
        yield (pages.Test2_Page, {'test2_answer': random.choice(['A', 'B'])})
        yield (pages.Test3_Page, {'test3_answer': random.choice(['A', 'B'])})
        yield (pages.Test4_Page, {'test4_answer': random.choice(['A', 'B'])})
        yield (pages.Test5_Page, {'test5_answer': random.choice(['A', 'B'])})
        yield (pages.PersonalityResultsPage)
        yield (pages.Questions_Page, {'appreciate_picturaux': random.randint(1, 50),
                                      'identify_to_picturaux': random.randint(1, 50),
                                      'appreciate_experientiels': random.randint(1, 50),
                                      'identify_to_experientiels': random.randint(1, 50)})
        yield (pages.Matrix1Page, {'matrix1_response': random.choice([
            "19_1", "18_3", "17_5", "16_7", "15_9", "14_11", "13_13",
            "12_15", "11_17", "10_19", "9_21", "8_23", "7_25"])})
        yield (pages.Matrix2Page, {'matrix2_response': random.choice([
            "11_5", "12_7", "13_9", "14_11", "15_13", "16_15", "17_17",
            "18_19", "19_21", "20_23", "21_25", "22_27", "23_29"])})
        # V1:  yield (pages.RepresentationsGeneralPresentationPage)
        # V1:  yield (pages.Page_0, {'idealgroup_nocheaf_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'idealgroup_nocheaf_mygroupagree': random.randint(1, 100),
        # V1:                        'idealgroup_nocheaf_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.Page_1, {'idealgroup_sameenvironment_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'idealgroup_sameenvironment_mygroupagree': random.randint(1, 100),
        # V1:                        'idealgroup_sameenvironment_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.Page_2, {'wastesorting_useful_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'wastesorting_useful_mygroupagree': random.randint(1, 100),
        # V1:                        'wastesorting_useful_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.Page_3, {'wastesorting_clean_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'wastesorting_clean_mygroupagree': random.randint(1, 100),
        # V1:                        'wastesorting_clean_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.Page_4, {'studies_knowledge_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'studies_knowledge_mygroupagree': random.randint(1, 100),
        # V1:                        'studies_knowledge_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.Page_5, {'studies_culture_iagree': random.choice(Constants.c_agreement_levels),
        # V1:                        'studies_culture_mygroupagree': random.randint(1, 100),
        # V1:                        'studies_culture_othergroupagree': random.randint(1, 100)})
        # V1:  yield (pages.IdentificationPage, {'gender': random.choice(["un homme", "une femme"]),
        # V1:                                    'age': random.randint(20, 100)})

        answering_list = ["studies_require_work", "studies_require_investment", "studies_give_knowledge",
                          "studies_prepare_future", "studies_imply_exams", "studies_imply_diplomas",
                          "studies_access_culture", "studies_long_term", "studies_university"]
        random.shuffle(answering_list)
        answering_dict = {
            answering_list[0]: Constants.c_representations_v2_choices[0],
            answering_list[1]: Constants.c_representations_v2_choices[0],
            answering_list[2]: Constants.c_representations_v2_choices[0],
            answering_list[3]: Constants.c_representations_v2_choices[1],
            answering_list[4]: Constants.c_representations_v2_choices[1],
            answering_list[5]: Constants.c_representations_v2_choices[1],
            answering_list[6]: Constants.c_representations_v2_choices[2],
            answering_list[7]: Constants.c_representations_v2_choices[2],
            answering_list[8]: Constants.c_representations_v2_choices[2],
        }
        yield (pages.RepresentationsV2Page1, answering_dict)
        answering_list2 = ["ideal_group_no_cheaf", "ideal_group_positive_relations", "ideal_group_frequent_meetings",
                           "ideal_group_same_interests", "ideal_group_same_activities", "ideal_group_proximity",
                           "ideal_group_same_opinion", "ideal_group_same_background"]
        random.shuffle(answering_list2)
        answering_dict2 = {
            answering_list2[0]: Constants.c_representations_v2_choices[0],
            answering_list2[1]: Constants.c_representations_v2_choices[0],
            answering_list2[2]: Constants.c_representations_v2_choices[0],
            answering_list2[3]: Constants.c_representations_v2_choices[1],
            answering_list2[4]: Constants.c_representations_v2_choices[1],
            answering_list2[5]: Constants.c_representations_v2_choices[1],
            answering_list2[6]: Constants.c_representations_v2_choices[2],
            answering_list2[7]: Constants.c_representations_v2_choices[2],
        }
        yield (pages.RepresentationsV2Page2, answering_dict2)
        yield (pages.IdentificationPage, {
            'gender': random.choice(['un homme', 'une femme']),
            'age': random.randint(20, 70),
        })
        # No NextButton on the MerciPage: yield (pages.MerciPage)
