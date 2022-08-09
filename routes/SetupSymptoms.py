from flask import Blueprint, jsonify, request
from models.SetupSymptomsModel import SetupSymptomsModel
from database.db import get_connection

main=Blueprint('setupsymptoms_blueprint', __name__)

@main.route('/')
def get_SetupSymptoms():
    try:
        SetupSymptoms = SetupSymptomsModel.get_SetupSymptoms()
        return jsonify(SetupSymptoms)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_SetupSymptom(id):
    try:
        SetupSymptoms = SetupSymptomsModel.get_SetupSymptom(id)
        return jsonify(SetupSymptoms)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_SetupSymptom():
    try:
        setupsymptom_details = request.get_json()

        # IDSetupSymptoms = setupsymptom_details[0]['IDSetupSymptoms']
        IDSetupBodyOrgans = setupsymptom_details[0]['IDSetupBodyOrgans']
        Symptoms = setupsymptom_details[0]['Symptoms']
        RangeMax = setupsymptom_details[0]['RangeMax']
        RangeMin = setupsymptom_details[0]['RangeMin']
        Lenguage = setupsymptom_details[0]['Lenguage']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetupsymptoms),0) + 1 from setupsymptoms")
            id = cursor.fetchone()
        connection.close()
        IDSetupSymptoms= int(id[0])

        affected_rows = SetupSymptomsModel.add_SetupSymptom(IDSetupSymptoms, IDSetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_SetupSymptom():
    try:
        setupsymptom_details = request.get_json()

        IDSetupSymptoms = setupsymptom_details[0]['IDSetupSymptoms']
        IDSetupBodyOrgans = setupsymptom_details[0]['IDSetupBodyOrgans']
        Symptoms = setupsymptom_details[0]['Symptoms']
        RangeMax = setupsymptom_details[0]['RangeMax']
        RangeMin = setupsymptom_details[0]['RangeMin']
        Lenguage = setupsymptom_details[0]['Lenguage']

        affected_rows = SetupSymptomsModel.update_SetupSymptom(IDSetupSymptoms, IDSetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500