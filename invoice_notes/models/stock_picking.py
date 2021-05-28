from odoo import _, api, fields, models, tools

class StockPicking(models.Model):
    _inherit  = 'stock.picking'

    stock_activity_id = fields.Many2one('mail.activity', string='Actividad de demo')
    stock_finish_date = fields.Datetime("Fecha finalización entrega")
