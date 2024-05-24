from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_selected = fields.Boolean(string="Is Selected")
