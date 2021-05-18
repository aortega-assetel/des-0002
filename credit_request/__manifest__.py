# -*- coding: utf-8 -*-
{
    'name': "Solicitudes de crédito",

    'summary': """
        Solicitudes de crédito""",

    'description': """
        Solicitudes de crédito para modúlo CRM y Proyecto
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'project', 'sale_management', 'contacts', 'sale_timesheet'],

    # always loaded
    'data': [
        'views/project_task.xml',
        'views/crm_lead.xml',
        'views/crm_stage.xml',
        'views/res_config_settings.xml',
    ],
}
