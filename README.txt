Il s'agit d'une plateforme num�rique pour coordonner les comp�titions deadlifting, strongman en Am�rique du Nord et en Australie ! 
et qui permet a certains clubs de reserver des places dans ces comp�titions,  apr�s avoir recu le mail de monsieur Sayf Bejaoui nous avons commencer 
a corriger les bugs qui fesait planter la web app et avons mis en place une s�rie de test et un rapport de couverture achev�s ainsi qu'un rapport de performance 


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
Le rapport de couverture peut �tre g�n�r� en tapant:
# importer coverage
pip install coverage
# generer rapport coverage
## se placer � la racine du projet (au niveau de votre main)
coverage run -m pytest
# generer une page html � partir du rapport
coverage html
Les tests de performance sont effectu�s avec locust.
 L'interface locust pour les tests peut �tre appel�e en tapant :
locust -f tests/locust_test --host http://127.0.0.1:5000/ --users 1 --spawn-rate 1
Rendez-vous dans votre navigateur web � l'url : http://localhost:8089







 