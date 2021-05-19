# -*- coding: utf-8 -*-
{
    'name': "Asiento contable por hora",

    'summary': """
        Asiento contable por hora""",

    'description': """
        Asiento contable por hora
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp'],

     # always loaded
    'data': [
        'views/mrp_workcenter.xml',
        ],
}