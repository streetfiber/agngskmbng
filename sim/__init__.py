from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask('__name__',template_folder='sim/templates', static_folder='sim/static')
app.config['SECRET_KEY']="d6079c2d0066bfd187b348e8df6fb192"
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///sim_pengaduan.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)


from sim.mahasiswa.routes import rmahasiswa
app.register_blueprint(rmahasiswa)