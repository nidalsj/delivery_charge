{
    'name': 'Sale Order Delivery Charge',
    'category': 'Sales',
    'summary': 'Manage Sale Orders',
    'depends': ['sale','account'],
    'license': 'LGPL-3',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/res_config_settings_views.xml',
        'views/sale_sql_view.xml',
    ],


    'installable': True,
    'auto_install': False,
    'application': False,
}
