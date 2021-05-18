# -*- coding: utf-8 -*-
from odoo import models, api, fields

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)
        count = 0
        for line in result.invoice_line_ids:
            line.sequence = count
            product = self.env['product.template'].search([('id', '=', line.product_id.id)])
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

        return result
    