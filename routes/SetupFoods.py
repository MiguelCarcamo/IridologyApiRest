from flask import Blueprint, jsonify, request
from models.SetupFoodsModel import SetupFoodsModel
from database.db import get_connection

main=Blueprint('setupfoods_blueprint', __name__)

@main.route('/')
def get_SetupFoods():
    try:
        SetupFoods = SetupFoodsModel.get_SetupFoods()
        return jsonify(SetupFoods)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_SetupFood(id):
    try:
        SetupFinding = SetupFoodsModel.get_SetupFood(id)
        return jsonify(SetupFinding)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_SetupFood():
    try:
        setupfoods_details = request.get_json()

        # IDSetupFoods = setupfoods_details[0]['IDSetupFoods']
        idsetupsystems = setupfoods_details[0]['idsetupsystems']
        Foods = setupfoods_details[0]['Foods']
        NotFoods = setupfoods_details[0]['NotFoods']
        RangeMax = setupfoods_details[0]['RangeMax']
        RangeMin = setupfoods_details[0]['RangeMin']
        Lenguage = setupfoods_details[0]['Lenguage']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetupfoods),0) + 1 from setupfoods")
            id = cursor.fetchone()
        connection.close()
        IDSetupFoods= int(id[0])

        affected_rows = SetupFoodsModel.add_SetupFood(IDSetupFoods, idsetupsystems, Foods, NotFoods, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_SetupFood():
    try:
        setupfoods_details = request.get_json()

        IDSetupFoods = setupfoods_details[0]['IDSetupFoods']
        # idsetupsystems = setupfoods_details[0]['idsetupsystems']
        Foods = setupfoods_details[0]['Foods']
        NotFoods = setupfoods_details[0]['NotFoods']
        RangeMax = setupfoods_details[0]['RangeMax']
        RangeMin = setupfoods_details[0]['RangeMin']
        Lenguage = setupfoods_details[0]['Lenguage']

        affected_rows = SetupFoodsModel.update_SetupFood(IDSetupFoods, Foods, NotFoods, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500