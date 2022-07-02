from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Length,Email

class mahasiswa_F(FlaskForm):
    npm = StringField('NPM',validators=[DataRequired(), Length(min==10,max==5)])
    nama = StringField('Nama',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    kelas = StringField('Kelas',validators=[DataRequired()])
    alamat = TextAreaField ('Alamat')
    submit = SubmitField('Tambah')
    