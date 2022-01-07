from os import environ

SESSION_CONFIGS = [
    dict(
        name='FGES_Louvain',
        display_name="Efficacité collective, penser le groupe et son fonctionnement",
        num_demo_participants=3,
        app_sequence=['FGES_Louvain']
    ),
    dict(
        name='mineurs_age_v2',
        display_name="La prise en charge des jeunes non accompagnés",
        num_demo_participants=3,
        app_sequence=['mineurs_age_v2']
    ),
    dict(
       name='voiture',
       display_name="Décisions de la voiture autonome",
       num_demo_participants=3,
       app_sequence=['voiture']
    ),
    dict(
       name='groupes_minimaux_labo',
       display_name="Les groupes et leurs relations",
       num_demo_participants=3,
       representation_or_imputation="representation",
       app_sequence=['groupes_minimaux_labo']
    ),
    dict(
        name='com_serielle',
        display_name="Rumeurs et infoxs",
        num_demo_participants=7,
        app_sequence=['com_serielle']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1495337653867'
