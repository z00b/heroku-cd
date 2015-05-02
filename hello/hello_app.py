from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, I'm at TechCrunch Disrupt!"

if __name__ == "__main__":
    app.run()
