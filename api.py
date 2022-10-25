from flask import Flask

app=Flask(__name__)

@app.route("/")
def default():
    return "welcome from docker"


@app.route("/display")
def read():
    
    return "display from docker"


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8090)