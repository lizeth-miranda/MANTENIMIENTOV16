# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models, _


class mainten(models.Model):
    _inherit = 'maintenance.equipment'

    marca = fields.Char(string="Marca",)
    obra = fields.Many2one(
        comodel_name='account.analytic.account', string="Obra", )
    sistemas = fields.Boolean(string='Sistemas', default=False,)

    employee = fields.Many2one('hr.employee', string='Empleado', tracking=True)

    department = fields.Char(
        related="employee.department_id.name",
        string="Departamento",
    )
    puesto = fields.Char(related="employee.job_id.name", string="Puesto")
