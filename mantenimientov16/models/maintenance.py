# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models, _


class mainten(models.Model):
    _inherit = 'maintenance.request'

    # name_seq = fields.Char(string='N° de Orden', required=True,
    #                        copy=False, readonly=True, index=True, default=lambda self: _('New'))
    dpto = fields.Many2one('hr.department', string="Departamento",)
    puesto = fields.Many2one('hr.job', string="Puesto", )
    cod_obra = fields.Many2one(
        'account.analytic.account', string="Código de Obra",)
    equipo = fields.Many2one('maintenance.equipment', string="Equipo",)
    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo", related="equipment_id.model",)
    Numserie = fields.Char(string="N°serie", related="equipment_id.serial_no",)
    hrs_trabajo = fields.Char(string="Odómetro / Horas de Trabajo",)
    desc_falla = fields.Text(
        string="Descripción de la Falla por Cliente Interno",)
    rep_inm = fields.Boolean(string="Reparación Inmediata",)
    rep_compra = fields.Boolean(string="Reposición compra",)
    rep_alma = fields.Boolean(string="Reposición por Almacén",)
    renta = fields.Boolean(string="Renta",)
    sust_herr = fields.Boolean(string="Sustitución de Herramienta ",)
    esp_rep = fields.Boolean(string="Espera de Reparación ",)
    otr = fields.Boolean(string="Otros ",)
    sign_confor = fields.Char(string="Firma de conformidad del usuario",)
    solucion_mante = fields.Text(string="Solución de Mantenimiento ",)
    fecha_comp = fields.Date(string="Fecha Compromiso de Entrega",)
    refa_ids = fields.One2many(
        comodel_name='refacciones.line', inverse_name='refacciones_id',)
    currency_id = fields.Many2one('res.currency', 'Currency',)
    revision = fields.Char(string="Revisión",)
    fecha_publi = fields.Date(string="Fecha de Publicación",)
    fecha_prox = fields.Date(string="Fecha de Próxima Revisión",)
    codigo = fields.Char(string="Código",)
    pregunta1 = fields.Selection([
        ('si', 'Si'),
        ('no', 'No')], string="¿Se realizó algún movimiento al equipo por el operador?",)
    explicacion = fields.Text(string="Explique Brevemente",)
    observaciones = fields.Text(
        string="Observaciones del Supervisor ante la solución inmediata",)
    flota = fields.Many2one(comodel_name='fleet.vehicle', string="Vehiculo",)

    # @api.model
    # def create(self, vals):
    #     if vals.get('name_seq', _('New')) == _('New'):
    #         vals['name_seq'] = self.env['ir.sequence'].next_by_code(
    #             'maintenance.request.sequence') or _('New')
    #     result = super(mainten, self).create(vals)
    #     return result
