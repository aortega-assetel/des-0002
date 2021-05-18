# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields, exceptions

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_stage = fields.Boolean(string='Etapa de solicitud de crédito', default=False, related='stage_id.request_stage')

    def _compute_request_ids(self):
        #Se cuentan todos las solicitudes de crédito de la oportunidad actual#
        for reg in self:
            request_count = reg.env['project.task'].search_count([('lead_id', '=', reg.id), ('request_task', '=', True)])
            reg.update({
                'request_task_count': request_count,
            })

    request_task_count = fields.Integer(string='request count', compute='_compute_request_ids')
    request_task_ids = fields.One2many('project.task', 'lead_id', string='Solicitudes de crédito')


    def new_request(self):
        if self.partner_id:

            action = self.env.ref('credit_request.get_project_task_request_view').read()[0]
            action['views'] = [(self.env.ref('credit_request.project_task_form_from_crm').id, 'form')]
            action['context'] = {'default_name': 'SOLICITUD DE CRÉDITO', 'default_project_id': self.company_id.request_project_id.id,
            'default_user_id': self.company_id.request_project_id.user_id.id, 'default_partner_id': self.partner_id.id,
            'default_lead_id': self.id, 'default_request_task': True}
            action['target'] = 'new'
            return action

        else:
            raise exceptions.ValidationError('Necesitas registrar un cliente')


    def action_view_task_request(self):
        action = self.env.ref('credit_request.get_project_task_request_view').read()[0]

        solicitudes = self.mapped('request_task_ids')

        if len(solicitudes) > 1:
            action['domain'] = [('id', 'in', solicitudes.ids), ('request_task', '=', True)]
            action['views'] = [(self.env.ref('credit_request.project_task_tree_from_crm').id, 'tree'), (self.env.ref('credit_request.project_task_form_from_crm').id, 'form')]
        elif solicitudes:
            action['views'] = [(self.env.ref('credit_request.project_task_form_from_crm').id, 'form')]
            action['res_id'] = solicitudes.id
        return action
