# -*- coding: utf-8 -*-
from odoo import models, api, fields, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_order_id = fields.Many2one('sale.order', string='Presupuesto')

    @api.model    
    def create(self, vals):
        result = super(StockPicking, self).create(vals)
        if result.sale_order_id.invoice_count > 0:
            result.message_post(body='PEDIDO FACTURADO <br/><br/><button name="%(action_view_url)d" string="FACTURAR" type="action""/>')  
        else:
            result.message_post(body='Por el momento no hay pedidos facturados')

        return result

    def action_view_url(self):
        id_view = self.sale_order_id.account_move_id.id
        for reg in self:
            if reg.sale_order_id.invoice_count>1:
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://assetel-test02-2459183.dev.odoo.com/web?#id=%s&action=381&active_id=2415&model=account.move&view_type=list&cids=1&menu_id=389" % id_view,
                    'target': 'new',
                }
            else:
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://assetel-test02-2459183.dev.odoo.com/web?#id=%s&action=381&active_id=2415&model=account.move&view_type=form&cids=1&menu_id=389" % id_view,
                    'target': 'new',
                }