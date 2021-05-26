# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one('sale.order', string="Facturas")
    delivery_id = fields.Many2one('stock.picking', string='Pedidos')

    def action_post(self):
        result = super(AccountMove, self).action_post()
        body = '<p>PEDIDO FACTURADO:</p><p style=" "></p><a href="/web#id='+ str(self.id) +'&amp;action=270&amp;active_id=21&amp;model=account.move&amp;view_type=form&amp;cids=1&amp;menu_id=233" class="btn btn-primary" style=" ">Ir a Factura</a><p></p>'
        if self.state == 'posted':
            sale_order = self.env['sale.order'].search([('name', '=', self.invoice_origin)])
            for mess in sale_order.picking_ids:
                mess.message_post(body=body)
        return result


    def action_view_url(self):
        id_view = self.id
        for reg in self.sale_order_id:
            if reg.invoice_count>1:
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://aortega-assetel-des-0002-test1-2563447.dev.odoo.com/web?#id=%s&action=270&active_id=4&model=account.move&view_type=list&cids=1&menu_id=233" % id_view,
                    'target': 'new',
                }
            else:
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://aortega-assetel-des-0002-test1-2563447.dev.odoo.com/web?#id=%s&action=270&active_id=4&model=account.move&view_type=form&cids=1&menu_id=233" % id_view,
                    'target': 'new',
                }
