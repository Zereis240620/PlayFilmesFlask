from app import db

class User(db.Model):
	__tablename__ = "users"

	id       = db.Column(db.Integer, primary_key=True)
	login    = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return '<Users %r>' % self.login

class Category(db.Model):
	__tablename__ = "categorys"
	
	id          = db.Column(db.Integer, primary_key=True)
	descricao   = db.Column(db.String(200))

	def __repr__(self):
		return '<Category %r>' % self.id

class Filme(db.Model):
	__tablename__ = "filmes"

	id          = db.Column(db.Integer, primary_key=True)
	nome        = db.Column(db.String(200))
	duracao     = db.Column(db.String(200))
	ano		    = db.Column(db.String(200))
	url         = db.Column(db.String(200))
	capa        = db.Column(db.String(200))
	resumo		= db.Column(db.Text)
	id_user_cad = db.Column(db.Integer, db.ForeignKey("users.id"))
	id_category = db.Column(db.Integer, db.ForeignKey("categorys.id"))

	user     = db.relationship("User", foreign_keys= id_user_cad)
	category = db.relationship("Category", foreign_keys= id_category)

	def __repr__(self):
		return '<Filme %r>' % self.id