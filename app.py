from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return('I LOVE U')

if(__name__=="__main__"):
   app.run()