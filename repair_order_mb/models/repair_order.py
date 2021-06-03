# -*- coding: utf-8 -*-
from odoo import models, api, fields

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    lot_id = fields.Many2one(
        'stock.production.lot', 'Lot/Serial', check_company=True,
        help="Products repaired are all belonging to this lot")

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        serie = self.env['stock.production.lot'].search([['id', '=', self.lot_id]])
        self.product_id = serie.product_id
