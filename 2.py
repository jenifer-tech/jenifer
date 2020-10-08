from flask import*
app = Flask(__name__)

@app.route('/guest',methods=['GET'])
def hello_guest():
   print("Welcome guest page")
   return 'Hello  as Guest' 
   print(request.args)        


if __name__ == '__main__':
   app.run(debug = True)
