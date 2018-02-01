# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime

class Semestre(models.Model):
    _name = 'consultas.semestre'
    _rec_name = "smt_codigo"

    smt_estado = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Activo'),
        ('closed', 'Cerrado')
        ])

    smt_codigo = fields.Integer(string="Codigo Semestre",
                                required=True,
                                size=8,
                                index=True
                               )

    smt_fecha_inicio = fields.Date(string="Inicio",
                                   help="Fecha de inicio",
                                   required=True,
                                  )

    smt_fecha_fin = fields.Date(string="Finalizacion",
                                help="Fecha de finalizacion",
                                required=True,
                               )

    # relaciones
    smt_smt_crs_ids = fields.One2many('consultas.smt_crs',
                                      'smt_crs_semestre_id',
                                      string="Detalle de semestre",
                                     )

    # defaults
    _defaults = {
        'smt_estado': 'draft',
        'smt_fecha_inicio': datetime.now().strftime('%Y-%m-%d'),
        'smt_fecha_fin': datetime.now().strftime('%Y-%m-%d')
    }

    # buttons actions
    @api.one
    def activate(self):
        #Generates a random name between 9 and 15 characters long and writes it to the record.
        self.smt_estado = 'active'

    @api.one
    def close(self):
        #Generates a random name between 9 and 15 characters long and writes it to the record.
        self.smt_estado = 'closed'

    # Order
    def _generate_order_by(self, order_spec, query):
        my_order = "CASE WHEN smt_estado='draft' THEN 0 WHEN smt_estado = 'active'  THEN 1 ELSE 2 END"
        if order_spec:
            return super(Semestre, self)._generate_order_by(order_spec, query) + ", " + my_order
        return " order by " + my_order

    # constraints
    _sql_constraints = [
        ('smt_unique',
         'UNIQUE (smt_codigo)',
         'El codigo del semestre no puede repetirse!'
        )]