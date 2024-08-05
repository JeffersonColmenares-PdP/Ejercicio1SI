""" rutas del servicio 2 """

from flask import Blueprint

from . import controllers

#----------------- PRINCIPAL ------------------------------

servicio_2_blueprint = Blueprint(
    "servicio_2_blueprint",
    __name__,
    url_prefix='/usuario',
)

#-----------------TABLA PAISES ------------------------------
servicio_2_blueprint.add_url_rule(
    "/crear",
    view_func=controllers.agregar_usuario,
    methods=["POST"]
)