# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Curso(models.Model):
    _name = 'consultas.curso'
    _rec_name = "crs_nombre"

    crs_codigo = fields.Integer(string="Codigo Curso",
                                required=True,
                                size=8,
                                index=True
                               )

    crs_nombre = fields.Char(string="Nombre Curso",
                             size=30,
                             required=True
                            )

    _sql_constraints = [
        ('crs_unique',
         'UNIQUE (crs_codigo)',
         'El codigo del curso no puede repetirse!'
        )]