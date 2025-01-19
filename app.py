"""Concept
1. Fonctionnalités de base :
Création de compte utilisateur : Permettre aux utilisateurs de s'inscrire et de se connecter.
Profils utilisateurs : Chaque utilisateur a un profil avec des informations personnelles, une photo de profil, et une biographie.
Ajout d'amis : Les utilisateurs peuvent envoyer des demandes d'amis et accepter ou refuser celles des autres.
Fil d'actualités : Un fil d'actualités où les utilisateurs peuvent voir les mises à jour de leurs amis (publications, photos, etc.).
Publications : Les utilisateurs peuvent publier des textes, des images ou des vidéos.
Commentaires et likes : Les utilisateurs peuvent commenter et aimer les publications des autres.
2. Fonctionnalités avancées :
Messagerie privée : Permettre aux utilisateurs d'envoyer des messages directs.
Groupes : Créer des groupes où les utilisateurs peuvent discuter autour de centres d'intérêt communs.
Événements : Permettre aux utilisateurs de créer et de gérer des événements.
Notifications : Alerter les utilisateurs des nouvelles interactions (likes, commentaires, demandes d'amis).
Comment y arriver
Choix de la technologie :
Backend : Utilise un framework comme Flask ou Django pour gérer le serveur et les requêtes.
Frontend : Utilise HTML, CSS et JavaScript (ou un framework comme React ou Vue.js) pour créer l'interface utilisateur.
Base de données : Utilise une base de données comme SQLite, PostgreSQL ou MongoDB pour stocker les données des utilisateurs et des publications.
2. Architecture de l'application :
Modèle de données : Crée des modèles pour les utilisateurs, les publications, les amis, les commentaires, etc.
API REST : Développe une API pour gérer les interactions entre le frontend et le backend.
3. Développement étape par étape :
Phase 1 : Commence par la création de comptes utilisateurs et la gestion des profils.
Phase 2 : Ajoute la fonctionnalité d'ajout d'amis et de fil d'actualités.
Phase 3 : Implémente les publications, les commentaires et les likes.
Phase 4 : Ajoute des fonctionnalités avancées comme la messagerie et les groupes.
4. Tests et déploiement :
Tests : Écris des tests pour vérifier que chaque fonctionnalité fonctionne correctement.
Déploiement : Utilise des services comme Heroku ou AWS pour déployer ton application en ligne.
Améliorations futures :
Sécurité : Implémente des mesures de sécurité pour protéger les données des utilisateurs.
Scalabilité : Prépare ton application à gérer un grand nombre d'utilisateurs et de données."""


from flask import Flask, request, render_template, redirect, url_for
import os 

app = Flask(__name__)

usernamesok = ["gabriel"]
mdpok = ["GABRIEL;30400"]
chemin_fichier = "/Users/gabrieljeanvermeille/venv/bin/Vilar_reseau/usernames.txt"
chemin_fichier2 = "/Users/gabrieljeanvermeille/venv/bin/Vilar_reseau/mdp.txt"
user_data = {"gabriel": "GABRIEL;30400"}  # Utilisation d'un dictionnaire pour stocker les utilisateurs et leurs mots de passe


@app.route('/')
def principale():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global chemin_fichier
    global chemin_fichier2
    global usernamesok
    global inlycee
    global password
    global new_password
    global user_data

    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new-password')
        username = request.form.get('username')
        inlycee = request.form.get('in_lycée')
        password = request.form.get('mot-de-passe')

        # Ajoutez un message de débogage pour afficher tous les champs
        print(f'new_username: {new_username}, new_password: {new_password}, username: {username}, inlycee: {inlycee}, password: {password}')

        if inlycee == "C":
            if new_username and new_password:  # Vérifiez si un nouveau nom d'utilisateur et un mot de passe sont fournis
                user_data[new_username] = new_password  # Ajoutez le nouvel utilisateur au dictionnaire
                print(f'Nouvel utilisateur ajouté : {new_username}')
                
                with open(chemin_fichier, 'a') as fichier:
                    fichier.write(new_username + '\n')  
                        
                with open(chemin_fichier2, 'a') as fichier:
                    fichier.write(new_password + '\n')  # Écrire le mot de passe au lieu du nom d'utilisateur

        if username in user_data:  # Vérifiez si l'utilisateur existe dans le dictionnaire
            print('ok ça va')
            print(f'Mot de passe entré : {password}')  # Affiche le mot de passe entré pour le débogage
            print(f'Mot de passe attendu : {user_data[username]}')  # Affiche le mot de passe attendu pour le débogage
            if password == user_data[username]:  # Vérifiez si le mot de passe correspond
                print('c bon')
                return redirect(url_for('home', username=username))
            else:
                return render_template("login.html", error="Mauvais mot de passe !")
        else:
            return render_template("login.html", error="Mauvais nom d'utilisateur !")

    return render_template('login.html')  # Assurez-vous de retourner le modèle pour les requêtes GET

@app.route('/home') 

def home():
    username = request.args.get('username')
    return render_template('home.html', username=username)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')

