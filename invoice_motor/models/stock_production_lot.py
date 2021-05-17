# -*- coding: utf-8 -*-
from odoo import models, api, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    motor = fields.Boolean(string='Motor', default=False)
    no_motor = fields.Char(string='No. Motor')

    @api.model
    def create(self, vals):
        result = super(StockProductionLot, self).create(vals)

        serie = self.env['stock.move.line'].search([('lot_id', '=', result.id)])

        result.motor = True
        result.no_motor = serie.no_motor

        return result


    
        