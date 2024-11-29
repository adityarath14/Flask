from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/First')
def First():
    return 'First Flask Project'
@FAI.route('/aditya')
def aditya():
    return render_template('aditya.html')
@FAI.route('/demo/<data>/')
def demo(data):
    return f'demo {data}'
@FAI.route('/view')
def view():
    return render_template('view.html')
if __name__=='__main__':
    FAI.run(debug=True,host='192.168.43.95',port=5001)