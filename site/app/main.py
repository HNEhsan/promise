from flask import render_template, Flask, request

app = Flask(__name__)

sitenumber = 0
submitnumber = 0

@app.route("/")
def home():       
    op = open('log.txt','r')
    counter = op.readline()
    counter = str(counter)
    counter = int(counter)
    global sitenumber 
    sitenumber = counter
    op.close()
    op = open('log.txt','w')
    counter += 1
    counter = str(counter)
    op.writelines(str(counter))
    print('counter is :{}'.format(counter))
    op.close()

    return render_template('index.html')

@app.route('/log')
def log():
    global sitenumber

    return ''' <center> <b> user see the site is :{} </b>'''.format(sitenumber)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)