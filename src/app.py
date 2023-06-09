from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    x=1
    return "Taylor Swift, Fearless, Speak Now, Red, 1989, Rep, Folklore, Evermore, Midnights"

if __name__ == "__main__": 
    app.run()

