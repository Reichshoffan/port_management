# -*- coding: utf-8 -*-
{
    'name': "Port MLC",
    'application': True,
    'installable': True,

    'summary': "Plateforme de gestion des cargaisons",

    'description': """
Long description of module's purpose
    """,

    'author': "NGZ Consulting",
    'website': "https://www.ngzconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/port_cargaison_sequence.xml',
        'reports/depart_cargaison_template.xml',
        'reports/depart_cargaison_action.xml',
        'views/move_views.xml',
        'views/type_marchandise_views.xml',
        'views/type_cargaison_views.xml',
        #'views/depart_views.xml',
        'views/cargaison_views.xml',
        'views/gps_views.xml',
        'views/mode_transport_views.xml',
        'views/product_template_views.xml',
        'views/menuitems.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}

