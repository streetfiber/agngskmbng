from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_wtf.file import FileField,FileAllowed

class mahasiswa_F(FlaskForm):
    npm = StringField('NPM',validators=[DataRequired()])
    nama = StringField('Nama',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    kelas = StringField('Kelas',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    kon_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat = TextAreaField ('Alamat')
    submit = SubmitField('Tambah')

    #ceknpm
    def validate_npm(self,npm):
        ceknpm = Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM sudah terdaftar, Gunakan NPM yang lain')

     #cekemail
    def validate_email(self,email):
        cekemail = Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email sudah terdaftar, Gunakan Email yang lain')

class loginmahasiswa_F(FlaskForm):
    npm = StringField('NPM',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Tambah')

class editmahasiswa_F(FlaskForm):
    npm = StringField('NPM',validators=[DataRequired()])
    nama = StringField('Nama',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    kelas = StringField('Kelas',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    kon_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat = TextAreaField ('Alamat')
    foto = FileField('Ubah Foto Profil', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Ubah data')

    #ceknpm
    def validate_npm(self,npm):
        if npm.data != current_user.npm:
            ceknpm = Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM sudah terdaftar, Gunakan NPM yang lain')

     #cekemail
    def validate_email(self,email):
        if email.data != current_user.email:
            cekemail = Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email sudah terdaftar, Gunakan Email yang lain')

class pengaduan_F(FlaskForm):
    subjek = StringField('Subjek',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'),('fasilitas','Fasilitas'), ('dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan= TextAreaField('Pengaduan')
    submit = SubmitField('Kirim')

class editpengaduan_F(FlaskForm):
    subjek = StringField('Subjek',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'),('fasilitas','Fasilitas'), ('dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan= TextAreaField('Pengaduan')
    submit = SubmitField('Ubah')

class artikel_F(FlaskForm):
    judul = StringField('Judul artikel : ',validators=[DataRequired()])
    kategori= SelectField(u'Kategori artikel : ', choices=[('ikan','Ikan'),('Action','Aksi'), ('ternate','Ternate')], validators=[DataRequired()])
    detail_artikel= TextAreaField('Artikel')
    submit = SubmitField('Kirim')

class editartikel_F(FlaskForm):
    subjek = StringField('Subjek',validators=[DataRequired()])
    kategori= SelectField(u'Kategori artikel : ', choices=[('ikan','Ikan'),('Action','Aksi'), ('ternate','Ternate')], validators=[DataRequired()])
    detail_artikel= TextAreaField('Artikel')
    submit = SubmitField('Ubah')

class surat_F(FlaskForm):
    subjek = StringField('Pengirim : ',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Surat : ', choices=[('HMJ','Hmj'),('Pemerintah','Pemerintah'), ('Kampus','Kamppus')], validators=[DataRequired()])
    detail_surat= TextAreaField('Isi Surat : ')
    submit = SubmitField('Kirim')

class editsurat_F(FlaskForm):
    subjek = StringField('Pengirim :',validators=[DataRequired()])
    kategori= SelectField(u'Kategori Surat', choices=[('HMJ','Hmj'),('Pemerintah','Pemerintah'), ('Kampus','Kamppus')], validators=[DataRequired()])
    detail_surat= TextAreaField('Pengaduan')
    submit = SubmitField('Ubah')

