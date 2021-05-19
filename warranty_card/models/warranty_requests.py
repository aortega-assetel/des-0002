# -*- coding: utf-8 -*-
from odoo import models, api, fields, exceptions, _

class WarrantyRequests(models.Model):
    _name = 'warranty.requests'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Solicitudes de garantía'

    name = fields.Char('N° de Solicitud', copy=False, index=True, default=lambda self: _('New'))
    kanban_state = fields.Selection([
        ('normal', 'Gris'),
        ('done', 'Verde'),
        ('blocked', 'Rojo')], string='Kanban State',
        copy=False, default='normal', required=True)
    color = fields.Integer(string='Color Index')
                
    folio = fields.Many2one('warranty.card', string='Evaluaciones')
    cliente = fields.Char(string='Cliente')
    no_serie = fields.Many2one('warranty.requests', string='Modelo')
    modelo = fields.Many2one('warranty.requests', string='Modelo')
    no_motor = fields.Many2one('warranty.requests', string='N° de Motor')
    date_sold = fields.Date(string='Fecha de compra')
    anio_motocicleta = fields.Integer(string='Año Motocicleta')
    kilometraje = fields.Integer(string='Kilometraje')
    descripcion = fields.Html(string='Descripción')
    date = fields.Date(string='Fecha')

    stage_sign_in = fields.Selection([
        ('new', 'Nuevo'),
        ('proceso', 'Proceso'),
        ('cerrado', 'Cerrado')
    ], string='Etapa')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].sudo().next_by_code('warranty.requests') or _('New')
        result = super(WarrantyRequests, self).create(vals)
        
        return result