from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField
Application_Instance=Flask(__name__)
@Application_Instance.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        data=request.form
        return data['na']
    return render_template('form.html')
class Nameform(Form):
    name=StringField()
    submit=SubmitField()
@Application_Instance.route('/webform',methods=['GET','POST'])
def webform():
    form=Nameform()
    if request.method=='POST':
        dat=Nameform(request.form)
        return dat.name.data
    return render_template('webform.html',form=form)
Application_Instance.run(debug=True)