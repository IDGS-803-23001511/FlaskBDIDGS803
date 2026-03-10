from flask import Flask, render_template
from wtforms import form

from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g 
from flask_migrate import Migrate
from maestros.routes import maestros


import forms
from model import Maestros, db
from model import Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
db.init_app(app)
migrate=Migrate(app,db)
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
            apellidos=create_form.apellidos.data, 
            telefono=create_form.telefono.data, 
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
		apellidos = alumn.apellidos
		telefono= alumn.telefono
		email = alumn.email
	return render_template(
     "detalles.html",
     	alumn= alumn,
		nombre= nombre,
		apellidos= apellidos,
		email= email,
		telefono=telefono
	)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    id = request.args.get('id')
    alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    if request.method == 'GET':
        create_form.id.data=request.args.get('id')
        create_form.nombre.data = alumn.nombre
        create_form.apellidos.data = alumn.apellidos
        create_form.telefono.data = alumn.telefono
        create_form.email.data = alumn.email

    if request.method == 'POST':
        alumn=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn.nombre = create_form.nombre.data
        alumn.apellidos = create_form.apellidos.data
        alumn.telefono = create_form.telefono.data
        alumn.email = create_form.email.data

        db.session.commit()
        return redirect(url_for('index'))

    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    id = request.args.get('id')

    alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    if request.method == 'GET':
        create_form.id.data=request.args.get('id')
        create_form.nombre.data = alumn.nombre
        create_form.apellidos.data = alumn.apellidos
        create_form.telefono.data = alumn.telefono
        create_form.email.data = alumn.email

    if request.method == 'POST':
        db.session.delete(alumn)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("eliminar.html", form=create_form)
	
#Maestros
@app.route("/index_maestro")
def index_maestro():
    maestros = Maestros.query.all()
    return render_template("index_maestro.html", maestros=maestros)
@app.route("/Maestros", methods=['POST','GET'])
def maestros():
    create_form = forms.MaestroForm(request.form)
    maestros = Maestros.query.all()

    if request.method == 'POST':

        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data,
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('index_maestro'))

    return render_template("Maestros.html", form=create_form, maestros=maestros)

@app.route("/maestro_detalles", methods=['GET'])
def maestro_detalles():

    matricula = request.args.get('matricula')

    maestro = Maestros.query.filter_by(matricula=matricula).first()

    if maestro is None:
        return redirect(url_for('index_maestro'))

    return render_template(
        "maestro_detalles.html",
        nombre=maestro.nombre,
        apellidos=maestro.apellidos,
        especialidad=maestro.especialidad,
        email=maestro.email
    )
@app.route("/maestro_modificar", methods=['GET', 'POST'])
def maestro_modificar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')

    maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

    if request.method == 'GET':
        create_form.matricula.data = matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST':
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data

        db.session.commit()
        return redirect(url_for('index_maestro'))

    return render_template("maestro_modificar.html", form=create_form)
@app.route("/maestro_eliminar", methods=['GET', 'POST'])
def maestro_eliminar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')

    maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

    if request.method == 'GET':
        create_form.matricula.data = matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('index_maestro'))

    return render_template("maestro_eliminar.html", form=create_form)

if __name__ == '__main__':
	csrf.init_app(app)

	with app.app_context():	
		db.create_all()
	app.run(debug=True)