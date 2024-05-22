from odoo import fields, models, tools, api


class SaleSqlView(models.Model):
    _name = "sale.sql.view"
    _description = "Sale Order SQL View"
    _auto = False

    sale_number = fields.Char(string='Sale Number')
    order_date = fields.Datetime(string='Date & Time')
    customer_name = fields.Char(string='Customer Name')
    total_amount = fields.Monetary(string='Total Amount')
    currency_id = fields.Many2one('res.currency', string="Currency")

    
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW sale_sql_view AS (
                SELECT row_number() OVER() as id,
                    so.name as sale_number,
                    rp.name as customer_name,
                    so.date_order as order_date,
                    so.amount_total as total_amount,
                    rc.id as currency_id     
                FROM
                    sale_order so
                    JOIN res_partner rp ON so.partner_id = rp.id    
                    JOIN res_currency rc ON so.currency_id = rc.id    
            )
        """)

