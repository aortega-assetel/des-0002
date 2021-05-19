# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    

    first_name = fields.Char(string="Nombre(s)")
    last_name_1 = fields.Char(string="Apellido paterno")
    last_name_2 = fields.Char(string="Apellido materno")

    @api.onchange('first_name', 'last_name_1', 'last_name_2')
    def _on_change_first_name_last_name_1_last_name_2(self):
        nombre = self.first_name + ' ' +  self.last_name_1 + ' ' + self.last_name_2
        self.name = nombre