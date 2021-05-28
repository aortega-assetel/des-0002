# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    

    first_name = fields.Char(string="Nombre(s)")
    last_name_1 = fields.Char(string="Apellido paterno")
    last_name_2 = fields.Char(string="Apellido materno")

    @api.onchange('first_name', 'last_name_1', 'last_name_2')
    def _on_change_first_name_last_name_1_last_name_2(self):
        nombre = ''
        if self.first_name:
            nombre += self.first_name + ' '
        if self.last_name_1:
            nombre += self.last_name_1 + ' '
        if self.last_name_2:
            nombre += self.last_name_2

        self.update({
            'name': nombre + str(self.first_name) + str(self.last_name_1) + str(self.last_name_2)
        })
