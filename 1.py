from flask import*
app = Flask(__name__)

@app.route('/admin/<admin>')
def hello_admin(admin):
   if admin=='vijina':
      print("Welcome Admin page")
      return 'Hello {}  You are Admin now !'.format(admin)
   else:
      return "You are not admin"   


if __name__ == '__main__':
   app.run(debug = True)

