# -*- coding: utf-8 -*-
from odoo import models, api, fields

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)

        values = {
                    'name' : 'Hola este es un texto jshdfsdf',
                    'display_type': 'line_note',
                    'move_id': result.id,
                }
        new_note = self.env['account.move.line'].create(values)  

        return result
    