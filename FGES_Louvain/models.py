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
                                                   min=0, max=50, step=1, widget=widgets.SliderWidget)
    identify_to_focal = models.PositiveIntegerField(label="Je m’identifie au groupe des Focalisés :",
                                                    initial=25,
                                                    min=0, max=50, step=1, widget=widgets.SliderWidget)
    appreciate_holi = models.PositiveIntegerField(label="J’apprécie le groupe des Holistiques :",
                                                  initial=25,
                                                  min=0, max=50, step=1, widget=widgets.SliderWidget)
    identify_to_holi = models.PositiveIntegerField(label="Je m’identifie au groupe des Holistiques :",
                                                   initial=25,
                                                   min=0, max=50, step=1, widget=widgets.SliderWidget)
    # Question et Data for gruop fictif examples
    group_fict_example_1 = models.StringField(label="Fil :", choices=["Electrique", "Aiguille", "Corde", "Pêche"], widget=widgets.RadioSelect)
    group_fict_example_2 = models.StringField(label="Stylo :", choices=["Mine", "Encre", "Feuille", "Plume"], widget=widgets.RadioSelect)

    slider_fictex_1 = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    slider_fictex_2 = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    group_fict_real_1 = models.StringField(label="Plante :", choices=["Oxygène", "Fleur", "Feuille", "Verte"], widget=widgets.RadioSelect)
    group_fict_real_2 = models.StringField(label="Voiture :", choices=["Roue", "Essence", "Moto", "Moteur"], widget=widgets.RadioSelect)
    group_fict_real_3 = models.StringField(label="Bouteille :", choices=["Verre", "Alcool", "Bouchon", "Vin"], widget=widgets.RadioSelect)

    nous_groupe = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    nous_similaires = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    vision_commune = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    travail_ensemble = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    mots_nouveaux = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    amelioration = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    appreciate_self = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    identify_to_self = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    appartenance = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    heureux = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    faisant_partie = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    meilleurs = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    sentiment_membre = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)

    satisfait = models.PositiveIntegerField(
        label="(Déplacez le curseur sur la position qui reflète le mieux votre estimation)",
        initial=50, min=0, max=100, step=1, widget=widgets.SliderWidget)
