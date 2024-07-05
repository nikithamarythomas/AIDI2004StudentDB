from flask import Flask
app = Flask(__name__) #creating the Flask class object
@app.route('/') #decorator
def home():
    return "Hello! Welcome to my flask";
if __name__ =='__main__':
    app.run()
