#! /usr/bin/python3
# Les imports concernent les librairies associées à flask et concernant la gestion des bases de données
from flask import Flask, request, flash, url_for, redirect, \
    render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # On crée une application flask définie par un nom d'application
app.config.from_pyfile('back.cfg')  # On affecte à cette application , un fichier de configuration
db = SQLAlchemy(app)  # On définie un système de bases de données associée à l'application


# On crée une classe représentant la première table de notre base de données
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    nom = db.Column('nom', db.String(60))
    prenom = db.Column('prenom', db.String(80))
    mail = db.Column('mail', db.String(100))
    telephone = db.Column('telephone', db.String(10))
    role = db.Column('role', db.Enum('admin', 'membre'))

    # On définit un constructeur en donnant un rôle par défaut
    def __init__(self, nom, prenom, mail, telephone):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.role = 'membre'


# Cette fonction permet de récupérer la totalité de notre table users en
# utilisant la requête http GET
@app.route('/user', methods=['GET'])
def show_all_users():
    return render_template('show_all_users.html', users=User.query.all())


@app.route('/user/delete', methods=['POST'])
def delete_user():
    identifier = request.form['delete_button']
    user = User.query.filter_by(id=identifier).first()
    db.session.delete(user)
    flash('UTILISATEUR SUPPRIME')
    db.session.commit()
    return redirect(url_for('show_all_users'))


@app.route('/user/new', methods=['GET'])
def show_new_user():
    return render_template('add_new_user.html')


# Cette fonction permet de créer une nouvelle entité user dans la table users (on utilise la requête http POST)
@app.route('/user/new', methods=['GET', 'POST'])
def add_new_user():
    if not request.form.get('nom', False):
        flash('Le nom est requis', 'error')
    elif not request.form.get('prenom', False):
        flash('Le prenom est requis', 'error')
    elif not request.form.get('mail', False):
        flash('Le mail est requis', 'error')
    elif not request.form.get('telephone', False):
        flash('mettre le n° tel est recommandé', 'warning')
    else:
        user = User(request.form['nom'], request.form['prenom'], request.form['mail'], request.form['telephone'])
        db.session.add(user)
        db.session.commit()
        flash(u'Compte bien créé !')
        return redirect(url_for('show_all_users'))
    return render_template('add_new_user.html')


@app.route('/user/update/<identifier>', methods=['GET'])
def show_update_user(identifier):
    return render_template('update_user.html', user=User.query.get(identifier))


# Cette fonction permet la modification d'une donnée d'une entitée dans la table users
@app.route('/user/update/<identifier>', methods=['POST'])
def update_user(identifier):
    user = User.query.get(identifier)
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    mail = request.form.get("mail")
    telephone = request.form.get("telephone")
    user.nom = nom
    user.prenom = prenom
    user.mail = mail
    user.telephone = telephone
    flash('UTILISATEUR MIS A JOUR')
    db.session.commit()
    return redirect(url_for('show_all_users'))


# On crée une classe représentant la table produits de notre base de données
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column('id', db.Integer, primary_key=True)
    nom = db.Column('nom', db.String(50))
    description = db.Column('description', db.String(300))
    qte = db.Column('qte', db.BigInteger)
    prix = db.Column('prix', db.Float)

    # On définit un constructeur en donnant un rôle par défaut
    def __init__(self, nom, description, qte, prix):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.qte = qte


@app.route('/products', methods=['GET'])
def show_all_products():
    return render_template('show_all_products.html', products=Product.query.all())


@app.route('/products/delete', methods=['POST'])
def delete_product():
    identifier = request.form['delete_button']
    product = Product.query.get(identifier)
    db.session.delete(product)
    flash('PRODUIT SUPPRIME')
    db.session.commit()
    return redirect(url_for('show_all_products'))


@app.route('/products/new', methods=['GET'])
def show_new_product():
    return render_template('add_new_product.html')


# Cette fonction permet de créer une nouvelle entité user dans la table users (on utilise la requête http POST)
@app.route('/products/new', methods=['GET', 'POST'])
def add_new_product():
    if not request.form.get('nom', False):
        flash('Le nom est requis', 'error')
    elif not request.form.get('description', False):
        flash('La desription est requise', 'error')
    elif not request.form.get('quantité', False):
        flash('La quantité est requise', 'error')
    elif not request.form.get('prix', False):
        flash('mettre le n° tel est recommandé', 'warning')
    else:
        product = Product(request.form['nom'], request.form['description'], request.form['quantité'],
                          request.form['prix'])
        db.session.add(product)
        db.session.commit()
        flash(u'Produit bien créé !')
        return redirect(url_for('show_all_products'))
    return render_template('add_new_product.html')


@app.route('/products/update/<identifier>', methods=['GET'])
def show_update_product(identifier):
    return render_template('update_product.html', product=Product.query.get(identifier))


# Cette fonction permet la modification d'une donnée d'une entitée dans la table users
@app.route('/products/update/<identifier>', methods=['POST'])
def update_product(identifier):
    product = Product.query.get(identifier)
    product.nom = request.form.get("nom")
    product.description = request.form.get("description")
    product.qte = request.form.get("quantité")
    product.prix = request.form.get("prix")
    flash('PRODUIT MIS A JOUR')
    db.session.commit()
    return redirect(url_for('show_all_products'))


if __name__ == '__main__':
    app.run(debug=True)
