from flask import Flask

app = Flask(__name__)

@app.route ('/')
def home():
    return 'Hell9 world'
    
if __name__ == '__main__':
   app.run 
