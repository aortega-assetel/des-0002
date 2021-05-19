# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, api, fields
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)

class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    cuenta_cargo = fields.Many2one('account.account', string='Cuenta cargo')
    cuenta_abono = fields.Many2one('account.account', string='Cuenta abono')
    journal = fields.Many2one('account.journal', string='Diario contable')


    def button_mark_done(self):
        result = super(MrpProduction, self).button_mark_done()
        if self.state == 'done':
            for line in self.workorder_ids:
                cost = line.duration * (line.workcenter_id.costs_hour/60)
                move_lines = [
                            (0, 0, {
                                'account_id' : line.workcenter_id.cuenta_abono.id,
                                'name': self.name +  ' - Costo de producción',
                                'credit': cost,
                                
                            }),
                            (0, 0, {
                                'account_id' : line.workcenter_id.cuenta_cargo.id,
                                'name': self.name +  ' - Costo de producción',
                                'debit': cost,
                            })
                        ]
                values = {
                    'ref' : self.name +  ' - Costo de producción',
                    'date' : datetime.today().strftime('%d/%m/%Y'),
                    'journal_id' : line.workcenter_id.journal.id,
                    'line_ids' : move_lines
                    }
                asiento = self.env['account.move'].create(values)
                asiento.action_post()
            
        return result
