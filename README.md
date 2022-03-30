# Description du projet

Ce projet Github est un composant de la plate-forme pédagogique réalisée dans le cadre du projet Ephemer (https://lillethics.com/projet-ephemer/). Cette plate-forme est constituée de 3 composants conçus pour fonctionner ensemble :

- une app Django pour le frontend : `https://github.com/io-craft-org/ephemer`
- un oTree project pour le backend : c'est ce projet !
- un moteur oTree modifié : `https://github.com/io-craft-org/otree-core`


# Déploiement en production

Les grandes étapes du déploiement et les variables de configuration. Cette application est un oTree project classique ayant une dépendance sur un package `otree-core` modifié pour la plate-forme Ephemer.

Pour plus d'infos :

- la doc de oTree : https://otree.readthedocs.io/en/latest/
- en particulier le déploiement sur Ubuntu : https://otree.readthedocs.io/en/latest/server/ubuntu.html


## Environnement nécessaire

- Python 3.9 (contrainte du serveur oTree 5.4, on a remarqué une incompatibilité avec Python 3.10)
- postgresql


## Installation depuis Github

```bash
$ git clone https://github.com/io-craft-org/ephemer-otree.git
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install requirements.txt
```

Installer le package `psycopg2` nécessite des outils de compilation sur l'host. Alternativement on peut tenter de le remplacer par le package `psycopg2-binary`.


## Configuration et démarrage

En ayant le virtualenv activé.

La configuration se fait par des variables d'environnement. L'environnement de production nécessite les variables suivantes :

```bash
$ export OTREE_PRODUCTION=1
$ export OTREE_AUTH_LEVEL=STUDY
$ export OTREE_ADMIN_PASSWORD=<le mot de passe admin>  # Devrait être communiqué au responsable métier de la plate-forme
$ export OTREE_REST_KEY=<une clé secrète>  # La variable `settings.OTREE_REST_KEY` du front Django devra avoir cette même valeur
$ export DATABASE_URL=postgres://<user>:<password>@<hostname>/<database>
```

```bash
$ otree prodserver <server port>
```
