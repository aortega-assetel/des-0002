# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    cuenta_cargo = fields.Many2one('account.account', string='Cuenta cargo')
    cuenta_abono = fields.Many2one('account.account', string='Cuenta abono')



    
        