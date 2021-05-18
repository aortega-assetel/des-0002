# -*- coding: utf-8 -*-
import logging

from odoo import models, api, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    request_task = fields.Boolean(string='Tarea de solicitudes de crédito', default=False)
    
    lead_id = fields.Many2one('crm.lead', string='Oportunidad')

    @api.model
    def create(self, vals):
        result = super(ProjectTask, self).create(vals)

        if result.request_task:
            result.name = '(#' + str(result.id) + ') - ' + result.name

            text = '''<div style="margin: 0px; padding: 0px;">
                <p style="margin: 0px; padding: 0px; font-size: 13px;">
                    Buen día,
                    <br/><br/>
                    Se ha creado una nueva tarea de solicitudes de crédito:
                    <br/><br/>
                    Proyecto: ''' + str(result.project_id.name) + '''
                    <br/>
                    Nombre: ''' + str(result.name) + '''
                    <br/>
                    Oportunidad: ''' + str(result.lead_id.name) + '''
                    <br/>
                    Cliente: ''' + str(result.partner_id.name) + '''
                    <br/>
                    Descripción: ''' + str(result.description) + '''
                    <br/><br/>
                    Saludos.
                </p>'''

            for line in result.project_id.users_to_notify:
                result.message_post(body=text, partner_ids=[line.partner_id.id])
        
        return result

    def action_view_lead(self):
        action = self.env.ref('project.act_project_project_2_project_task_all').read()[0]

        if self.lead_id:
            action['views'] = [(self.env.ref('project.view_task_form2').id, 'form')]
            action['res_id'] = self.lead_id.id
        return action