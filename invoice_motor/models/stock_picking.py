# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.onchange('state')
    def _onchange_state(self):
        #By Alan Ortega
        if self.state == 'done':
            for line in self.move_line_nosuggest_ids:
                serie = self.env['stock.production.lot'].search([('id', '=', line.lot_id.id)])
                serie.motor = True
                serie.no_motor = line.no_motor
        #By Alan Ortega


    
        