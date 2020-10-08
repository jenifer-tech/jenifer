from flask import*
app = Flask(__name__)

@app.route('/noj',methods=['GET','POST'])
def hello_guest():
   
    x=request.get_json('x')
    return x

      
   
if __name__ == '__main__':
   app.run(debug = True)