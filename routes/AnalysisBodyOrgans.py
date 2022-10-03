from flask import Blueprint, jsonify, request

from models.AnalysisBodyOrgansModel import AnalysisBodyOrgansModel
from database.db import get_connection

main=Blueprint('AnalysisBodyOrgans_blueprint', __name__)

@main.route('/<id>')
def get_AnalysisBodyOrgans(id):
    try:
        Analysis = AnalysisBodyOrgansModel.get_AnalysisBodyOrgansModel(id)
        return jsonify(Analysis)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_Analysis():
    try:
        Analysis_details = request.get_json()

        id = Analysis_details[0]['id']
        bodyorgansvalue = Analysis_details[0]['bodyorgansvalue']
        systems = Analysis_details[0]['systems']
        bodyorgans = Analysis_details[0]['bodyorgans']

        affected_rows = AnalysisBodyOrgansModel.update_AnalysisBodyOrgansModel(id, bodyorgansvalue, systems, bodyorgans)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500