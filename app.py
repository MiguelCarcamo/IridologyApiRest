from flask import Flask
from flask_cors import CORS
from routes import User, SetupSystems, SetupBodyOrgans, SetupFindings, SetupSymptoms, AnalysisPatient
app = Flask(__name__)
# Routes
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

app.register_blueprint(User.main, url_prefix='/api/user')
app.register_blueprint(SetupSystems.main, url_prefix='/api/SetupSystems')
app.register_blueprint(SetupBodyOrgans.main, url_prefix='/api/SetupBodyOrgans')
app.register_blueprint(SetupFindings.main, url_prefix='/api/SetupFindings')
app.register_blueprint(SetupSymptoms.main, url_prefix='/api/SetupSymptoms')
app.register_blueprint(AnalysisPatient.main, url_prefix='/api/AnalysisPatient')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)