
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">
        <h1>Welcome to Azure!</h1>
        <h2>Python 3.15 Web Application</h2>
        <p>Successfully deployed using Azure App Service.</p>
        <h3>Running on Microsoft Azure Cloud</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
