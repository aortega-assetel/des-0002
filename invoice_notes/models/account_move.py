# -*- coding: utf-8 -*-
from odoo import models, api, fields, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one('sale.order', string="Facturas")
    delivery_id = fields.Many2one('stock.picking', string='Pedidos')

    @api.onchange('state')
    def invoice_note(self, vals):
        for invoice in self:
            if invoice.state == 'posted':
                sale_order = self.env['sale.order'].search([('name', '=', invoice.invoice_origin)])
                for mess in sale_order.picking_ids:
                    mess.message_post(body='PEDIDO FACTURADO <br/><br/><button name="%(action_view_url)d" string="FACTURAR" type="action"/>')
                    mess.message_post(body='Facturado')
            else:
                for mess in sale_order_id.picking_ids:
                    mess.message_post(body='No Facturado')


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
