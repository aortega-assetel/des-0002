# -*- coding: utf-8 -*-
from odoo import models, api, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    motor = fields.Boolean(string='Motor', default=False)
    no_motor = fields.Char(string='No. Motor')

    
        