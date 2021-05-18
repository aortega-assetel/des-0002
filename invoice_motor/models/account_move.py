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
            attribute_value = ''
            for product_variant in product.attribute_line_ids:
                for attribute_line in product_variant.attribute_id.value_ids:
                    attribute = product_variant.attribute_id.name
                    attribute_value = attribute_value + ', ' + attribute_line.name
                
                
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
    