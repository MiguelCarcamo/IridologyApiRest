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