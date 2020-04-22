from flask import Flask, render_template, url_for, request
# render_template : pour l'affichage des pages HTML contenant des parametres {{}}
# url_for : pour générer l'URL de retour de la page 'page_1.html' vers la racine du site
# request : pour la récupération des paramètres passés par l'URL https://begin.pythonanywhere.com/next?
app = Flask(__name__)
# retrait du mode debug quand le programme est au point
# app.config["DEBUG"] = True

# _______________________ page d'acceuil _____________________________________________________
# @app.route() : "décorateur" de la fonction hello()
# designe la fonction lançée lorsque l'URL de la racine du site "/" est appellée
# dans notre cas il s'agit de "https://begin.pythonanywhere.com/" et de la fonction hello()
@app.route("/")
def hello():
    # necessaire pour que fonction2nd ne soit pas perdu après l'execution de hello()
    # (en l'absence d'une reconstruction après le choix de la fonction à afficher)
    global fonction2nd
    fonction2nd = 'f(x) = ax² + bx +c'
    # render_template() : affichage de la page HTML "home.html" qui contient des variables et instructions Flask
    # c'est ce qui est appellé de "...l'HTML altéré..." à cause de la présence des variables
    # toutes les pages .html doivent se situer dans un répertoire nommé /templates
    return render_template("home.html", dossier = "ISN - La Source - Ts 2019", eleve = "Arnaud Bacle - Inès Drulang", fonction2nd=fonction2nd)

# _______________________ page d'affichage courbe ________________________________________
# @app.route() : "décorateur" de la fonction suite()
# designe la fonction lançée lorsque l'URL de la racine du site suivie de /next est appellée
# dans notre cas il s'agit de "https://begin.pythonanywhere.com/next" et de la foction suite()
@app.route("/next")
def suite():
    # recuperation des valeurs des constantes a,b et c passées en argument de l'URL généré par la page d'acceuil
    cst_a = request.args.get('cst_a', None)
    cst_b = request.args.get('cst_b', None)
    cst_c = request.args.get('cst_c', None)
    #  calcul des valeurs [x] et [f(x)] de la courbe : a faire en fonction des constantes récupéres
    #  les contantes sont saisies en texte : float() permet de les convertir en nombres
    #  pour l'instant l'utilisateur ne peut rentrer ces valeurs, donc 2 courbes sont proposées sur lapage d'acceuil
    #   --- en attente de collaboration ----
    #   devrait être remplacé par un programme python qui calcul les meilleurs valeurs x pourque f(x) soit lisible sur le graphe
    #   ce programme devrait aussi construire "fonction2nd" correctement en texte en fonction des constantes
    #   en particulier pour éviter l'affichage de "f(x) = -3x² + -2x + 10"
    if float(cst_c) == -10:
        axe_Y = [-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
        axe_X = [160,  125,  94,  67,  44,  25,  10,  -1,  -8,  -11,  -10,  -5,  4,  17,  34,  55,  80,  109,  142,  179,  220]

    if float(cst_c) == 10:
        axe_Y = [-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
        axe_X = [-270,  -215,  -166,  -123,  -86,  -55,  -30,  -11,  2,  9,  10,  5,  -6,  -23,  -46,  -75,  -110,  -151,  -198,  -251,  -310]
    # render_template() : même remarque que pour la page d'acceuil
    return render_template('page_1.html', values=axe_X, labels=axe_Y, fonction2nd=fonction2nd, cst_a=cst_a,cst_b=cst_b,cst_c=cst_c)

# _________________________ lancement de l'application ______________________________________
if __name__ == '__main__':
    app.run()
