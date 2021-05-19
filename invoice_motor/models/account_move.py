# -*- coding: utf-8 -*-
from odoo import models, api, fields

import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        count = 0
        for line in result.invoice_line_ids:
            line.sequence = count
            
            for line_sale in line.sale_line_ids:
                for line_move in line_sale.move_ids:
                    stock_move_line = self.env['stock.move.line'].search([('move_id', '=', line_move.id)])
                    for linea in stock_move_line:
                        note_text = ''
                        for product_variant in line.product_id.product_template_attribute_value_ids:
                            if 'Modelo' in product_variant.display_name or 'Marca' in product_variant.display_name or 'Cilindrada' in product_variant.display_name or 'Color' in product_variant.display_name:
                                attribute = product_variant.display_name
                                note_text = note_text + attribute + '.\n'

                        serie = linea.lot_id.name
                        no_motor = linea.lot_id.no_motor
                        referencia = linea.reference

                        pedimento = self.env['stock.move.line'].search([('lot_id.name', '=', serie)])
                        date_1 = self.env['stock.landed.cost'].search([('picking_ids', '=', linea.move_id.picking_id.name)])

                        _logger.info(str(pedimento))

                        note_text = note_text + 'Serie: ' + serie +'.\n' + 'No Motor: ' + no_motor +'.\n' + 'Pedimento: ' + str(pedimento.l10n_mx_edi_customs_number) +'.\n' + 'Fecha de ingreso: ' + str(date_1) +'.\n'
            

                        values = {
                                'name' : note_text,
                                'display_type': 'line_note',
                                'move_id': result.id,
                                'sequence': count + 1,
                            }
                        new_note = self.env['account.move.line'].create(values)
                        count = count + 2


        return result
    