# -*- coding: utf-8 -*-
from odoo import models, api, fields

class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

    stock_move_activity = fields.Boolean(string='Actividad de entrega', default=False)
