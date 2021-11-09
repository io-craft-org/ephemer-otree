from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Flovic Gosselin / Antoine Deplancke'

doc = """
Expérience Maxime Prost refonte Juin 2019
"""


#################################################
#################################################
class Constants(BaseConstants):
    name_in_url = 'groupes_minimaux_labo'
    players_per_group = None
    num_rounds = 1

    # Constants for XP itself
    # c_timeout_inseconds = 120
    #############################################
    #############################################
    c_treatments = ["Picturaux"]  # In the laboratory version all participants are said to be "picturaux"
    # c_treatments = ["Picturaux", "Expérientiels"] # In the classroom version participants are divided in 2 groups
    #############################################
    c_repartition_information = ["48/52", "52/48"]
    #############################################
    #############################################
    c_agreement_levels = ["Certainement non", "Probablement non", "Probablement oui", "Certainement oui"]
    c_representations_v2_choices = ["Désaccord", "Accord", "Neutre"]
    Self_or_other = ["self", "other"]

class Subsession(BaseSubsession):
    def creating_session(self):
        # Initialise subsession variables
        # Create the necessary session variables

        for g in self.get_groups():
            # Initialise groups variables
            # Initialise players variables
            treatments = itertools.cycle(Constants.c_treatments)
            repartition_info = itertools.cycle(Constants.c_repartition_information)
            Self_or_other_first = itertools.cycle(Constants.Self_or_other)

# ANCIENNE VERSION, mais modifs car on n'a qu'un seul round
            # for p in g.get_players():
            #     if self.round_number == 1:
            #         # Do not initialise fields that need to be filled by the players
            #         # to not have default values displayed
            #         # Declare and initialise the participant dictionary
            #         p.treatment = next(treatments)
            #         p.repartition_information = next(repartition_info)
            #         p.Self_or_other_first = next(Self_or_other_first)
            #         # Randomize the sequence in which the cases are presented
            #     p.treatment = p.in_round(1).treatment
            #     p.Self_or_other_first = p.in_round(1).Self_or_other_first

            for p in g.get_players():

                 # Do not initialise fields that need to be filled by the players
                    # to not have default values displayed
                    # Declare and initialise the participant dictionary
                p.treatment = next(treatments)
                p.repartition_information = next(repartition_info)
                p.Self_or_other_first = next(Self_or_other_first)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    order1 = models.StringField() # pour récupérer la liste shuffle random des question dans representationpage 1
    order2 = models.StringField()  # pour récupérer la liste shuffle random des question dans representationpage 2

    # Data for XP mechanics
    page_sequence = models.StringField()
    treatment = models.StringField()
    repartition_information = models.StringField()
    Self_or_other_first = models.StringField()


    # Data for XP results
    # Data for personality test
    test1_answer = models.StringField(choices=["A", "B"])
    test2_answer = models.StringField(choices=["A", "B"])
    test3_answer = models.StringField(choices=["A", "B"])
    test4_answer = models.StringField(choices=["A", "B"])
    test5_answer = models.StringField(choices=["A", "B"])
    # Data for questions_page
    appreciate_picturaux = models.PositiveIntegerField(label="J’apprécie le groupe des picturaux :",
                                                       initial=25,
                                                       min=1, max=50, widget=widgets.Slider(attrs={'step': '1'}))
    identify_to_picturaux = models.PositiveIntegerField(label="Je m’identifie au groupe des picturaux :",
                                                        initial=25,
                                                        min=1, max=50, widget=widgets.Slider(attrs={'step': '1'}))
    appreciate_experientiels = models.PositiveIntegerField(label="J’apprécie le groupe des expérientiels :",
                                                           initial=25,
                                                           min=1, max=50, widget=widgets.Slider(attrs={'step': '1'}))
    identify_to_experientiels = models.PositiveIntegerField(label="Je m’identifie au groupe des expérientiels :",
                                                            initial=25,
                                                            min=1, max=50, widget=widgets.Slider(attrs={'step': '1'}))
    # Data for matrices
    matrix1_response = models.StringField()
    matrix2_response = models.StringField()

    studies_require_work = models.StringField(
        label="Les études demandent du travail",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_require_investment = models.StringField(
        label="Les études demandent de l'investissement",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_give_knowledge = models.StringField(
        label="Les études permettent d'acquérir des connaissances",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_prepare_future = models.StringField(
        label="Les études permettent permettent de préparer son avenir",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_imply_exams = models.StringField(
        label="Les études impliquent la passation d'examens",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_imply_diplomas = models.StringField(
        label="Les études impliquent l'acquisition de diplômes",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_access_culture = models.StringField(
        label="Les études favorisent l'accès à un haut niveau de culture",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_long_term = models.StringField(
        label="Les études sont une activité de longue haleine",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    studies_university = models.StringField(
        label="Les études se déroulent à l'Université",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    # Data for representations questions V2, page 2
    ideal_group_no_cheaf = models.StringField(
        label="Dans le groupe idéal, il n'y a pas de chef",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_positive_relations = models.StringField(
        label="Dans le groupe idéal, les relations sont positives",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_frequent_meetings = models.StringField(
        label="Dans le groupe idéal, les personnes se réunissent souvent",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_same_interests = models.StringField(
        label="Dans le groupe idéal, les personnes partagent les mêmes intérêts",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_same_activities = models.StringField(
        label="Dans le groupe idéal, les personnes partagent les mêmes activités",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_proximity = models.StringField(
        label="Dans le groupe idéal, les personnes habitent à proximité",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_same_opinion = models.StringField(
        label="Dans le groupe idéal, les personnes partagent les mêmes opinions",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    ideal_group_same_background = models.StringField(
        label="Dans le groupe idéal, les personnes sont du même milieu",
        choices=Constants.c_representations_v2_choices,
        widget=widgets.RadioSelectHorizontal()
    )
    # Imputation question 1
    experientiels_studies_1 = models.StringField(label="", max_length=30)
    experientiels_studies_2 = models.StringField(label="", max_length=30)
    experientiels_studies_3 = models.StringField(label="", max_length=30)
    experientiels_studies_4 = models.StringField(label="", max_length=30)
    picturaux_studies_1 = models.StringField(label="", max_length=30)
    picturaux_studies_2 = models.StringField(label="", max_length=30)
    picturaux_studies_3 = models.StringField(label="", max_length=30)
    picturaux_studies_4 = models.StringField(label="", max_length=30)

    # Imputation question 2
    experientiels_ideal_friend_group_1 = models.StringField(label="", max_length=30)
    experientiels_ideal_friend_group_2 = models.StringField(label="", max_length=30)
    experientiels_ideal_friend_group_3 = models.StringField(label="", max_length=30)
    experientiels_ideal_friend_group_4 = models.StringField(label="", max_length=30)
    picturaux_ideal_friend_group_1 = models.StringField(label="", max_length=30)
    picturaux_ideal_friend_group_2 = models.StringField(label="", max_length=30)
    picturaux_ideal_friend_group_3 = models.StringField(label="", max_length=30)
    picturaux_ideal_friend_group_4 = models.StringField(label="", max_length=30)
    # Data for identification questions
    gender = models.StringField(label="Vous êtes:",
                                choices=["un homme", "une femme"],
                                widget=widgets.RadioSelectHorizontal())
    age = models.PositiveIntegerField(label="Votre âge:",)

