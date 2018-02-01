# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Inscripcion(models.Model):
    _name = 'consultas.inscripcion'
    _rec_name = "ins_smt_crs_id"

    ins_semestre = fields.Many2one('consultas.semestre',
                                   string="Semestre",
                                   required=True
                                  )

    ins_smt_crs_id = fields.Many2one('consultas.smt_crs',
                                     string="Curso de Semestre",
                                     required=True
                                    )

    ins_ins_alu_ids = fields.One2many('consultas.ins_alu',
                                      'ins_alu_inscripcion_id',
                                      string="",
                                     )
