#! /usr/bin/python3

from flask import Flask, request, flash, url_for, redirect, \
    render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('back.cfg')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    nom = db.Column('nom', db.String(60))
    prenom = db.Column('prenom', db.String(80))
    mail = db.Column('mail', db.String(100))
    telephone = db.Column('telephone', db.String(10))
    role = db.Column('role', db.Enum('admin', 'membre'))

    def __init__(self, nom, prenom, mail, telephone):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.role = 'member'


@app.route('/')
def show_all_users():
    return render_template('show_all.html', users=User.query.all())


@app.route('/user/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['nom']:
            flash('Le nom est requis', 'error')
        elif not request.form['prenom']:
            flash('Le prenom est requis', 'error')
        elif not request.form['mail']:
            flash('Le mail est requis', 'error')
        elif not request.form['telephone']:
            flash('mettre le n° tel est recommandé', 'warning')
        else:
            user = User(request.form['nom'], request.form['prenom'], request.form['mail'], request.form['telephone'])
            db.session.add(user)
            db.session.commit()
            flash(u'Compte bien créé !')
            return redirect(url_for('show_all_users'))
    return render_template('new.html')


@app.route('/user/update', methods=['POST'])
def update_user():
    for user in User.query.all():
        user.nom = ('nom.%d' % user.id) in request.form
        user.prenom = ('prenom.%d' % user.id) in request.form
        user.mail = ('mail.%d' % user.id) in request.form
        user.telephone = ('telephone.%d' % user.id) in request.form
    flash('UTILISATEUR MIS A JOUR')
    db.session.commit()
    return redirect(url_for('show_all_users'))


if __name__ == '__main__':
    app.run()
