from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_comments = fields.Text(string='Delivery Comments')
    delivery_terms = fields.Text(string='Delivery Terms')
    