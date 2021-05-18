# -*- coding: utf-8 -*-
from odoo import models, api, fields

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        '''count = 0
        for line in result.invoice_line_ids:
            line.sequence = count
            product = self.env['product.product'].search([('id', '=', line.product_id.id)])
            note_text = ''
            for product_variant in product.attribute_line_ids:
                attribute_value = ''
                count_values = 0
                for attribute_line in product_variant.value_ids:
                    attribute = product_variant.attribute_id.name
                    if count_values == 0:
                        attribute_value = attribute_value + attribute_line.name
                    else:
                        attribute_value = attribute_value + ', ' + attribute_line.name
                    count_values = count_values + 1
                    
                
                
                note_text = note_text + attribute + ': ' + attribute_value + '.\n'
            values = {
                        'name' : note_text,
                        'display_type': 'line_note',
                        'move_id': result.id,
                        'sequence': count + 1,
                    }
            new_note = self.env['account.move.line'].create(values)
            count = count + 2
'''
        count = 0
        for line in result.invoice_line_ids:
            line.sequence = count
            note_text = ''
            for product_variant in line.product_id.product_template_attribute_value_ids:
                if 'Modelo' in product_variant.display_name or 'Marca' in product_variant.display_name or 'Cilindrada' in product_variant.display_name or 'Color' in product_variant.display_name:
                    attribute = product_variant.display_name
                    note_text = note_text + attribute + '.\n'
            
            for line_sale in line.sale_line_ids:
                for line_move in line.move_ids:
                    stock_move_line = self.env['stock.move.line'].search([('move_id', '=', line_move.id)])
                    serie = stock_move_line.lot_id.name
                    no_motor = stock_move_line.lot_id.no_motor

            note_text = note_text + 'Serie: ' + serie +'.\n' + 'No Motor: ' + no_motor +'.\n'

                
            values = {
                    'name' : note_text,
                    'display_type': 'line_note',
                    'move_id': result.id,
                    'sequence': count + 1,
                }
            new_note = self.env['account.move.line'].create(values)
            count = count + 2


        return result
    