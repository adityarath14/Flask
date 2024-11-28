from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/First')
def First():
    return 'First Flask Project'
@FAI.route('/aditya')
def aditya():
    return render_template('aditya.html')
if __name__=='__main__':
    FAI.run(debug=True)