# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactsAddons(models.Model):
    _inherit = 'res.partner'
    
    @api.depends('name_indiviual', 'surname_matern', 'surname_patern')
    def _concatenate_fields_contacts_addons(self):
        nombre = + str(self.name_indiviual) + str(self.surname_patern) + str(self.surname_matern)

        self.update({
            'name': nombre
        })


    name_indiviual = fields.Char(string="Nombre(s)", store=True, compute='_concatenate_fields_contacts_addons', tracking=4)
    surname_matern = fields.Char(string="Apellido materno")
    surname_patern = fields.Char(string="Apellido paterno")