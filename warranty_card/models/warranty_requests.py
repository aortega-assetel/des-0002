# -*- coding: utf-8 -*-
from odoo import models, api, fields, exceptions, _

class WarrantyRequests(models.Model):
    _name = 'warranty.requests'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Solicitudes de garantía'

    kanban_state = fields.Selection([
        ('normal', 'Gris'),
        ('done', 'Verde'),
        ('blocked', 'Rojo')], string='Kanban State',
        copy=False, default='normal', required=True)
    color = fields.Integer(string='Color Index')
                
    folio = fields.Many2one('warranty.card', string='Evaluaciones')
    cliente = fields.Many2one('warranty.card', string='Cliente', related='folio.propietario')
    no_serie = fields.Many2one('warranty.card', string='Modelo')
    modelo = fields.Many2one('warranty.card', string='Modelo')
    no_motor = fields.Many2one('warranty.card', string='N° de Motor')
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