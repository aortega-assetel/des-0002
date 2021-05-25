# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase_order = fields.Char(string='Orden de compra')

    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        sale_order = self.env['sale.order'].search([('name', '=', result.invoice_origin)])
        if sale_order.purchase_order:
            result.purchase_order = str(sale_order.purchase_order)
        
        return result
