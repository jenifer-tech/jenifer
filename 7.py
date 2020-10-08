from flask import*
app = Flask(__name__)

@app.route('/no')
def hello_guest():
   
    return request.args.get('x','Nul')


       
   
if __name__ == '__main__':
   app.run(debug = True)