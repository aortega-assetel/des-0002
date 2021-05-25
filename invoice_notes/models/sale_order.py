# -*- coding: utf-8 -*-
from odoo import models, api, fields, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    account_move_id = fields.Many2one('account.move', string="Facturas")
    delivery_id = fields.Many2one('stock.picking', string='Pedidos')

    def invoice_note(self, vals):
        for bud in self:
            for fac in bud.account_move_id:
                budget_id = self.env['sale.order'].search([('name', '=', fac.invoice_origin)])
                if budget_id:
                    for mess in bud.picking_ids:
                        if bud.invoice_count > 0:
                            mess.message_post(body='PEDIDO FACTURADO <br/><br/><button name="%(action_view_url)d" string="FACTURAR" type="action"/>')


    def action_view_url(self):
        id_view = self.account_move_id.id
        for reg in self:
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
