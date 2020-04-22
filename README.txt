Projet:
Graphe d'une fonction du second degré
réalisé sur un site web dynamique, hébergeur PythonanyWhere

Chaque contributeur développe sur son compte PythonanyWhere
puis git "push" sur Github.

Enfin, le contenu du site est rechargé sur le site central,
résultat des sites PythonAnyWhere de developpement.

grapheur_v3

grapheur_v3 avec passage de variables par URL.

C'est à dire : Abandon des formulaires pour la sasie des constantes a, b et c :
il faudrait utiliser un module de Flask dédié " Flask-WTF " qui résoud tous les problèmes :
"Using Flask-WTF in your app makes it so much easier to handle forms in Flask.
Instead of manually handling everything... "

Le choix est fait de transmettre les constantes via l'URL qui relie la page d'acceuil à la page qui dessine.
Il y a 2 choix :
f(x) = 3x² + 2x -10
ou bien
f(x) = -3x² -2x +10

qui génèrent les 2 URL de la page dessin (page_1.html) avec les constantes :
https://begin.pythonanywhere.com/next?cst_a=3&cst_b=2&cst_c=-10
https://begin.pythonanywhere.com/next?cst_a=-3&cst_b=-2&cst_c=10

pour la version 3 l'adresse est : https://begin.pythonanywhere.com/