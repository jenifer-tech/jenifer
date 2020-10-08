from flask import*
app = Flask(__name__)

stock={"names":{"name":"jenfer"}}
      
@app.route('/home/<name>')
def home(name):
    print("Hello {} You are in Home Page!".format(name))
    return "Hello {} You are in Home Page!".format(name)

@app.route('/query')
def query():
    name=request.args.get('name')
    print("Hello {} You are in query Page!".format(name))
    return "Hello {} You are in Query Page!".format(name)

@app.route('/json')
def json():
    a= jsonify({"name":"jenifer"})
    return a

@app.route('/stock')
def get_stock():
    res=make_response(jsonify(stock))
    return res

      
   
if __name__ == '__main__':
   app.run(debug = True)