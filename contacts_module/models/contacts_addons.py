# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactsAddons(models.Model):
    _inherit = 'res.partner'

    name_indiviual = fields.Char(string="Nombre(s)")
    surname_matern = fields.Char(string="Apellido materno")
    surname_patern = fields.Char(string="Apellido paterno")