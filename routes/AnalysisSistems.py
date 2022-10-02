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