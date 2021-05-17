# -*- coding: utf-8 -*-
{
    'name': "Facturas MBMotos",

    'summary': """
        Facturas MBMotos""",

    'description': """
        Facturas MBMotos
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','stock'],

     # always loaded
    'data': [
        'views/stock_production_lot.xml',
        ],
}