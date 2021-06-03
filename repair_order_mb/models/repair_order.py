# -*- coding: utf-8 -*-
from odoo import models, api, fields

class RepairOrder(models.Model):
    _inherit = 'repair.order'


    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        serie = self.env['stock.production.lot'].search([['id', '=', self.lot_id]])
        self.product_id = serie.product_id
