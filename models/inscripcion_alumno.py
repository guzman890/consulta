# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Inscripcion_alumno(models.Model):
    _name = 'consultas.ins_alu'
    _rec_name = "ins_alu_alumno_id"

    ins_alu_inscripcion_id = fields.Many2one('consultas.inscripcion',
                                             string="Cursos",
                                             required=True
                                            )

    ins_alu_alumno_id = fields.Many2one('consultas.alumno',
                                        string="Alumno",
                                        required=True
                                       )

    ins_alu_uno = fields.Integer(string="Nota uno",
                                 size=8,
                                 onchange="_compute_promedio",
                                 index=True
                                )

    ins_alu_dos = fields.Integer(string="Nota dos",
                                 size=8,
                                 onchange="_compute_promedio",
                                 index=True
                                )

    ins_alu_promedio = fields.Float(string="Promedio",
                                    compute='_compute_promedio'
                                   )

    @api.multi
    def _compute_promedio(self):
        self.ins_alu_promedio = (float(self.ins_alu_uno + self.ins_alu_dos))/2