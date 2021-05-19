# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    cost_aduana = fields.Char(string="Aduana")