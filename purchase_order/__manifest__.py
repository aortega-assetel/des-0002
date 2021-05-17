# -*- coding: utf-8 -*-
{
    'name': "purchase_order",

    'summary': """
        Configuraciones adicionales en modulo de ventas y contabilidad""",

    'description': """
        Campo agregado "Orden de compra"
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order.xml',
    ],
}