from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    delivery_terms = fields.Char(string="Delivery Terms", config_parameter = 'delivery_charge.delivery_terms')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        delivery_terms = self.env['ir.config_parameter'].sudo().get_param('delivery_charge.delivery_terms', default='')
        res.update(
            delivery_terms=delivery_terms,
        )
        return res

