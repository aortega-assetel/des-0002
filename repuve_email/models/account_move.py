# -*- coding: utf-8 -*-
from odoo.modules.module import get_resource_path
import base64

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def send_repuve(self):
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()
        template_id = self.env['ir.model.data'].xmlid_to_res_id('repuve_email.email_template_repuve', raise_if_not_found=False)
        lang = self.env.context.get('lang')
        template = self.env['mail.template'].browse(template_id)

        if template.lang:
            lang = template._render_template(template.lang, 'installed.services', self.ids[0])
        ctx = {
            'default_model': 'account.move',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'custom_layout': "repuve_email.template_repuve",
            'force_email': True,
            'model_description': "Correo REPUVE",
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
