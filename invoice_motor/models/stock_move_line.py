# -*- coding: utf-8 -*-
from odoo import models, api, fields

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    no_motor = fields.Char(string='No. Motor')


    
        