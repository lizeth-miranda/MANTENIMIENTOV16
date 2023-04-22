# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class promaint(models.Model):
    _inherit = 'product.template'

    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo",)
    proveedor = fields.Many2one(
        string="Proveedor", comodel_name="res.partner",)
    num_serie = fields.Char(string="Número de Serie",)
    empleado = fields.Many2one(
        string="Empleado Responsable", comodel_name="hr.employee",)
    obra = fields.Many2one(
        comodel_name='account.analytic.account', string="Obra", )
    fecha_exp = fields.Date(string="Fecha Expiración Garantía",)
    responsable = fields.Many2one(
        comodel_name="res.users", string="Responsable",)
    plan_id = fields.Many2one(
        'hr.plan', default=lambda self: self.env['hr.plan'].search([], limit=1))
    equipos = fields.Many2one(
        comodel_name='maintenance.equipment', string="Equipos", )

    def enviar(self):
        for record in self:
            buscar = self.env['maintenance.equipment'].search_count([
                ('serial_no', '=', record.num_serie),

            ])
            if buscar > 0:
                raise ValidationError(
                    _("Uno o varios de los registros ya existen"))

            elif not buscar:
                vals = {
                    'name': record.name,
                    'serial_no': record.num_serie,
                    'model': record.modelo,
                    'marca': record.marca,
                    'warranty_date': record.fecha_exp,
                    'employee_id': record.empleado.id,
                    'obra': record.obra.id,
                    'partner_id': record.proveedor.id,
                    'cost': record.standard_price,
                }
                record.env['maintenance.equipment'].create(vals)
                for activity_type in self.plan_id.plan_activity_type_ids:
                    activity = self.env['mail.activity'].create({
                        'res_id': self.equipos.id,
                        'res_model_id': self.env['ir.model']._get('maintenance.equipment').id,
                        'summary': activity_type.summary,
                        'note': activity_type.note,
                        'activity_type_id': activity_type.activity_type_id.id,
                        'user_id': self.responsable.id,
                    })
                    activity._onchange_activity_type_id()
                    activity.user_id = self.responsable.id
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'message': 'Registro Exitoso',
                        'type': 'rainbow_man',
                    }
                }

    # def action_launch(self):
    #     for activity_type in self.plan_id.plan_activity_type_ids:
    #         responsible = activity_type.get_responsible_id(self.employee_id)

    #         if self.env['hr.employee'].with_user(responsible).check_access_rights('read', raise_exception=False):
    #             activity = self.env['mail.activity'].create({
    #                 'res_id': self.employee_id.id,
    #                 'res_model_id': self.env['ir.model']._get('hr.employee').id,
    #                 'summary': activity_type.summary,
    #                 'note': activity_type.note,
    #                 'activity_type_id': activity_type.activity_type_id.id,
    #                 'user_id': responsible.id,
    #             })
    #             activity._onchange_activity_type_id()
    #             activity.user_id = responsible.id

    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'hr.employee',
    #         'res_id': self.employee_id.id,
    #         'name': self.employee_id.display_name,
    #         'view_mode': 'form',
    #         'views': [(False, "form")],
    #     }
