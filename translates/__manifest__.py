# -*- coding: utf-8 -*-
{
    'name': "Traducciones",

    'summary': """
        Cambio de etiquetas""",

    'description': """
        Se cambiaron etiquetas de algunos modulos como en Inventario y sales
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'l10n_mx_edi_extended'],

    # always loaded
    'data': [
        'views/product_template_translates.xml',
        'views/landed_cost.xml',
    ],
}