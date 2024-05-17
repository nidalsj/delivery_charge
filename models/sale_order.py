from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_comments = fields.Text(string='Delivery Comments')
    delivery_terms = fields.Char(string="Delivery Terms", default=lambda self: self._get_default_delivery_terms(), readonly=True)

    #PASS DELIVERY COMMENTS FROM SALE ORDER TO INVOICE    
    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)
        for move in moves:
            move.delivery_comments = self.delivery_comments
            move.delivery_terms = self.delivery_terms
        return moves


    @api.model
    def _get_default_delivery_terms(self):
        delivery_terms = self.env['ir.config_parameter'].sudo().get_param('delivery_charge.delivery_terms', default='')
        return delivery_terms
    


    

