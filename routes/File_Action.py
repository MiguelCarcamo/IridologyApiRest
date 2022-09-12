from flask import Blueprint, jsonify, request

main=Blueprint('FileAction_blueprint', __name__)

from flask import request, send_from_directory
import os
from os import getcwd
from werkzeug.utils import secure_filename

PATH_FILES = getcwd() + '\\Files'
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '\\Files'

@main.route('/<id>')
def get_file(id):
    return send_from_directory(PATH_FILES, path=id, as_attachment=True)
    
@main.route('/add', methods=['POST'])
def add_file():
    try:
        x = request.files['File']
        x.save(os.path.join(PATH_FILES, secure_filename(x.filename)))
        return dict(msj='Accion Realizada Correctamente')
    except FileNotFoundError:
        return dict(msj='Folder not found')