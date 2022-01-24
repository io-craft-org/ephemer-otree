from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time





class wait_allplayers(WaitPage):
    wait_for_all_groups = True
    body_text = "Salle d'attente : veuillez patienter, nous attendons que tous les joueurs arrivent."


# ETES VOUS UN ROBOT ???
class P0_IDENTITE_SUJ(Page):
    timeout_seconds  = Constants.delai_page

    form_model = 'player'
    form_fields = ['IS_NOT_A_BOT']

    def is_displayed(self):
        return self.round_number == 1


class P1_ROLE(Page):
    def vars_for_template(self):
        self.player.group_name_individu()
        self.player.timeout_for_bots()
        self.player.bot_or_pas_bot_all_game()       

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()



class P2_TX_IMPOT(Page):
    form_model = 'player'
    form_fields = ['A_TX_IMPOT', 'A_TX_REDISTRIB']

    def before_next_page(self):
        self.player.bot_or_pas_bot_tx_impot()
        self.group.taxation()

    def is_displayed(self):
        return self.player.ROLE == 'A'

    def vars_for_template(self):
        self.player.timeout_for_bots()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()




class A_B_and_C_Wait_for_A(WaitPage):
    wait_for_all_groups = True
    body_text = "Salle d'attente : Attendez que les joueurs A aient décidé du taux d'imposition entre 0% et 50% et du taux de redistribution entre 0% et 100%"

 


class B_CAN_CHANGE(Page):
    form_model = 'player'
    form_fields = ['B_CHOOSE_GROUPE']

    def before_next_page(self):
        self.player.bot_or_pas_bot_choose_groupe()
        self.player.group_name_after_choice_B()
        

    def is_displayed(self):
        return self.player.ROLE == 'B'

    def vars_for_template(self):
        self.player.timeout_for_bots()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()

    


class GROUPING(WaitPage):
    wait_for_all_groups = True
    body_text = "Salle d'attente : Attendez que les joueurs B aient décidé du groupe dans lequel ils souhaitent se rendre."

    after_all_players_arrive = 'grouping_after_choose_groupe'  




class P3_DECLARATION(Page):
    form_model = 'player'
    form_fields = ['DECLARATION']

    def is_displayed(self):
        return self.player.ROLE != 'A'

    def vars_for_template(self):
        self.player.timeout_for_bots()

    def before_next_page(self):
        self.player.bot_or_pas_bot_declaration()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()





class WaitComputeDeclare(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'collectImpot'  
    body_text = "Salle d'attente : Attendez que les joueurs aient terminé de déclarer leur revenu"









class Results(Page):
    def vars_for_template(self):
        self.player.timeout_for_bots()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()


class transition(Page):
    def before_next_page(self):
        self.player.remuneration()

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.timeout_for_bots()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()



class Results_Final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.timeout_for_bots()

    def get_timeout_seconds(self):    
        return self.participant.vars['my_page_timeout_seconds'] - time.time()


page_sequence = [
                wait_allplayers,
                P0_IDENTITE_SUJ,
                P1_ROLE, 
                P2_TX_IMPOT,
                A_B_and_C_Wait_for_A,
                B_CAN_CHANGE,
                GROUPING,
                P3_DECLARATION,
                WaitComputeDeclare, 
                Results,
                transition,
                Results_Final
                ]
