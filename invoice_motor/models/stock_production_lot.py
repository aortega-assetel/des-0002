# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    motor = fields.Boolean(string='Motor', default=False)
    no_motor = fields.Char(string='No. Motor')

    @api.model
    def create(self, vals):
        result = super(StockProductionLot, self).create(vals)

        serie = self.env['stock.move.line'].search([('lot_id.name', '=', result.name)])
        _logger.info(str(serie))
        _logger.info(str(vals))
        result.motor = True
        result.no_motor = vals.no_motor

        return result


    
        