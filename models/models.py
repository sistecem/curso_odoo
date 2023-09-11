# -*- coding: utf-8 -*-

from odoo import models, fields, api


class curso_odoo(models.Model):
    _name = 'curso_odoo.curso_odoo'
    _description = 'curso_odoo.curso_odoo'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    date = fields.Date(string='Fecha')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
