# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    aduana = fields.Char(string='Aduana')



    
        