# -*- coding: utf-8 -*-

from odoo import models, fields, SUPERUSER_ID, api, _ 

class WarrantyCard(models.Model):
    _name = 'warranty.card'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Modulo Garantías'
    
    name = fields.Char('N° de Folio', copy=False, index=True, default=lambda self: _('New'))
    stage_id = fields.Many2one('warranty.card.stage', string='Etapa', ondelete='restrict', tracking=True, copy=False, index=True, group_expand='_read_group_stage_ids',)
    requests_id = fields.Many2one('warranty.requests', string='Solicitudes de Garantía')

    kanban_state = fields.Selection([
        ('normal', 'Gris'),
        ('done', 'Verde'),
        ('blocked', 'Rojo')], string='Kanban State',
        copy=False, default='normal', required=True)
    color = fields.Integer(string='Color Index')

    stage_sign_in = fields.Selection([
    ('new', 'Nuevo'),
    ('activa', 'Activa'),
    ('inactiva', 'Inactiva')
    ], string='Etapa', related='stage_id.stage_sign_in')

    propietario = fields.Many2one('res.partner', string="Propietario")
    distribuidor = fields.Many2one('res.partner', string="Distribuidor")
    sucursal = fields.Many2one('res.partner', string="Sucursal ")
    no_serie = fields.Many2one('stock.production.lot', string='N° de Serie')
    fecha_entrega = fields.Date(string='Fecha de Entrega')
    no_motor = fields.Many2one('warranty.requests', string='No de Motor', related='requests_id.no_motor')
    modelo = fields.Many2one('warranty.requests', string='Modelo', related='requests_id.modelo')
    descripcion = fields.Html(string='Descripción')


    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].sudo().next_by_code('warranty.card') or _('New')

        if vals.get('stage_id.stage_sign_in') != 'new':
            vals['stage_id'] = self.env['warranty.card.stage'].sudo().search([('stage_sign_in', '=', 'new')]).id

        result = super(WarrantyCard, self).create(vals)
        
        return result
    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('active', '=', True)]

        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)
