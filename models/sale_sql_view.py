from odoo import fields, models, tools

class SaleSqlView(models.Model):
    _name = "sale.sql.view"
    _description = "Sale Order SQL View"
    _auto = False

    sale_number = fields.Char(string='Sale Number')
    order_date = fields.Datetime(string='Date & Time')
    customer_name = fields.Char(string='Customer Name')
    total_amount = fields.Monetary(string='Total Amount')
    total_volume = fields.Float(string='Total Volume')
    total_quantity = fields.Float(string='Total Quantity')
    currency_id = fields.Many2one('res.currency', string="Currency")
    user_name = fields.Char(string='Salesperson')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'sale_sql_view')
        self._cr.execute("""
            CREATE OR REPLACE VIEW sale_sql_view AS (
                SELECT 
                    row_number() OVER() as id,
                    so.name as sale_number,
                    rp.name as customer_name,
                    so.date_order as order_date,
                    so.amount_total as total_amount,
                    ru.login as user_name,
                    SUM(sol.product_uom_qty) as total_quantity,
                    SUM(pt.volume * sol.product_uom_qty) as total_volume,
                    so.currency_id as currency_id
                FROM
                    sale_order so
                    JOIN res_partner rp ON so.partner_id = rp.id
                    JOIN res_currency rc ON so.currency_id = rc.id
                    JOIN res_users ru ON so.user_id = ru.id
                    JOIN sale_order_line sol ON sol.order_id = so.id
                    JOIN product_product pp ON sol.product_id = pp.id
                    JOIN product_template pt ON pp.product_tmpl_id = pt.id
                GROUP BY
                    so.name, rp.name, so.date_order, so.amount_total, rc.id, ru.login, so.currency_id
            )
        """)

