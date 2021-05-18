# -*- coding: utf-8 -*-
from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    account_move_id = fields.Many2one('account.move', string="Facturas")