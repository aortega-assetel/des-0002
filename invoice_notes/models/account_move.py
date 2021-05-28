# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self, result):
        result = super(AccountMove, self).action_post()
        body = '<p>PEDIDO FACTURADO:</p><p style=" "></p><a href="/web#id='+ str(self.id) +'&amp;action=270&amp;active_id=21&amp;',
        'model=account.move&amp;view_type=form&amp;cids=1&amp;menu_id=233" class="btn btn-primary" style=" ">Ir a Factura</a><p></p>'
        if self.state == 'posted':
            sale_order = self.env['sale.order'].search([('name', '=', self.invoice_origin)])
            for mess in sale_order.picking_ids:
                mess.message_post(body=body)

                #Si tengo actividad registrada en transferencia la borro
                if mess.stock_activity_id:
                    mess.stock_activity_id.unlink()

                model_id = mess.env['ir.model']._get(self._name).id
                activity_id = self.env['mail.activity.type'].search([['stock_move_activity', '=', True]])

                vals = {
                    'res_model' : "stock.picking",
                    'res_model_id' : model_id,
                    'res_id' : mess.id,
                    'summary' : "Finalizar Entrega",
                    'activity_type_id' : activity_id.id,
                    #'date_deadline' : mess.stock_finish_date,
                    'user_id' : mess.activity_user_id.id,
                }
                new_activity = self.env['mail.activity'].create(vals)
                mess.stock_activity_id = new_activity.id
        return result