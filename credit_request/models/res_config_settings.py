# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    request_project_id = fields.Many2one(
        related='company_id.request_project_id', readonly=False,
        string='Proyecto de solicitudes de crédito')
