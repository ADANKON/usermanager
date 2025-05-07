# User Manager (Django)

Plateforme d’apprentissage de l’authentification avec Django.

## Fonctionnalités prévues
- Connexion, déconnexion, inscription
- Gestion des utilisateurs
- Système de rôles (admin, manager, utilisateur)
- Permissions personnalisées
- Backend d’authentification customisé

## Installation

```bash
git clone https://github.com/<ton_nom>/usermanager.git
cd usermanager
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
