from flask import*
app = Flask(__name__)

@app.route('/guest')
def hello_guest():
   
   print("Welcome guest page")
   x= request.args.get('x')
   y=request.args.get('y','15')
   z=request.args['z']
   return "The given value is {},{} and {}".format(x,y,z)
if __name__ == '__main__':
   app.run(debug = True)