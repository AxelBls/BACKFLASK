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
