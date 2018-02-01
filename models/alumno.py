# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Alumno(models.Model):
    _name = 'consultas.alumno'
    _rec_name = "alu_nombre"

    alu_cui = fields.Integer(string="CUI",
                             required=True,
                             size=8,
                             index=True
                            )

    alu_nombre = fields.Char(string="Nombre",
                             size=30,
                             required=True
                            )

    alu_apellido = fields.Char(string="Apellidos",
                               size=30,
                               required=True
                              )
    _sql_constraints = [
        ('alu_unique',
         'UNIQUE (alu_cui)',
         'El codigo del alumno no puede repetirse!'
        )]