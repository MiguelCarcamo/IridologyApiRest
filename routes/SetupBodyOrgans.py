from flask import Blueprint, jsonify, request
from database.db import get_connection
from models.SetupBodyOrgansModel import SetupBodyOrgansModel

main=Blueprint('setupbodyorgans_blueprint', __name__)

@main.route('/')
def get_SetupBodyOrgans():
    try:
        SetupBodyOrgans = SetupBodyOrgansModel.get_SetupBodyOrgans()
        return jsonify(SetupBodyOrgans)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_SetupBodyOrgan(id):
    try:
        SetupBodyOrgans = SetupBodyOrgansModel.get_SetupBodyOrgan(id)
        if SetupBodyOrgans != None:
            return jsonify(SetupBodyOrgans)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        setupbodyOrgan_details = request.get_json()

        # IDSetupBodyOrgans = setupbodyOrgan_details[0]['IDSetupBodyOrgans']
        IDSetupSystems = setupbodyOrgan_details[0]['IDSetupSystems']
        BodyOrgans = setupbodyOrgan_details[0]['BodyOrgans']
        Left = setupbodyOrgan_details[0]['Left']
        Right = setupbodyOrgan_details[0]['Right']
        Men = setupbodyOrgan_details[0]['Men']
        Womman = setupbodyOrgan_details[0]['Womman']
        RangeMax = setupbodyOrgan_details[0]['RangeMax']
        RangeMin = setupbodyOrgan_details[0]['RangeMin']
        Lenguage = setupbodyOrgan_details[0]['Lenguage']

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idsetupbodyorgans),0) + 1 from setupbodyorgans")
            id = cursor.fetchone()
        connection.close()
        IDSetupBodyOrgans= int(id[0])

        affected_rows = SetupBodyOrgansModel.add_SetupBodyOrgan(IDSetupBodyOrgans, IDSetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update', methods=['PUT'])
def update_user():
    try:
        setupbodyOrgan_details = request.get_json()

        IDSetupBodyOrgans = setupbodyOrgan_details[0]['IDSetupBodyOrgans']
        IDSetupSystems = setupbodyOrgan_details[0]['IDSetupSystems']
        BodyOrgans = setupbodyOrgan_details[0]['BodyOrgans']
        Left = setupbodyOrgan_details[0]['Left']
        Right = setupbodyOrgan_details[0]['Right']
        Men = setupbodyOrgan_details[0]['Men']
        Womman = setupbodyOrgan_details[0]['Womman']
        RangeMax = setupbodyOrgan_details[0]['RangeMax']
        RangeMin = setupbodyOrgan_details[0]['RangeMin']
        Lenguage = setupbodyOrgan_details[0]['Lenguage']

        affected_rows = SetupBodyOrgansModel.update_SetupBodyOrgan(IDSetupBodyOrgans, IDSetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage)

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500