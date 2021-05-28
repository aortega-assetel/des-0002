# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields

class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

    stock_ending_activity = fields.Boolean(string='Actividad finalización Entrega', default=False)
