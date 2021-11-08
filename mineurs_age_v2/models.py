from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
# For monitoring thread
import threading
import time

author = 'Your name here'

doc = """
Your app description
"""


#################################################
#################################################
class Constants(BaseConstants):
    name_in_url = 'mineurs_age_v2'
    players_per_group = None
    num_rounds = 3
    guilty = ["yes", "no"]
    # c_infos = ["entretien", "etat_civil", "test_osseux"]
    c_timeout_inseconds = 120

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # Déterminer les ordres de passage
            for p in self.get_players():
                p.coupable = random.choice(Constants.guilty)


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    coupable = models.StringField()
    # Data for XP results
    # General level
    # age_evolution = models.StringField()
    # confidence_evolution = models.StringField()
    # age_cas1_IG = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
    #                                   min=12,
    #                                    max=30,
    #                                    step=1, widget=widgets.SliderWidget)
    #
    # age_cas2_IG = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
    #                                        min=12,
    #                                        max=30,
    #                                        step=1, widget=widgets.SliderWidget)
    #
    # age_cas3_IG = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
    #                                        min=12,
    #                                        max=30,
    #                                        step=1, widget=widgets.SliderWidget)
    #
    # age_cas4_IG = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
    #                                        min=12,
    #                                        max=30,
    #                                        step=1, widget=widgets.SliderWidget)
    #
    # age_cas5_IG = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
    #                                        min=12,
    #                                        max=30,
    #                                        step=1, widget=widgets.SliderWidget)
    #
    # confidence_cas1_IG = models.PositiveIntegerField(
    #      max=100,
    #      step=5, widget=widgets.SliderWidget,
    #      label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
    #            "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    #  )
    # confidence_cas2_IG = models.PositiveIntegerField(
    #     max=100,
    #     step=5, widget=widgets.SliderWidget,
    #     label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
    #           "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    # )
    # confidence_cas3_IG = models.PositiveIntegerField(
    #     max=100,
    #     step=5, widget=widgets.SliderWidget,
    #     label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
    #           "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    # )
    # confidence_cas4_IG = models.PositiveIntegerField(
    #     max=100,
    #     step=5, widget=widgets.SliderWidget,
    #     label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
    #           "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    # )
    # confidence_cas5_IG = models.PositiveIntegerField(
    #     max=100,
    #     step=5, widget=widgets.SliderWidget,
    #     label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
    #           "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    # )

    age_cas1_Entretien = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                     min=12,
                                                     max=30,
                                                     step=1, widget=widgets.SliderWidget)

    age_cas2_Entretien = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                     min=12,
                                                     max=30,
                                                     step=1, widget=widgets.SliderWidget)

    age_cas3_Entretien = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                     min=12,
                                                     max=30,
                                                     step=1, widget=widgets.SliderWidget)

    age_cas4_Entretien = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                     min=12,
                                                     max=30,
                                                     step=1, widget=widgets.SliderWidget)

    age_cas5_Entretien = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                     min=12,
                                                     max=30,
                                                     step=1, widget=widgets.SliderWidget)

    confidence_cas1_Entretien = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas2_Entretien = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas3_Entretien = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas4_Entretien = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas5_Entretien = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )

    age_cas1_Photo = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                 min=12,
                                                 max=30,
                                                 step=1, widget=widgets.SliderWidget)

    age_cas2_Photo = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                 min=12,
                                                 max=30,
                                                 step=1, widget=widgets.SliderWidget)

    age_cas3_Photo = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                 min=12,
                                                 max=30,
                                                 step=1, widget=widgets.SliderWidget)

    age_cas4_Photo = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                 min=12,
                                                 max=30,
                                                 step=1, widget=widgets.SliderWidget)

    age_cas5_Photo = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                 min=12,
                                                 max=30,
                                                 step=1, widget=widgets.SliderWidget)

    confidence_cas1_Photo = models.PositiveIntegerField(
         max=100,
         step=5, widget=widgets.SliderWidget,
         label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
               "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
     )
    confidence_cas2_Photo = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas3_Photo = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas4_Photo = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas5_Photo = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )

    age_cas1_test_oss = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                    min=12,
                                                    max=30,
                                                    step=1, widget=widgets.SliderWidget)

    age_cas2_test_oss = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                    min=12,
                                                    max=30,
                                                    step=1, widget=widgets.SliderWidget)

    age_cas3_test_oss = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                    min=12,
                                                    max=30,
                                                    step=1, widget=widgets.SliderWidget)

    age_cas4_test_oss = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                    min=12,
                                                    max=30,
                                                    step=1, widget=widgets.SliderWidget)

    age_cas5_test_oss = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                    min=12,
                                                    max=30,
                                                    step=1, widget=widgets.SliderWidget)

    confidence_cas1_test_oss = models.PositiveIntegerField(
         max=100,
         step=5, widget=widgets.SliderWidget,
         label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
               "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
     )
    confidence_cas2_test_oss = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas3_test_oss = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas4_test_oss = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas5_test_oss = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )

    age_cas1_Etat_civil = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                      min=12,
                                                      max=30,
                                                      step=1, widget=widgets.SliderWidget)

    age_cas2_Etat_civil = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                      min=12,
                                                      max=30,
                                                      step=1, widget=widgets.SliderWidget)

    age_cas3_Etat_civil = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                      min=12,
                                                      max=30,
                                                      step=1, widget=widgets.SliderWidget)

    age_cas4_Etat_civil = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                      min=12,
                                                      max=30,
                                                      step=1, widget=widgets.SliderWidget)

    age_cas5_Etat_civil = models.PositiveIntegerField(label="Quel âge donneriez-vous à ce jeune ?",
                                                      min=12,
                                                      max=30,
                                                      step=1, widget=widgets.SliderWidget)

    confidence_cas1_Etat_civil = models.PositiveIntegerField(
         max=100,
         step=5, widget=widgets.SliderWidget,
         label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
               "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
     )
    confidence_cas2_Etat_civil = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas3_Etat_civil = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas4_Etat_civil = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
    confidence_cas5_Etat_civil = models.PositiveIntegerField(
        max=100,
        step=5, widget=widgets.SliderWidget,
        label="Sur une échelle de 0 à 100%, avec quel degré de certitude donnez-vous cet âge "
              "(0 signifiant que vous n’êtes pas certain du tout et 100 signifie que vous êtes absolument certain?"
    )
















    # # Specific info level
    # postpicture_age = models.PositiveIntegerField()
    # postpicture_confidence_level = models.PositiveIntegerField()
    # postbones_age = models.PositiveIntegerField()
    # postbones_confidence_level = models.PositiveIntegerField()
    # postdocs_age = models.PositiveIntegerField()
    # postdocs_confidence_level = models.PositiveIntegerField()
    # postinterview_age = models.PositiveIntegerField()
    # postinterview_confidence_level = models.PositiveIntegerField()
    # # Complementary questions
    # question_nb_places_dispos = models.StringField(
    #     label="Concernant les informations que vous avez reçues au début, il était précisé que, dans le cadre de "
    #           "cette expérience, le nombre de places disponibles pour l’accueil d’un/des jeune(s) était :",
    #     choices=["Cela n'était pas précisé", "Une place", "Deux places", "Je ne sais pas"],
    #     widget=widgets.RadioSelect(),
    # )
    # # Data for identification questions
    # player_gender = models.StringField(label="Vous êtes:",
    #                             choices=["un homme", "une femme"],
    #                             widget=widgets.RadioSelectHorizontal())
    # player_age = models.PositiveIntegerField(label="Votre âge:",)
    #
    # def age_evolution_dumps(self, last_age):
    #     last_evolution = []
    #     if self.age_evolution is not None:
    #         last_evolution = json.loads(self.age_evolution)
    #     last_evolution.append(last_age)
    #     self.age_evolution = json.dumps(last_evolution)
    #
    # def age_evolution_loads(self):
    #     if self.age_evolution is not None:
    #         last_age = json.loads(self.age_evolution)
    #         return last_age.pop()
    #     else:
    #         return None
    #
    # def confidence_evolution_dumps(self, last_confidence):
    #     last_evolution = []
    #     if self.confidence_evolution is not None:
    #         last_evolution = json.loads(self.confidence_evolution)
    #     last_evolution.append(last_confidence)
    #     self.confidence_evolution = json.dumps(last_evolution)
    #
    # def confidence_evolution_loads(self):
    #     if self.confidence_evolution is not None:
    #         last_confidence = json.loads(self.confidence_evolution)
    #         return last_confidence.pop()
    #     else:
    #         return None
    #

from . import pages
