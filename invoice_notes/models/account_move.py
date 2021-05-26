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
        body = '<p>PEDIDO FACTURADO:</p><p style=" "></p><a href="/web#id='+ str(self.id) +'&amp;action=270&amp;active_id=21&amp;',
        'model=account.move&amp;view_type=form&amp;cids=1&amp;menu_id=233" class="btn btn-primary" style=" ">Ir a Factura</a><p></p>'
        if self.state == 'posted':
            sale_order = self.env['sale.order'].search([('name', '=', self.invoice_origin)])
            for mess in sale_order.picking_ids:
                mess.message_post(body=body)
                if mess.stock_activity_id:
                    mess.stock_activity_id.unlink()
                model_id = self.env['ir.model']._get(self._name).id
                activity_id = self.env['mail.activity.type'].search([['demo_ending_activity', '=', True]])

        return result


    def create_activity_demo(self, result):
        if result.stock_activity_id:
            result.stock_activity_id.unlink()

        model_id = self.env['ir.model']._get(self._name).id
        activity_id = self.env['mail.activity.type'].search([['demo_ending_activity', '=', True]])

        vals = {
            'res_model' : "installed.services",
            'res_model_id' : model_id,
            'res_id' : result.id,
            'summary' : "Finalizar demo",
            'activity_type_id' : activity_id.id,
            'date_deadline' : result.demo_finish_date,
            'user_id' : result.project_task.project_id.user_id.id,
        }
        new_activity = self.env['mail.activity'].create(vals)
        result.demo_activity_id = new_activity.id
