from flask import Blueprint, jsonify, request

from models.SetupSystemsModel import SetupSystemsModel
from database.db import get_connection

main=Blueprint('setupsystems_blueprint', __name__)

@main.route('/')
def get_SetupSystems():
    try:
        SetupSystems = SetupSystemsModel.get_SetupSystems()
        return jsonify(SetupSystems)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_user(id):
    try:
        SetupSystems = SetupSystemsModel.get_SetupSystem(id)
        if SetupSystems != None:
            return jsonify(SetupSystems)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        setupsystems_details = request.get_json()

        setupsystems= setupsystems_details[0]['SetupSystems']
        rangemax= setupsystems_details[0]['RangeMax']
        rangemin= setupsystems_details[0]['RangeMin']
        lenguage= setupsystems_details[0]['Lenguage']
        importance_level= setupsystems_details[0]['importance_level']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetupsystems),0) + 1 from setupsystems")
            id = cursor.fetchone()
        connection.close()
        idsetupsystems= int(id[0])

        affected_rows = SetupSystemsModel.add_SetupSystems(idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importance_level)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_user():
    try:
        setupsystems_details = request.get_json()
        idsetupsystems= setupsystems_details[0]['IDSetupSystems']
        setupsystems= setupsystems_details[0]['SetupSystems']
        rangemax= setupsystems_details[0]['RangeMax']
        rangemin= setupsystems_details[0]['RangeMin']
        lenguage= setupsystems_details[0]['Lenguage']
        importance_level= setupsystems_details[0]['importance_level']

        affected_rows = SetupSystemsModel.update_SetupSystems(idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importance_level)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500   