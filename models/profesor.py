# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime

class Profesor(models.Model):
    _name = 'consultas.profesor'
    _rec_name = "prf_nombre"

    prf_nombre = fields.Char(string="Nombres",
                             size=30,
                             required=True
                            )

    prf_apellido = fields.Char(string="Apellidos",
                               size=30,
                               required=True
                              )

    prf_direccion = fields.Char(string="Dirección",
                                size=50,
                                required=True
                               )

    prf_edad = fields.Integer(string="Edad",
                              required=True,
                              size=8,
                             )

    prf_telefono = fields.Char(string="Telefono",
                               required=True,
                               size=8,
                              )

    prf_fecha_nacimiento = fields.Date(string="Fecha de nacimiento",
                                       help="Nacimiento",
                                       required=True,
                                      )

    prf_fecha_hora_ingreso = fields.Datetime(string="Fecha y Hora ingreso",
                                             help="Fecha y Hora"
                                            )

    prf_foto = fields.Binary(string="Foto")

