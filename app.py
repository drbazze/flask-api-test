from flask import Flask

app = Flask(__name__)

@app.route("/status")
def health_endpoint():
    return "live"

if __name__ == "__main__":
    app.run()