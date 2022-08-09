from flask import Blueprint, jsonify, request
from models.SetupFindingsModel import SetupFindingsModel
from database.db import get_connection

main=Blueprint('setupfindings_blueprint', __name__)

@main.route('/')
def get_SetupFindings():
    try:
        SetupFindings = SetupFindingsModel.get_SetupFindings()
        return jsonify(SetupFindings)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_SetupFinding(id):
    try:
        SetupFinding = SetupFindingsModel.get_SetupFinding(id)
        return jsonify(SetupFinding)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_SetupFinding():
    try:
        setupfindings_details = request.get_json()

        # IDSetupFindings = setupfindings_details[0]['IDSetupFindings']
        IDSetupBodyOrgans = setupfindings_details[0]['IDSetupBodyOrgans']
        Foods = setupfindings_details[0]['Foods']
        NotFoods = setupfindings_details[0]['NotFoods']
        Findings = setupfindings_details[0]['Findings']
        RangeMax = setupfindings_details[0]['RangeMax']
        RangeMin = setupfindings_details[0]['RangeMin']
        Lenguage = setupfindings_details[0]['Lenguage']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetupfindings),0) + 1 from setupfindings")
            id = cursor.fetchone()
        connection.close()
        IDSetupFindings= int(id[0])

        affected_rows = SetupFindingsModel.add_SetupFinding(IDSetupFindings, IDSetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_SetupFinding():
    try:
        setupfindings_details = request.get_json()

        IDSetupFindings = setupfindings_details[0]['IDSetupFindings']
        IDSetupBodyOrgans = setupfindings_details[0]['IDSetupBodyOrgans']
        Foods = setupfindings_details[0]['Foods']
        NotFoods = setupfindings_details[0]['NotFoods']
        Findings = setupfindings_details[0]['Findings']
        RangeMax = setupfindings_details[0]['RangeMax']
        RangeMin = setupfindings_details[0]['RangeMin']
        Lenguage = setupfindings_details[0]['Lenguage']

        affected_rows = SetupFindingsModel.update_SetupFinding(IDSetupFindings, IDSetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500