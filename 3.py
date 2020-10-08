from flask import*
app = Flask(__name__)

@app.route('/guest')
def hello_guest():
   
   print("Welcome guest page")
   print( request.args.get('xy'))
   print(request.args.get('yz'))
   return request.args.get('jeni')
if __name__ == '__main__':
   app.run(debug = True)
