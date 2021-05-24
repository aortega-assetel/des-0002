# -*- coding: utf-8 -*-
{
    'name': "Garantías",

    'summary': """
        Garantías""",

    'description': """
        Modulo de Garantías""",

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'stock'], 

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'views/warranty_card_menu.xml',
        'views/warranty_card.xml',
        'views/warranty_card_stage.xml',
        'views/warranty_pdf.xml',
        'views/warranty_requests.xml',
        ],

}