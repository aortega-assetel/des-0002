# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AduanaShowroom(models.Model):
    _inherit = 'stock.landed.cost'

    cost_aduana = fields.Char(string="Aduana")