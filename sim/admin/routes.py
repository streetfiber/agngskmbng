from flask import Flask, render_template, redirect, url_for

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data_mahasiswa", methods=['GET','POST'])
def data_m():
    form = mahasiswa_F()
    if form.validate_on_submit():
        return redirect(url_for('data_m'))
    return render_template( "data-mahasiswa.html", data_mahasiswa=data_mahasiswa, form=form)

@app.route("/artikel/<info>")
def artikel_info(info):
    return("halaman Artikel " + info)

