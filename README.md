# sentiment_analysis_project
Ceci est la description d'un projet d'analyse des sentiments des utilisatuers twitter;
Son objectif est d'extraire des données de twitter à l'AOI Rest, de les restructurer et les traiter afin d'analyser le sentiment des utilisateurs à partir d'un calcul de score de chaque tweet de cet utilisateur.

Ce projet contient des fichiers de codes python , des fichiers  de données et des fichiers  resultats

Les fichiers code:
twwet-sentiment.py: C'est le code python qui permet de restructurer les données brutes  afin d'y chercher les termes d'analyse dans le fichier AFINN-111.txt et de calculer leur score pour une évaluation des sentiments des utilisateurs twitter.

twitterstream.py : Ceci est le code qui permet le chargement des données en live d'un utlisateur twitter donné

AFINN-DICTIONARY.PY: code de restructuration du fichier AFINN-111.txt sous format de dictionnaire python

les fichiers de données:
AFINN-111.txt: termes d'analyse
output.txt : données utilisateur (identifiant, historique, messages textes...)

Les fichers résultats:
afinn-out.json (résultat de AFINN-DICTIONARY.PY):

terms.txt: (Résultat 1 de twwet-sentiment.py):
Contient tous les termes de AFINN-111 retrouvés dans les messages textes de l'utilisateur dans output.txt 

scores.txt (Résultat 2 de twwet-sentiment.py):
Contient les scores des termes du fichier terms.txt

totalscores.txt: (Résultat 3 de twwet-sentiment.py):
Contient le total du score calculé pour chaque utlistaeur
