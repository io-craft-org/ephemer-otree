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
import itertools
import time


author = 'Vincent Lenglin'

doc = """
    evasion fiscale Biden treatment
"""


#############################################################################################
#############################################################################################
    # -----------------------------------------------------------------------
    # CONSTANTE
    # -----------------------------------------------------------------------
#############################################################################################
#############################################################################################

class Constants(BaseConstants):
    name_in_url = 'evasion_FINAL_BIDEN'
    players_per_group = 3
    num_rounds = 3

    delai_page = 3000
    timeout_bot = 1
    timeout_humain = 5000

    show_up = 5

    rolage= ['A', 'B', 'C']

    nom_groupe = [ 'bleu', 'jaune', 'orange' , 'rouge', 'vert', 'noir', 'blanc']

    min_income = 175
    max_income = 525

    multiplier = 1.7
    max_tx_impot = 50
    min_tx_impot = 0

    seuil_bankrupt = 100

    penalty_multiplier = 3

    nb_round_remunerate = 3

    SEUIL_BIDEN = 15

    taux_de_change = 150


# variables à changer en fonction du nombre de personnes dans un groupe au début de l'expérience
    numb_of_players_non_B = 2

    numb_of_player_C_per_group = 1

    numb_of_player_B_per_group = 1





#############################################################################################
#############################################################################################
    # -----------------------------------------------------------------------
    # SUBSESSION
    # -----------------------------------------------------------------------
#############################################################################################
#############################################################################################
class Subsession(BaseSubsession):
    def creating_session(self):

        group_iter = itertools.cycle(Constants.nom_groupe)


        # ATTRIBUTION DES ROLES + REVENU INITIAL + GROUPE D'ORIGINE + TX IMPOT + DECLARATION
        role_iter = itertools.cycle(Constants.rolage)
        players = [p for p in self.get_players()]

        for p in self.get_players():
            p.ROLE = next(role_iter)
            p.GROUP_ORIGIN = p.group.id_in_subsession
            
            p.NUMBER_OF_GROUPS = int(len(players)/Constants.players_per_group)
            p.ROUNDED_PENALTY = 0
            p.MONTANT_IMPOT_BIDEN = 0

            p.participant.vars['REVENU_FINAL_3_TOURS'] = []
            p.TOTAL_NUMBER_OF_PLAYER_B = Constants.numb_of_player_B_per_group * p.NUMBER_OF_GROUPS

            if p.ROLE != 'A':
                p.A_TX_IMPOT = 0
                p.A_TX_REDISTRIB = 0
                p.A_REMUNERATE = 0
                p.participant.vars['REVENU_INITIAL'] = [random.randint(Constants.min_income, Constants.max_income) for i in range(Constants.num_rounds)]
                

            elif p.ROLE == 'A':
                p.REVENU_INITIAL = 0
                p.DECLARATION = 0
                p.MONTANT_IMPOT = 0
                

            if p.ROLE != 'B':
                p.B_CHOOSE_GROUPE = p.GROUP_ORIGIN


            for s in range(1, Constants.num_rounds + 1):
                if p.ROLE != 'A':
                    p.in_round(s).REVENU_INITIAL = p.participant.vars['REVENU_INITIAL'][s-1]







 #########################################################################################
    # SET PAYOFFS

    # ON APPLQUE LE TAUX D'IMPOSITION DECIDE PAR A AUX DECLARATION DES JOUEURS ET ON CALCUL LA COLLECT TOTAL DES IMPOTS
    def collectImpot(self):
        players = self.get_players()
        groups = self.get_groups()

        

        for p in players:
            p.TX_NOW = p.group.TX_IMPOSITION
            p.TX_REDISTRIBUTION_NOW = p.group.TX_REDISTRIBUTION

            if p.ROLE != 'A':
                p.MONTANT_IMPOT = round(p.DECLARATION * (p.TX_NOW / 100), 1)


        ### TAUX MONTANT BIDEN
        #######################################################
            # SI LES DEUX PAYS SONT EN DESSOUS DU SEUIL
            if p.ROLE == "B":
                if p.TX_NOW < Constants.SEUIL_BIDEN and p.TX_ORIGIN < Constants.SEUIL_BIDEN :
                    if p.TX_NOW > p.TX_ORIGIN :
                        p.TX_IMPOT_BIDEN = 0
                        p.HAVE_TO_PAY_BIDEN = 0

                    elif p.TX_NOW < p.TX_ORIGIN :
                        p.TX_IMPOT_BIDEN = 0
                        p.HAVE_TO_PAY_BIDEN = 0

                    else:
                        p.TX_IMPOT_BIDEN = 0
                        p.HAVE_TO_PAY_BIDEN = 0


            # SI UNIQUEMENT LE PAYS D'ACCEUIL EST EN DESSOUS DU SEUIL
                elif p.TX_NOW < Constants.SEUIL_BIDEN and p.TX_ORIGIN > Constants.SEUIL_BIDEN :
                    if p.TX_NOW < p.TX_ORIGIN :
                        p.TX_IMPOT_BIDEN = p.TX_ORIGIN  - p.TX_NOW
                        p.HAVE_TO_PAY_BIDEN = 1
                    else:
                        p.TX_IMPOT_BIDEN = 0
                        p.HAVE_TO_PAY_BIDEN = 0

            # DANS TOUS LES AUTRES CAS
                else:
                    p.TX_IMPOT_BIDEN = 0
                    p.HAVE_TO_PAY_BIDEN = 0

            else:
                p.TX_IMPOT_BIDEN = 0

            if p.ROLE == 'B':
                 p.MONTANT_IMPOT_BIDEN = round(p.DECLARATION * ((p.TX_IMPOT_BIDEN ) / 100), 1)


        

       


    # CREATION DES LISTES POUR ENSUITE ENVOYER LES BONNES DONNEES DANS LES GROUPES
        # DECLARATION SOMME 
        LIST_DECLARATION = [p.DECLARATION for p in players]
        LIST_GROUP = [p.B_CHOOSE_GROUPE for p in players]
        zipDeclarationGroup = zip(LIST_DECLARATION, LIST_GROUP )

        listDeclarationGroup = list(zipDeclarationGroup)
        vecDeclaration = [[i for i, element in listDeclarationGroup if element == j] for j in range(1, max(LIST_GROUP) + 1  )]

        # TOTAL COLLECT IMPOT SOMME
        LIST_MONTANT_IMPOT= [p.MONTANT_IMPOT for p in players]
        zipTotalCollectnGroup = zip(LIST_MONTANT_IMPOT, LIST_GROUP )

        listTotalCollectnGroup = list(zipTotalCollectnGroup)
        vecTotalCollect = [[i for i, element in listTotalCollectnGroup if element == j] for j in range(1, max(LIST_GROUP) + 1 )]

        # TOTAL COLLECT IMPOT BIDEN
        LIST_GROUP_ORIGINE = [p.GROUP_ORIGIN for p in players]
        LIST_MONTANT_IMPOT_BIDEN = [p.MONTANT_IMPOT_BIDEN for p in players]
        zipTotalCollectBidenGroup = zip(LIST_MONTANT_IMPOT_BIDEN, LIST_GROUP_ORIGINE )

        listTotalCollectBidenGroup = list(zipTotalCollectBidenGroup)
        vecTotalCollectBiden = [[i for i, element in listTotalCollectBidenGroup if element == j] for j in range(1, max(LIST_GROUP) + 1 )]


    # ENVOIE DES INFORMATIONS DANS LE BON GROUPE : l'envoie des impots est indexé sur le B_CHOOSE_GROUPE
        for p in self.get_players():
            for g in groups:
                g.TOTAL_DECLARATION = sum(vecDeclaration[g.id_in_subsession - 1])
                g.TOTAL_COLLECT = int(round(sum(vecTotalCollect[g.id_in_subsession - 1]), 1))
                g.TOTAL_COLLECT_BIDEN = int(round(sum(vecTotalCollectBiden[g.id_in_subsession - 1]), 1))
                g.TOTAL_COLLECT_WITH_BIDEN = g.TOTAL_COLLECT + g.TOTAL_COLLECT_BIDEN
                g.TOTAL_COLLECT_MULTIPLIER = int(round(g.TOTAL_COLLECT_WITH_BIDEN * Constants.multiplier))
                g.NUMB_PLAYER_PER_GROUP = len(vecDeclaration[g.id_in_subsession - 1])
                g.NB_PLAYERS_WITHOUT_A = g.NUMB_PLAYER_PER_GROUP - 1
        


        # DETERMINATION DES GAINS POUR B ET C + CONTROL AUDIT
        for p in self.get_players():
            for g in groups:

                if p.ROLE != 'A':
                    p.MONTANT_IMPOT_THEORIQUE = round(p.REVENU_INITIAL * (p.TX_NOW / 100), 1)
                    p.DIFF_REEL_VS_FRAUDE = round(p.MONTANT_IMPOT_THEORIQUE - p.MONTANT_IMPOT, 1)

                    # FRAUDE  OR NOT FRAUDE ?
                    if p.REVENU_INITIAL > p.DECLARATION:
                        p.FRAUDE = 1
                    else:
                        p.FRAUDE = 0

                    # CONTROLE AUDIT OR NOT AUDIT 
                    p.CONTROL = random.choices([0, 1], weights=[0, 1])[0]

                    if p.CONTROL == 0:
                        p.REVENU_APRES_IMPOT = int(round(p.REVENU_INITIAL - p.MONTANT_IMPOT - p.MONTANT_IMPOT_BIDEN))

                    elif p.CONTROL == 1:
                        if p.REVENU_INITIAL > p.DECLARATION:
                            p.PENALTY = round((Constants.penalty_multiplier * p.DIFF_REEL_VS_FRAUDE), 1)
                            p.ROUNDED_PENALTY = int(round(p.PENALTY))
                            p.REVENU_APRES_IMPOT = int(round(p.REVENU_INITIAL - p.MONTANT_IMPOT - p.MONTANT_IMPOT_BIDEN - p.ROUNDED_PENALTY))
                        else:
                            p.PENALTY = 0
                            p.ROUNDED_PENALTY = 0
                            p.REVENU_APRES_IMPOT = int(round(p.REVENU_INITIAL - p.MONTANT_IMPOT - p.MONTANT_IMPOT_BIDEN ))

                elif p.ROLE == 'A':
                    pass



        # TOTAL COLLECT IMPOT SOMME
        LIST_TOTAL_PENALTY= [p.ROUNDED_PENALTY for p in players]
        zipTotalPenaltyGroup = zip(LIST_TOTAL_PENALTY, LIST_GROUP )

        listTotalPenaltyGroup = list(zipTotalPenaltyGroup)
        vecTotalPenalty = [[i for i, element in listTotalPenaltyGroup if element == j] for j in range(1, max(LIST_GROUP) + 1 )]    

        for p in self.get_players():
            for g in groups:    
                g.TOTAL_PENALTY = sum(vecTotalPenalty[g.id_in_subsession - 1])
                
                

        # MONTANT A PARTAGER APRES REMUNERATION DE A - REVENU FINAL DE A
        for p in self.get_players():
            for g in groups:
                if p.ROLE == 'A':
                    p.A_TX_POUR_SOI = 100 - p.group.TX_REDISTRIBUTION
                    g.A_REMUNERATION = int(round(g.TOTAL_COLLECT_MULTIPLIER * (1-(g.TX_REDISTRIBUTION/100))))
                    g.TOTAL_MONTANT_A_PARTAGER = int(round(g.TOTAL_COLLECT_MULTIPLIER - g.A_REMUNERATION))
                    g.MONTANT_A_PARTAGER = int(round(g.TOTAL_MONTANT_A_PARTAGER / (g.NUMB_PLAYER_PER_GROUP - 1)))
                    p.REVENU_FINAL = int(p.group.A_REMUNERATION)

                else:
                    pass

        # REVENU FINAL DE B ET C
        for p in self.get_players():
            for g in groups:
                if p.ROLE !='A':
                    p.REVENU_FINAL = int(round(p.REVENU_APRES_IMPOT + g.MONTANT_A_PARTAGER))






    # ----------------------------------------------------------------------------------
    # MATRICES DES GROUPES EN FONCTION DES CHOIX DES JOUEURS C
    # ----------------------------------------------------------------------------------
    def grouping_after_choose_groupe(self): 
        vec_id_joueur = []   
        players = []     
        MAX_GROUPE = []   
        vec_choose_groupe = []
        new_structure = []
        players = [p for p in self.get_players()]
        groups = [g for g in self.get_groups()]
     
        MAX_GROUPE = int(len(players) / Constants.players_per_group)
        
        vec_choose_groupe = [p.B_CHOOSE_GROUPE for p in players]
        vec_id_joueur = [[index + 1 for index, element in enumerate(vec_choose_groupe) if element == i] for i in range(1, MAX_GROUPE + 1 )]
        new_structure = vec_id_joueur
        

        self.set_group_matrix(new_structure)


        for p in self.get_players():
            p.group.NUMB_PLAYER_PER_GROUP_AFTER_CHOICE_B = len(new_structure[p.group.id_in_subsession - 1])
            p.group.NUMB_B_PLAYER_PER_AFTER_CHOICE_B = p.group.NUMB_PLAYER_PER_GROUP_AFTER_CHOICE_B - Constants.numb_of_players_non_B
            
                
                


        # application de la structure du groupe au round T jusqu'au round T+n
        #for subsession in self.in_rounds(self.round_number, Constants.num_rounds):
        #    subsession.group_like_round(self.round_number)


        players = self.get_players()

        for p in players:
            if p.ROLE == 'A':
                p.group.TX_IMPOSITION = p.A_TX_IMPOT
                p.group.TX_REDISTRIBUTION = p.A_TX_REDISTRIB
                p.group.A_TX_POUR_SOI_GPE = 100 - p.A_TX_REDISTRIB

                # BIDEN : est-ce que la taxe imposée par A est en dessous de 15%
                if p.group.TX_IMPOSITION <= Constants.SEUIL_BIDEN:
                    p.group.BIDEN_IS_BELOW_QUINZE = 1
                    p.group.DIFF_TX_IMPOT_BIDEN = Constants.SEUIL_BIDEN -  p.group.TX_IMPOSITION
                   
                else:
                    p.group.BIDEN_IS_BELOW_QUINZE = 0
                    p.group.DIFF_TX_IMPOT_BIDEN = 0

            else:
                
                pass

        for p in players:
            p.DIFF_TAUX = p.TX_ORIGIN - p.group.TX_IMPOSITION 

            

#############################################################################################
#############################################################################################
    # -----------------------------------------------------------------------
    # GROUPE
    # -----------------------------------------------------------------------
#############################################################################################
#############################################################################################
class Group(BaseGroup):
    GROUP_NAME_ORIGIN = models.StringField()

    NUMB_PLAYER_PER_GROUP_AFTER_CHOICE_B = models.IntegerField()
    NUMB_B_PLAYER_PER_AFTER_CHOICE_B = models.IntegerField()
    NUMB_PLAYER_PER_GROUP = models.IntegerField()
    NB_PLAYERS_WITHOUT_A = models.IntegerField()

    TX_IMPOSITION = models.IntegerField()
    TX_REDISTRIBUTION = models.IntegerField()
    A_TX_POUR_SOI_GPE =  models.IntegerField()

    TOTAL_DECLARATION = models.IntegerField()
    TOTAL_COLLECT = models.IntegerField()
    TOTAL_COLLECT_MULTIPLIER = models.IntegerField()

    TOTAL_PENALTY = models.IntegerField()
    BANQUEROUTE = models.IntegerField()
    
    TOTAL_MONTANT_A_PARTAGER = models.IntegerField()
    MONTANT_A_PARTAGER = models.IntegerField()
    A_REMUNERATION = models.IntegerField()

    # BIDEN VARIABLE
    BIDEN_IS_BELOW_QUINZE = models.IntegerField()
    DIFF_TX_IMPOT_BIDEN = models.FloatField()
    TOTAL_COLLECT_BIDEN = models.IntegerField()
    TOTAL_COLLECT_WITH_BIDEN = models.IntegerField()

   


    # ON REPAND LE TAUX D'IMPOSITION DECIDE PAR A AUX AUTRES JOUEURS DU GROUPE + APPLICATION BIDEN
    def taxation(self):
        players = self.get_players()

        for p in players:
            
            if p.ROLE == 'A':
                p.group.TX_IMPOSITION = p.A_TX_IMPOT
                p.group.TX_REDISTRIBUTION = p.A_TX_REDISTRIB
                p.group.A_TX_POUR_SOI_GPE = 100 - p.A_TX_REDISTRIB


                # BIDEN : est-ce que la taxe imposé par A est en dessous de 15 %
                if p.group.TX_IMPOSITION <= Constants.SEUIL_BIDEN:
                    p.group.BIDEN_IS_BELOW_QUINZE = 1
                   
                else:
                    p.group.BIDEN_IS_BELOW_QUINZE = 0
                     
            else:
                pass
            # TAUX D'IMPOSITION DU GROUPE D'ORIGINE QUI NE CHANGE PAS MËME LORSQU'ON REFORME LES GROUPES
            p.TX_ORIGIN = p.group.TX_IMPOSITION
            p.TX_REDISTRIB_ORIGIN = p.group.TX_REDISTRIBUTION

   

        
#############################################################################################
#############################################################################################
    # -----------------------------------------------------------------------
    # PLAYER
    # -----------------------------------------------------------------------
#############################################################################################
#############################################################################################

class Player(BasePlayer):

    IS_NOT_A_BOT = models.IntegerField(label='', blank = False)
    my_page_timeout_seconds = models.FloatField()

   
# CONSTANTES
    SHOW_UP = models.IntegerField(initial = Constants.show_up)
    MAX_INCOME = models.IntegerField(initial = Constants.max_income)
    MIN_INCOME = models.IntegerField(initial = Constants.min_income)
    MULTIPLIER = models.IntegerField(initial = Constants.multiplier)
    MAX_TX_IMPOT =  models.IntegerField(initial = Constants.max_tx_impot)
    MIN_TX_IMPOT = models.IntegerField(initial = Constants.min_tx_impot)
    PENALITY_MULTIPLIER = models.IntegerField(initial = Constants.penalty_multiplier)
    NB_ROUND_REMUNERATE = models.IntegerField(initial = Constants.nb_round_remunerate)
    SEUIL_TX_BIDEN = models.IntegerField(initial = Constants.SEUIL_BIDEN)
    TAUX_DE_CHANGE = models.IntegerField(initial = Constants.taux_de_change)
    

# TAXE ET INFO POUR BIDEN
    TX_ORIGIN = models.IntegerField()
    TX_NOW = models.IntegerField()
    TX_REDISTRIB_ORIGIN = models.IntegerField()
    TX_REDISTRIBUTION_NOW = models.IntegerField()

    DIFF_TAUX = models.IntegerField()

    HAVE_TO_PAY_BIDEN = models.IntegerField()
    TX_IMPOT_BIDEN = models.FloatField()

    

# ROLE
    ROLE = models.StringField()

# NOM DE GROUPE : ORIGIN + N + N-1
    GROUP_NAME_PARTICIPANT_ORIGIN = models.StringField()
    GROUP_NAME_PARTICIPANT = models.StringField()
    GROUP_NAME_PARTICIPANT_N_MOINS_UN = models.StringField()

# NUMERO DU GROUPE : ORIGIN + N + N-1
    GROUP_ORIGIN = models.IntegerField()
    GROUP_N_MOINS_UN = models.IntegerField(label='')
    B_CHOOSE_GROUPE = models.IntegerField(label='')

# NOMBRE DE PERSONNE DANS LE GROUPE AVANT ET APRES CHOIX B
    NUMBER_OF_GROUPS  = models.IntegerField()
    TOTAL_NUMBER_OF_PLAYER_B = models.IntegerField()
    NUMBER_OF_PLAYER_BEFORE_CHOICE_B = models.IntegerField(label='')
    NUMB_B_PLAYER_PER_BEFORE_CHOICE_B = models.IntegerField(label='')
    

# TAUX D'IMPOSITION + TAUX DE REDISTRIBUTION
    A_TX_IMPOT = models.IntegerField(label = "", blank = False, min = Constants.min_tx_impot, max = Constants.max_tx_impot)
    A_TX_REDISTRIB = models.IntegerField(label = "", blank = False, min = 0, max = 100)
    A_TX_POUR_SOI = models.IntegerField(label = "", blank = False, min = 0, max = 100)

# REVENU INITIAL + DECLARATION
    REVENU_INITIAL = models.IntegerField()
    DECLARATION = models.IntegerField(label = "", blank = False)

# MONTANT DE L'IMPOT (réel + théorique)
    MONTANT_IMPOT = models.FloatField()
    MONTANT_IMPOT_THEORIQUE = models.FloatField()
    MONTANT_IMPOT_BIDEN = models.FloatField()

# FRAUDE + MONTANT PENALITE
    DIFF_REEL_VS_FRAUDE = models.FloatField()
    FRAUDE = models.IntegerField()
    CONTROL = models.IntegerField()
    PENALTY = models.FloatField()
    ROUNDED_PENALTY = models.IntegerField()

# REVENU APRES IMPOT ET REVENU DE A
    REVENU_APRES_IMPOT = models.IntegerField()
    A_REMUNERATE = models.IntegerField(label = "", blank = False)
    REVENU_FINAL = models.IntegerField()

# PAIEMENT FINAL
    RAND_ESSAI = models.LongStringField()
    REVENU_FINAL_3_TOURS = models.LongStringField()
    SUM_REVENU_FINAL_3_TOURS = models.FloatField()
    PAIEMENT_EXPERIENCE = models.IntegerField()


    
    def group_name_after_choice_B(self):
        self.GROUP_NAME_PARTICIPANT = Constants.nom_groupe[self.B_CHOOSE_GROUPE - 1]



    def group_name_individu(self):
        
        self.GROUP_NAME_PARTICIPANT_ORIGIN = Constants.nom_groupe[self.GROUP_ORIGIN - 1]

        if self.round_number > 1 :
            self.GROUP_N_MOINS_UN = self.in_round(self.round_number - 1).B_CHOOSE_GROUPE

            self.GROUP_NAME_PARTICIPANT_N_MOINS_UN = self.in_round(self.round_number - 1).GROUP_NAME_PARTICIPANT
            self.GROUP_NAME_PARTICIPANT = Constants.nom_groupe[self.in_round(self.round_number - 1).B_CHOOSE_GROUPE - 1]
            self.NUMBER_OF_PLAYER_BEFORE_CHOICE_B = self.in_round(self.round_number - 1).group.NUMB_PLAYER_PER_GROUP
            self.NUMB_B_PLAYER_PER_BEFORE_CHOICE_B = self.NUMBER_OF_PLAYER_BEFORE_CHOICE_B - Constants.numb_of_players_non_B
            
        elif self.round_number == 1 :
            self.GROUP_NAME_PARTICIPANT = Constants.nom_groupe[self.GROUP_ORIGIN - 1]
        
            

        
    


  # ----------------------------------------------------------------------------------
    # MESSAGE D'ERREUR SI LE MEC RENTRE UN NOMBRE QUI N'EST PAS CONTENU DANS LE RANGE
  # ----------------------------------------------------------------------------------

    def A_TX_IMPOT_error_message(self, value): 
        if self.ROLE == 'A':    
            if value > Constants.max_tx_impot or value < 0:
                return 'Veuillez entrer un nombre entre' +  str(Constants.min_tx_impot) + 'et ' + str(Constants.max_tx_impot)


    def A_TX_REDISTRIB_error_message(self, value): 
        if self.ROLE == 'A':    
            if value > 100 or value < 0:
                return 'Veuillez entrer un nombre entre 0 ET 100'



    def DECLARATION_error_message(self, value):  
        if self.ROLE !='A':   
            if value > self.REVENU_INITIAL or value < 0:
                return 'Veuillez entrer un nombre entre 0 et ' + str(self.REVENU_INITIAL)


    def A_REMUNERATE_error_message(self, value):  
        if self.ROLE =='A':   
            if value > self.group.TOTAL_COLLECT_MULTIPLIER or value < 0:
                return 'Veuillez entrer un nombre entre 0 et ' + str(self.group.TOTAL_COLLECT_MULTIPLIER)



   # def B_CHOOSE_GROUPE_error_message(self, value):     
   #     if value > self.NUMBER_OF_GROUPS or value < 1:
   #         return 'Veuillez entrer un nombre entre 1 et ' + str(self.NUMBER_OF_GROUPS)



    # ----------------------------------------------------------------------------------
    # CODE DE REMUNERATION
    # ----------------------------------------------------------------------------------
    def remuneration(self):
        self.participant.vars['RAND_ESSAI'] = random.sample([i for i in range(1, Constants.num_rounds + 1)], k = Constants.nb_round_remunerate)

        self.RAND_ESSAI = str(self.participant.vars['RAND_ESSAI'])
        
        self.participant.vars['REVENU_FINAL_3_TOURS'] = [self.in_round(s).REVENU_FINAL for s in self.participant.vars['RAND_ESSAI']]

        self.REVENU_FINAL_3_TOURS = str(self.participant.vars['REVENU_FINAL_3_TOURS'])
        
    
        self.participant.vars['SUM_REVENU_FINAL_3_TOURS'] = int(round(sum(self.participant.vars['REVENU_FINAL_3_TOURS'])))

        self.SUM_REVENU_FINAL_3_TOURS = self.participant.vars['SUM_REVENU_FINAL_3_TOURS']

        self.PAIEMENT_EXPERIENCE = int(round(Constants.show_up + self.SUM_REVENU_FINAL_3_TOURS)/Constants.taux_de_change)




    # -----------------------------------------------------------------------
    # CODAGE DES BOTS POUR LES INPUTS
    # -----------------------------------------------------------------------

    # TIMEOUT DIFFERENT SI HUMAIN OU ROBOT
    def timeout_for_bots(self):
        if self.IS_NOT_A_BOT == 0:
            self.my_page_timeout_seconds = Constants.timeout_bot   
            self.participant.vars['my_page_timeout_seconds'] = time.time() + self.my_page_timeout_seconds 

        elif self.IS_NOT_A_BOT == 1:
            self.my_page_timeout_seconds = Constants.timeout_humain     
            self.participant.vars['my_page_timeout_seconds'] = time.time() + self.my_page_timeout_seconds


    def bot_or_pas_bot_all_game(self):
        if self.round_number == 1 :
            for i in range(1, Constants.num_rounds + 1):
                self.in_round(i).IS_NOT_A_BOT = self.in_round(1).IS_NOT_A_BOT
                self.in_round(i).my_page_timeout_seconds = self.in_round(1).my_page_timeout_seconds

    # DECLARATION IMPOT HUMAIN ET ROBOT
    def bot_or_pas_bot_declaration(self):
        if self.ROLE!='A':
            if self.IS_NOT_A_BOT == 0 :
                self.DECLARATION = random.randint(Constants.min_income, self.REVENU_INITIAL)
            elif self.IS_NOT_A_BOT == 1 and self.participant.vars['my_page_timeout_seconds'] - time.time() < 0:
                self.DECLARATION = random.randint(Constants.min_income, self.REVENU_INITIAL)
            else: 
                pass



    # TAUX D'IMPOSITION HUMAIN ET ROBOT
    def bot_or_pas_bot_tx_impot(self):
        if self.ROLE=='A' :
            if self.IS_NOT_A_BOT == 0 :
                self.A_TX_IMPOT = random.randint(0, Constants.max_tx_impot) 
                self.A_TX_REDISTRIB = random.randint(0, Constants.max_tx_impot) 
            elif self.IS_NOT_A_BOT == 1 and self.participant.vars['my_page_timeout_seconds'] - time.time() < 0:
                self.A_TX_IMPOT = random.randint(0, Constants.max_tx_impot) 
                self.A_TX_REDISTRIB = random.randint(0, Constants.max_tx_impot) 
            else: 
                pass


    # CHOIX GROUPE HUMAIN ET ROBOT
    def bot_or_pas_bot_choose_groupe(self):
        if self.ROLE=='B':
            if self.IS_NOT_A_BOT == 0 :
                self.B_CHOOSE_GROUPE = random.randint(1, self.NUMBER_OF_GROUPS) 
            elif self.IS_NOT_A_BOT == 1 and self.participant.vars['my_page_timeout_seconds'] - time.time() < 0:
                self.B_CHOOSE_GROUPE = random.randint(1, self.NUMBER_OF_GROUPS) 
            else: 
                pass
       
       
    