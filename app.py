from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola 👋, esta es mi Web App en Azure con Python!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
