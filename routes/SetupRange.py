from flask import Blueprint, jsonify, request

from models.SetupRangeModel import SetupFoodsModel
from database.db import get_connection

main=Blueprint('setuprange_blueprint', __name__)

@main.route('/')
def get_SetupRange():
    try:
        SetupSystems = SetupFoodsModel.get_SetupRanges()
        return jsonify(SetupSystems)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_SetupRange():
    try:
        setuprange_details = request.get_json()

        # idsetuprange= setuprange_details[0]['idsetuprange']
        setuprange= setuprange_details[0]['setuprange']
        rangemax= setuprange_details[0]['RangeMax']
        rangemin= setuprange_details[0]['RangeMin']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetuprange),0) + 1 from setuprange")
            id = cursor.fetchone()
        connection.close()
        idsetuprange= int(id[0])

        affected_rows = SetupFoodsModel.add_SetupRanges(idsetuprange, setuprange, rangemax, rangemin)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_SetupRange():
    try:
        setuprange_details = request.get_json()
        idsetuprange= setuprange_details[0]['idsetuprange']
        setuprange= setuprange_details[0]['setuprange']
        rangemax= setuprange_details[0]['RangeMax']
        rangemin= setuprange_details[0]['RangeMin']

        affected_rows = SetupFoodsModel.update_SetupRanges(idsetuprange, setuprange, rangemax, rangemin)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500   