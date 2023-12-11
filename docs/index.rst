Welcome to LVMH-sephora documentation!
===================================
# API LVMH Sephora

L'API LVMH Sephora est une interface de programmation permettant d'interagir avec la base de données de Sephora, une société de produits de beauté et de parfumerie appartenant au groupe LVMH.

**Ici je tiens à souligner que cette base de données est avant tout fictive, car inventée par mes propres soins,
dans le cadre du cours de Base de Données Avancées que je dispense en Master 1 Data Engineer.**

l'objectif de ce cours était triple :

- Faire du postgreSQL en utilisant des mécanimses d'optimisations de requêtes et aborder la notion des extensions

- Mettre en place une api qui interagit avec cette base de données, dans le but d'emmener les étudiants à appréhender en profondeur la nécessité d'une bonne modélisation avec UML dans le respect des normes de l'industrie du génie logiciel

- Enfin, de mieux maîtriser les notions de roles, users et privilèges dans la manipulation d'une base de données ainsi que leurs impactes au sein d'une application

Pour notre API, nous avons utilisé :

- le patron de conception DAO
- le langage python
- 2 exemples de framework comme point d'accès : Flask (dont les routes sort reprises ci-dessous) et Fast (repris dans sa doc automatique)
- une base de données postgreSQL sur supabase
- connecté la bd supabase sur le client pgAdmin
- Et enfin nous avons généré une documentation grace à https://readthedocs.org/

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is well done.

Contents
--------

.. toctree::

   usage
   api
