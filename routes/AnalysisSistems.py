from flask import Blueprint, jsonify, request

from models.AnalysisSistemsModel import AnalysisSistemsModel
from database.db import get_connection

main=Blueprint('AnalysisSistems_blueprint', __name__)

@main.route('/<id>')
def get_AnalysisSistems(id):
    try:
        Analysis = AnalysisSistemsModel.get_AnalysisSistems(id)
        return jsonify(Analysis)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_AnalysisSistems():
    try:
        Analysis_details = request.get_json()

        id = Analysis_details[0]['id']

        affected_rows = AnalysisSistemsModel.update_AnalysisSistems(id)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500