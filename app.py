from flask import Flask, render_template
from wtforms import form

from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g 


import forms
from model import db
from model import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_noy_found(e):
    return render_template("404.html")

@app.route("/", methods=['POST','GET'])
@app.route("/index")
def index():
	create_form = forms.UserForm(request.form)
	alumnos = Alumnos.query.all()
	return render_template("index.html",form=create_form, alumnos=alumnos)

@app.route("/Alumnos",methods=['POST','GET'])
def alumnos():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST':

        alumno = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data, 
            amaterno=create_form.amaterno.data, 
            email=create_form.email.data,
        )

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("alumnos.html", form=create_form)

@app.route("/detalles",methods=['POST','GET'])
def detalles():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		nombre = alumn.nombre
		apaterno = alumn.aPaterno
		correo = alumn.email
	return render_template(
     "detalles.html",
     	alumn= alumn,
		nombre= nombre,
		apaterno= apaterno,
		correo= correo,
	)
@app.route("/modificar",methods=['POST','GET'])
def modificar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.nombre.data = alumn.nombre.data
		create_form.apaterno.data = alumn.aPaterno.data
		create_form.correo.data = alumn.email.data
	if request.method=='POST':
		alumn.db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.nombre.data = alumn.nombre.data
		create_form.apaterno.data = alumn.aPaterno.data
		create_form.correo.data = alumn.email.data
		db.session.add(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html",form=create_form)

@app.route("/eliminar",methods=['POST','GET'])
def eliminar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.nombre.data = alumn.nombre.data
		create_form.apaterno.data = alumn.aPaterno.data
		create_form.correo.data = alumn.email.data
	if request.method=='POST':
		alumn.db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.nombre.data = alumn.nombre.data
		create_form.apaterno.data = alumn.aPaterno.data
		create_form.correo.data = alumn.email.data
		db.session.delete(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html",form=create_form)

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	with app.app_context():	
		db.create_all()
	app.run(debug=True)