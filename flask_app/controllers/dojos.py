from flask_app import app
from flask import render_template, redirect, flash, session, request
from .. models import dojo


@app.route('/')
def show_form():
    return render_template("form.html")


@app.route('/create', methods=['post'])
def create():

    if not dojo.Dojo.validate(request.form):
        return redirect('/')

    dojo.Dojo.add(request.form)
    session['dojo'] = request.form
    return redirect("/results")


@app.route('/results')
def show_result():
    return render_template("result.html", dojo=session['dojo'])
