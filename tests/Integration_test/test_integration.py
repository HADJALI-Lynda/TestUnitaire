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
def test_integration():
    ##loadClubs()
    clubs=loadClubs()
    first_mail =clubs[0]['email']
    ##loadCompetitions
    competitions=loadCompetitions()
    ##index()
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'<input' in response.data
    ##showSummary()
    response=tester.post('/showSummary',data=dict(email=first_mail),follow_redirects=True)
    assert response.status_code ==200
    result='Welcome, '+first_mail
    result=str.encode(result)
    assert result in response.data
    ##book()
    first_club =clubs[0]['name']
    first_competition=competitions[0]['name']
    b='/book/'+first_competition+'/'+first_club   
    response = tester.get(b)
    assert response.status_code == 200
    assert b'How many places?' in response.data
    ##purchase()
    response = tester.post('/purchasePlaces', data={'club':first_club,'competition':first_competition,'places': 1}, follow_redirects=True)
    assert b'Great-booking complete!' in response.data
    assert b'Number of Places: 24' in response.data
    assert b'Points available: 10' in response.data
    ##logout()
    response = tester.get('/logout',follow_redirects=True)
    assert response.status_code==200
    assert b'Please enter your ' in response.data
    

    
              

            
    