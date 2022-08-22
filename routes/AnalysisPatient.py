from flask import Blueprint, jsonify, request

from models.AnalysisPatientModel import AnalysisPatientModel
from database.db import get_connection

main=Blueprint('AnalysisPatient_blueprint', __name__)

@main.route('/')
def get_AnalysisPatients():
    try:
        AnalysisPatient = AnalysisPatientModel.get_AnalysisPatients()
        return jsonify(AnalysisPatient)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_AnalysisPatient(id):
    try:
        AnalysisPatient = AnalysisPatientModel.get_AnalysisPatient(id)
        return jsonify(AnalysisPatient)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        AnalysisPatient_details = request.get_json()

        # IDPatient = AnalysisPatient_details[0]['IDPatient']
        IDUser = AnalysisPatient_details[0]['IDUser']
        PatientName = AnalysisPatient_details[0]['PatientName']
        PatientLastName = AnalysisPatient_details[0]['PatientLastName']
        Lenguage = AnalysisPatient_details[0]['Lenguage']
        BirthDate = AnalysisPatient_details[0]['BirthDate']
        Gender = AnalysisPatient_details[0]['Gender']
        Weight = AnalysisPatient_details[0]['Weight']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idpatient),0) + 1 FROM analysispatient")
            id = cursor.fetchone()
        connection.close()
        IDPatient= int(id[0])

        affected_rows = AnalysisPatientModel.add_AnalysisPatient(IDPatient, IDUser, PatientName, PatientLastName, Lenguage, BirthDate, Gender, Weight)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_user():
    try:
        AnalysisPatient_details = request.get_json()

        IDPatient = AnalysisPatient_details[0]['IDPatient']
        PatientName = AnalysisPatient_details[0]['PatientName']
        PatientLastName = AnalysisPatient_details[0]['PatientLastName']
        Lenguage = AnalysisPatient_details[0]['Lenguage']
        BirthDate = AnalysisPatient_details[0]['BirthDate']
        Gender = AnalysisPatient_details[0]['Gender']
        Weight = AnalysisPatient_details[0]['Weight']

        affected_rows = AnalysisPatientModel.update_AnalysisPatient(IDPatient, PatientName, PatientLastName, Lenguage, BirthDate, Gender, Weight)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500