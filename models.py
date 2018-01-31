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
                                          required= True
                                         )

    smt_crs_curso_id = fields.Many2one('consultas.curso',
                                       string="Cursos",
                                       required=True
                                      )

    smt_crs_profesor_id = fields.Many2one('consultas.profesor',
                                          string="Profesores",
                                          required=True
                                         )

    ins_ins_crs_ids = fields.One2many('consultas.ins_crs',
                                      'ins_crs_smt_crs_id',
                                      string="Inscripciones",
                                     )

class Inscripcion(models.Model):
    _name = 'consultas.inscripcion'
    _rec_name = "ins_alumno"

    ins_alumno = fields.Many2one('consultas.alumno',
                                 string="Alumno",
                                 required=True
                                )

    ins_semestre = fields.Many2one('consultas.semestre',
                                   string="Semestre",
                                   required=True
                                  )
    ins_ins_crs_ids = fields.One2many('consultas.ins_crs',
                                      'ins_crs_inscripcion_id',
                                      string="Inscripcion detalle",
                                     )


class Inscripcion_Curso_Semestre(models.Model):
    _name = 'consultas.ins_crs'
    _rec_name = "ins_crs_inscripcion_id"

    ins_crs_inscripcion_id = fields.Many2one('consultas.inscripcion',
                                             string="Cursos",
                                             required=True
                                            )

    ins_crs_smt_crs_id = fields.Many2one('consultas.smt_crs',
                                         string="semestre curso",
                                         required=True
                                        )

    ins_nota_uno = fields.Integer(string="Nota uno",
                                  required=True,
                                  size=8,
                                  index=True
                                 )

    ins_nota_dos = fields.Integer(string="Nota dos",
                                  required=True,
                                  size=8,
                                  index=True
                                 )
