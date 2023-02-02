from flask import Flask
from flask_cors import CORS
from routes import User, SetupSystems, SetupBodyOrgans, SetupFindings, SetupSymptoms, AnalysisPatient, Analysis, File_Action, AnalysisSistems, AnalysisBodyOrgans, SetupFoods, SetupRange
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
app.register_blueprint(Analysis.main, url_prefix='/api/Analysis')
app.register_blueprint(AnalysisSistems.main, url_prefix='/api/AnalysisSistems')
app.register_blueprint(AnalysisBodyOrgans.main, url_prefix='/api/AnalysisBodyOrgans')
app.register_blueprint(SetupFoods.main, url_prefix='/api/SetupFoods')
app.register_blueprint(SetupRange.main, url_prefix='/api/SetupRange')
app.register_blueprint(File_Action.main, url_prefix='/api/File')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)