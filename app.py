from flask import Flask, request, jsonify
from routes import User, SetupSystems, SetupBodyOrgans, SetupFindings, SetupSymptoms
app = Flask(__name__)
# Routes

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.register_blueprint(User.main, url_prefix='/api/user')
    app.register_blueprint(SetupSystems.main, url_prefix='/api/SetupSystems')
    app.register_blueprint(SetupBodyOrgans.main, url_prefix='/api/SetupBodyOrgans')
    app.register_blueprint(SetupFindings.main, url_prefix='/api/SetupFindings')
    app.register_blueprint(SetupSymptoms.main, url_prefix='/api/SetupSymptoms')
    app.run(threaded=True, port=5000)