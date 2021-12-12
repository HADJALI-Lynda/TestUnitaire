import pytest
import json
from flask import template_rendered, url_for
from werkzeug import datastructures
import server
from server import loadClubs, loadCompetitions
app = server.create_app({"TESTING": True})
@pytest.fixture
def client():
    app = server.create_app({"TESTING": True})
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client  

 


def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'<input' in response.data 
    
def correct_login(email):
    tester = app.test_client()
    f = open ('tests/clubs.json', "r")
    data = json.loads(f.read())
    response = tester.post('/showSummary', data={'email': email}, follow_redirects=True)
    assert b'Welcome,' in response.data   
def test_correct_login():
    correct_login('john@simplylift.co')
    correct_login('admin@irontemple.com')
    correct_login('kate@shelifts.co.uk')    
def test_incorrect_login():
    tester = app.test_client()
    f = open ('tests/clubs.json', "r")
    data = json.loads(f.read())
    response = tester.post('/showSummary', data={'email': 'co'}, follow_redirects=True)
    assert b'Desole, cet email na pas ete trouve' in response.data
    
def test_book():
    tester = app.test_client()
    response = tester.get('/book/Spring%20Festival/Simply%20Lift')
    assert response.status_code == 200

def test_wrongbook():
    tester = app.test_client()
    response = tester.get('/book/Spring%20Festival/Sily%20Lift')
    assert response.status_code==400
    assert b"Something went wrong-please try again" in response.data
def test_purchases():
    tester = app.test_client()
    response = tester.post('/purchasePlaces', data={'club':"Simply Lift",'competition':"Spring Festival",'places': 3}, follow_redirects=True)
    assert b'Great-booking complete!' in response.data
    assert b'Number of Places: 22' in response.data
    assert b'Points available: 4' in response.data
def test_places_over_twelve():
    tester = app.test_client()
    response = tester.post('/purchasePlaces', data={'club':"Simply Lift",'competition':"Spring Festival",'places': 13}, follow_redirects=True)
    assert b'you cant' in response.data
def test_not_enough_places():
    tester = app.test_client()
    response = tester.post('/purchasePlaces', data={'club':"Simply Lift",'competition':"Spring Festival",'places': 30}, follow_redirects=True)
    assert b'not enough places' in response.data 
def test_not_enough_points():
    tester = app.test_client()
    response = tester.post('/purchasePlaces', data={'club':"Simply Lift",'competition':"Spring Festival",'places': 9}, follow_redirects=True)
    assert b'not enough points' in response.data 
def test_competitions_future():  
    tester = app.test_client()
    f = open ('tests/clubs.json', "r")
    data = json.loads(f.read())
    response = tester.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b'Fall Classic' not in response.data
def test_logout():
    tester = app.test_client()
    response = tester.get('/logout',follow_redirects=False)
    assert response.status_code==302
def test_dashboard():   
    tester = app.test_client()
    response = tester.get('/tab',follow_redirects=True)
    assert b'<td>Simply Lift</td>' in response.data
    assert b'<td>john@simplylift.co</td>' in response.data
def test_clubs():
    result = loadClubs()
    with open('tests/clubs.json') as clubs:
        assert result == json.load(clubs)['clubs']
def test_competitions():
    result = loadCompetitions()
    with open('tests/competitions.json') as comp:
        assert result == json.load(comp)['competitions']  
    
    
    
    
    

    