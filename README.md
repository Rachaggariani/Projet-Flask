Ce projet est divisé en trois parties, chacune abordant la gestion des formulaires de manière différente.
Pour faire fonctionner ce projet Flask, veuillez suivre les étapes suivantes :
Créer un environnement virtuel Exécutez la commande suivante pour créer un environnement virtuel Python : python -m venv monenv
Activer l'environnement virtuel Une fois l'environnement créé, activez-le avec la commande suivante : .monenv\Scripts\activate
Installer : pip install -r requirements.txt
Installer les bibliothèques nécessaires Installez les dépendances du projet en exécutant les commandes suivantes : pip install Flask pip install flask_migrate pip install passlib pip install jinja2 pip install flask-bootstrap pip install bcrypt pip install flask-restful pip install flask_wtf 
Remarque : -Si l'une des bibliothèques rencontre un problème d'installation, essayez d'abord de la désinstaller puis de la réinstaller :
pip uninstall monenv python -m venv monenvapp3

-Si vous rencontrez une erreur de permission lors de l'installation de la bibliothèque " pip install flask-bootstrap ", suivez les étapes ci-dessous :

Purgez le cache de pip avec la commande : pip cache purge
Ensuite, réinstallez la bibliothèque en spécifiant le répertoire du cache : pip install Flask-Bootstrap --cache-dir <chemin_vers_votre_répertoire_de_cache-flask_bootstrap> -Si vous rencontrez une erreur lors du l'installation de ce fihcier requirements.txt tu peut installer le contenu de ce fichier un par un : pip install flask-SqlAlchemy pip install flask-Migrate pip install flask-pymysql pip install passlib
Pour démarrer le projet, utilisez l'une des commandes suivantes : flask run ou bien app.py
