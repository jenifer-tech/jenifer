from flask import*
app = Flask(__name__)

@app.route('/stn')
def hello_guest():
   
    print("Name section")

    name=request.args.get('name', 'Hai.....Pass parameter in your name')
    return name
       
   
if __name__ == '__main__':
   app.run(debug = True)