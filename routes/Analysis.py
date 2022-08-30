from flask import Blueprint, jsonify, request

from models.AnalysisModel import AnalysisModel
from database.db import get_connection

main=Blueprint('Analysis_blueprint', __name__)

@main.route('/')
def get_Analysis():
    try:
        Analysis = AnalysisModel.get_Analysis()
        return jsonify(Analysis)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_Analysi(id):
    try:
        Analysis = AnalysisModel.get_Analysi(id)
        return jsonify(Analysis)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_Analysis():
    try:
        Analysis_details = request.get_json()

        # IDAnalysis = Analysis_details[0]['IDPatient']
        IDPatient = Analysis_details[0]['IDPatient']
        IDDoctor = Analysis_details[0]['IDDoctor']
        URLLeft = Analysis_details[0]['URLLeft']
        URLRight = Analysis_details[0]['URLRight']
        Status = Analysis_details[0]['Status']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idanalysis),0) + 1 FROM analysis")
            id = cursor.fetchone()
        connection.close()
        IDAnalysis= int(id[0])

        affected_rows = AnalysisModel.add_Analysis(IDAnalysis, IDPatient, IDDoctor, URLLeft, URLRight, Status)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_Analysis():
    try:
        Analysis_details = request.get_json()

        IDAnalysis = Analysis_details[0]['IDAnalysis']
        Status = Analysis_details[0]['Status']

        affected_rows = AnalysisModel.update_Analysis(IDAnalysis, Status)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500