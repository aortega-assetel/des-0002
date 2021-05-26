# -*- coding: utf-8 -*-
from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    no_motor = fields.Char(string='No. Motor')

    @api.onchange('lot_id')
    def _onchange_state(self):
        #By Alan Ortega
        _logger.info('MODEL: 1')
        if self.lot_id:
            _logger.info('MODEL: 3')
            self.lot_id.motor = True
            self.lot_id.no_motor = self.no_motor
        #By Alan Ortega


    
        