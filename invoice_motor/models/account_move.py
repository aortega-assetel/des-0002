# -*- coding: utf-8 -*-
from odoo import models, api, fields

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        count = 0
        for line in result.invoice_line_ids:
            for i in range(2):
                line.sequence = count
                note_text = ''
                for product_variant in line.product_id.product_template_attribute_value_ids:
                    if 'Modelo' in product_variant.display_name or 'Marca' in product_variant.display_name or 'Cilindrada' in product_variant.display_name or 'Color' in product_variant.display_name:
                        attribute = product_variant.display_name
                        note_text = note_text + attribute + '.\n'
                
                '''for line_sale in line.sale_line_ids:
                    for line_move in line_sale.move_ids:
                        stock_move_line = self.env['stock.move.line'].search([('move_id', '=', line_move.id)])

                        for linea in stock_move_line:
                            serie = linea.lot_id.name
                            no_motor = linea.lot_id.no_motor

                            note_text = note_text + 'Serie: ' + serie +'.\n' + 'No Motor: ' + no_motor +'.\n'
'''
                                
                        values = {
                                'name' : note_text,
                                'display_type': 'line_note',
                                'move_id': result.id,
                                'sequence': count + 1,
                            }
                        new_note = self.env['account.move.line'].create(values)
                        count = count + 2


        return result
    