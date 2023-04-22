# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, exceptions, _


class refa(models.Model):
    _name = "refacciones.line"
    _description = 'Registro de refacciones y facturas'

    refa_uti = fields.Char(string="Refacciones Utilizadas",)
    fac = fields.Char(string="Factura",)
    costos = fields.Monetary(string="Costos",)
    refacciones_id = fields.Many2one(
        'maintenance.request', string="Refacciones Utilizadas",)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=lambda self: self.env.company.currency_id.id)
