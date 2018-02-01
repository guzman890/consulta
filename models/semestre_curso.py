# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Semestre_Curso(models.Model):
    _name = 'consultas.smt_crs'
    _rec_name = "smt_crs_curso_id"

    smt_crs_creditos = fields.Integer(string="Creaditos de curso",
                                      required=True,
                                      size=2,
                                      index=True
                                     )
    # relaciones
    smt_crs_semestre_id = fields.Many2one('consultas.semestre',
                                          string="Semestre",
                                          ondelete="cascade",
                                          required=True
                                         )

    smt_crs_curso_id = fields.Many2one('consultas.curso',
                                       string="Cursos",
                                       required=True
                                      )

    smt_crs_profesor_id = fields.Many2one('consultas.profesor',
                                          string="Profesores",
                                          required=True
                                         )

    smt_crs_inscripcion_ids = fields.One2many('consultas.inscripcion',
                                              'ins_smt_crs_id',
                                              string="",
                                             )
