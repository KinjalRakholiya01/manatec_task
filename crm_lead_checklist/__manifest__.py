# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CRM Lead Checklist',
    'version': '1.1',
    'summary': 'CRM Lead Checklist',
    'sequence': 1,
    'description': """
        CRM
        ====================
        - Checklist Configure in User
        - Auto Create Checklist in Every Lead as per User's Checklist

    """,
    'category': 'CRM',
    'website': '',
    'images': [],
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/crm_lead_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'assets': {
    },
    'license': 'LGPL-3',
}
