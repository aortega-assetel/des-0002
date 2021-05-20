# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase_order = fields.Char(string='Orden de compra')



    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        sale_order = self.env['sale.order'].search([('name', '=', result.invoice_origin)])
        _logger.info(str(sale_order[0]))
        _logger.info(str(sale_order.purchase_order))
        self.purchase_order = str(sale_order.purchase_order)
        


        return result