import os
from flask import render_template, redirect, request, flash, url_for, send_file
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from app import app, db, lm
from app.models.forms import LoginForm, FilmeForm
from app.models.tables import User, Filme

@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@app.route('/', methods=['GET'], defaults={"page": 1}) 
@app.route('/<int:page>', methods=['GET'])
def index(page):
	pag = page
	per_page = 8
	data = Filme.query.order_by(Filme.id.asc()).paginate(pag,per_page,error_out=False)	
	return render_template('index.html', filmes=data)


@app.route("/login/", methods=['GET','POST'])
def login():
	form = LoginForm()	
	if form.validate_on_submit():		
		user = User.query.filter_by(login=form.login.data).first()		
		if user and user.password == form.password.data:
			login_user(user)
			flash("Logged In")
			return redirect('/listFilmesCad')

		else:
			flash("Invalid Login")

	else:
		print(form.errors)

	if current_user.is_authenticated:
		return redirect('/')

	return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/filme/", methods=['GET'], defaults={"id": None})
@app.route("/filme/<id>", methods=['GET'])
def filme(id):
	if id:
		filme = Filme.query.filter_by(id = id).first()
		return render_template('player.html', url = filme.url)

	return render_template('player.html')


@app.route("/listFilmesCad/", methods=['GET'], defaults={"page": 1})
@app.route("/listFilmesCad/<int:page>", methods=['GET'])
@login_required
def listFilmesCad(page):
	pag = page
	per_page = 7	
	data = Filme.query.paginate(pag,per_page,error_out=False)

	return render_template('ListFilme.html', filmes=data)


@app.route("/deleteFilme/<int:id>", methods=['GET'])
@login_required
def deleteFilme(id):
	filme = Filme.query.get(id)		
	if(filme):
		db.session.delete(filme)
		db.session.commit()

	return redirect('/listFilmesCad')



@app.route('/get_images/<int:filme_id>')
@login_required
def get_image(filme_id = None):
	
	if(filme_id != None):		
		filme = Filme.query.filter_by(id=filme_id).first()

		if(filme):
			filename = os.path.join(app.config['UPLOAD_FOLDER'], filme.capa)
			return redirect(url_for('static', filename=filename), code=301)

		return None


@app.route("/cadfilme/<int:filme_id>")
@app.route("/cadfilme/",methods=['GET','POST'])
@login_required
def cadFilme(filme_id = None):
	form = FilmeForm()
	if form.validate_on_submit():

		if form.capa.data:
			film = Filme(						 
						 nome 		 = form.nome.data,
			 			 duracao 	 = form.duracao.data,
						 ano 		 = form.ano.data,
						 url 	     = form.url.data,
						 capa 		 = form.capa.data.filename,
						 resumo 	 = form.resumo.data,
						 id_user_cad = form.id_user_cad.data,
						 id_category = form.id_category.data)
					
			f = form.capa.data
			filename = secure_filename(f.filename)
			f.save(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER'], filename))
			db.session.add(film)
			db.session.commit()

		else:						
			
			filme = Filme.query.get(int(form.id.data))
			filme.id          = form.id.data
			filme.nome 		  = form.nome.data
			filme.duracao 	  = form.duracao.data
			filme.ano 		  = form.ano.data
			filme.url 	      = form.url.data
			filme.capa 		  = filme.capa
			filme.resumo	  = form.resumo.data
			filme.id_user_cad = form.id_user_cad.data
			filme.id_category = form.id_category.data
			db.session.commit()			


		return render_template('FormFilme.html',form = form)

	else:
		print(">Error: ",form.errors)

	print(filme_id)

	if(filme_id != None):
		print('Edit')
		filme = Filme.query.filter_by(id=filme_id).first()

		if(filme):			
			form.id.data            = filme.id
			form.nome.data          = filme.nome
			form.duracao.data		= filme.duracao
			form.ano.data			= filme.ano
			form.url.data			= filme.url			
			form.resumo.data		= filme.resumo
			form.id_user_cad.data	= filme.id_user_cad
			form.id_category.data	= filme.id_category

	else:
		print(">>> Not edit")

	return render_template('FormFilme.html', form=form)


@app.route("/listfilme", methods=['GET'])
@login_required
def listFilme():
	# Query pegando filmes e mandando pra cá
	return render_template('ListFilme.html')