from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Hello</title></head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    """

@app.route("/metrics")
def metrics():
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
