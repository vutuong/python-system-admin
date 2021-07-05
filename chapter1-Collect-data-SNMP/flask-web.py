from flask import Flask, render_template

folder = '/home/dcn/python-system-admin/chapter1-Collect-data-SNMP'
app = Flask(__name__, template_folder=folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_1.html')
def index1():
    return render_template('check_1.html')

@app.route('/check_2.html')
def index2():
    return render_template('check_2.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')