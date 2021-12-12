Il s'agit d'une plateforme numérique pour coordonner les compétitions deadlifting, strongman en Amérique du Nord et en Australie ! 
et qui permet a certains clubs de reserver des places dans ces compétitions,  aprés avoir recu le mail de monsieur Sayf Bejaoui nous avons commencer 
a corriger les bugs qui fesait planter la web app et avons mis en place une série de test et un rapport de couverture achevés ainsi qu'un rapport de performance 


Installation
nous avons utiliser les technologies suivantes:
Python v3.8+
locust 
pytest 
flask 
Installation:
1-ouvrir le dossier dans visual studio 
2-pip freeze > requirements.txt
3-pour lancer la web app : python server.py 
commande pour lancer les tests: pytest tests\test_app.py
Le rapport de couverture peut être généré en tapant:
# importer coverage
pip install coverage
# generer rapport coverage
## se placer à la racine du projet (au niveau de votre main)
coverage run -m pytest
# generer une page html à partir du rapport
coverage html
Les tests de performance sont effectués avec locust.
 L'interface locust pour les tests peut être appelée en tapant :
locust -f tests/locust_test --host http://127.0.0.1:5000/ --users 1 --spawn-rate 1
Rendez-vous dans votre navigateur web à l'url : http://localhost:8089







 