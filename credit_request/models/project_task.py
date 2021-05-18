# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    request_task = fields.Boolean(string='Tarea de solicitudes de crédito', default=False)
    
    lead_id = fields.Many2one('crm.lead', string='Oportunidad')
    attached_document = fields.Many2many('ir.attachment', string='Documento en extenso')

    @api.model
    def create(self, vals):
        result = super(ProjectTask, self).create(vals)

        if result.request_task:
            result.name = '(#' + str(result.id) + ') - ' + result.name
        return result

    def action_view_lead(self):
        action = self.env.ref('project.act_project_project_2_project_task_all').read()[0]

        if self.lead_id:
            action['views'] = [(self.env.ref('project.view_task_form2').id, 'form')]
            action['res_id'] = self.lead_id.id
        return action