from Flask import Flask 
app = Flask(__name__) 

# routing the decorator function hello_name 
@app.route('/hello/<name>') 
def hello_name(name): 
    return 'I love you %s!' % name 

if __name__ == '__main__': 
    app.run(debug = True) 
