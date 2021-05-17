# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    pays_order = fields.One2many('account.payment', 'quotation_id', string='Pagos')
    
    @api.depends('pays_order.state')
    def _total_pagado_sale_order_addons(self):
        for reg in self:
            total_pagado = 0 
            for line in reg.pays_order:
                if line.state == 'posted':
                    total_pagado += line.amount

            reg.update({
                'total_pagado': total_pagado
            })

    total_pagado = fields.Monetary(string='Total pagado', store=True, readonly=True, compute='_total_pagado_sale_order_addons', tracking=4)
    
    @api.depends('amount_total', 'total_pagado')
    def _importe_adeudado_sale_order_addons(self):
        for order in self:
            total_orden = order.amount_total
            total_pagado = order.total_pagado

        order.update({
            'importe_adeudado': total_orden - total_pagado
        })
    
    importe_adeudado = fields.Monetary(string='Importe adeudado', store=True, readonly=True, compute='_importe_adeudado_sale_order_addons', tracking=4)



    def action_pay_register(self):
        circular = "Pago para cotización " + str(self.name)
        #Action para el boton "Registrar pago"
        action = self.env.ref('account.action_account_payments').read()[0] #ID Action=189
        action['views'] = [(self.env.ref('account.view_account_payment_form').id, 'form')] #ID Externo de la vista
        action['context'] = {'default_partner_id': self.partner_id.id, 'default_ref': circular, 'default_quotation_id': self.id} #Campos 
        action['target'] = 'new' #Acción que realiza una ventana como acceso rapido
        return action
