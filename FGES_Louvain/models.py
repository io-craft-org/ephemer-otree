from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
author = 'Antoine Deplancke'

doc = """
Manip Ephemer FGES Louvain
"""


class Constants(BaseConstants):
    name_in_url = 'FGES_Louvain'
    players_per_group = None
    num_rounds = 1
    perso_list = ['focal', 'holi']

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # Déterminer la personnalité
            for p in self.get_players():
                p.perso = random.choice(Constants.perso_list)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    perso = models.StringField()
    sexe = models.StringField(choices=["Une Femme", "Un Homme"], label='')
    age = models.IntegerField(min = 15, max= 100, label='')

    # Data for personality test
    test1_answer = models.StringField(choices=["A", "B"])
    test2_answer = models.StringField(choices=["A", "B"])
    test3_answer = models.StringField(choices=["A", "B"])
    test4_answer = models.StringField(choices=["A", "B"])
    test5_answer = models.StringField(choices=["A", "B"])
    # Data for matrices
    matrix1_response = models.StringField()
    matrix2_response = models.StringField()
    # Data for questions_page
    appreciate_focal = models.PositiveIntegerField(label="J’apprécie le groupe des Focalisés :",
                                                   initial=25,
                                                   min=0, max=50)
    identify_to_focal = models.PositiveIntegerField(label="Je m’identifie au groupe des Focalisés :",
                                                    initial=25,
                                                    min=0, max=50)
    appreciate_holi = models.PositiveIntegerField(label="J’apprécie le groupe des Holistiques :",
                                                  initial=25,
                                                  min=0, max=50)
    identify_to_holi = models.PositiveIntegerField(label="Je m’identifie au groupe des Holistiques :",
                                                   initial=25,
                                                   min=0, max=50)
    # Question et Data for gruop fictif examples
    group_fict_example_1 = models.StringField(label="Fil :", choices=["Electrique", "Aiguille", "Corde", "Pêche"], widget=widgets.RadioSelect)
    group_fict_example_2 = models.StringField(label="Stylo :", choices=["Mine", "Encre", "Feuille", "Plume"], widget=widgets.RadioSelect)

    slider_fictex_1 = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    slider_fictex_2 = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    group_fict_real_1 = models.StringField(label="Plante :", choices=["Oxygène", "Fleur", "Feuille", "Verte"], widget=widgets.RadioSelect)
    group_fict_real_2 = models.StringField(label="Voiture :", choices=["Roue", "Essence", "Moto", "Moteur"], widget=widgets.RadioSelect)
    group_fict_real_3 = models.StringField(label="Bouteille :", choices=["Verre", "Alcool", "Bouchon", "Vin"], widget=widgets.RadioSelect)

    nous_groupe = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    nous_similaires = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    vision_commune = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    travail_ensemble = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    mots_nouveaux = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    amelioration = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    appreciate_self = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    identify_to_self = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    appartenance = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    heureux = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    faisant_partie = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    meilleurs = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    sentiment_membre = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)

    satisfait = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100)
