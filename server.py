import json
from flask import Flask, render_template, request, session, url_for, redirect,flash
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

    
def create_app(config): 
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object("config")
    app.config["TESTING"] = config.get("TESTING")


    competitions = loadCompetitions()
    clubs = loadClubs()   
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        clubs1 = [club for club in clubs if club['email'] == request.form['email']]
        competitions1= [competition for competition in competitions if ((datetime.strptime(competition['date'],"%Y-%m-%d %H:%M:%S"))>datetime.now())]
        if clubs1:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html', club=club, competitions=competitions1)
        else :
            error='Desole, cet email na pas ete trouve'
            return render_template('index.html', error=error)


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        try:
            foundClub = [c for c in clubs if c['name'] == club][0]
            foundCompetition = [c for c in competitions if c['name'] == competition][0]
            if foundClub and foundCompetition:
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
        except:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions), 400


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]        
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        club['points'] 
        placesRequired = int(request.form['places'])
        if placesRequired < int(competition['numberOfPlaces']) :
            if placesRequired < 12 :
                if placesRequired*3 < int(club['points']):
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
                    club['points']=int(club['points'])-placesRequired*3
                    flash('Great-booking complete!')
                else:
                    flash('not enough points')
            else:
                flash('you cant, it s over 12, Please retry ')
        else:
            flash('not enough places')
        competitions1= [competition for competition in competitions if ((datetime.strptime(competition['date'],"%Y-%m-%d %H:%M:%S"))>datetime.now())]
        return render_template('welcome.html', club=club, competitions=competitions1)


    # TODO: Add route for points display
    @app.route('/tab')
    def tab():
        return render_template('tab.html', clubs=clubs)

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app

app = create_app({"TESTING": False})


if __name__ == "__main__":
    app.run(debug=True)