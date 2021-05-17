# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order = fields.Char(string='Orden de compra')