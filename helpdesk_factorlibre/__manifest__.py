# -*- coding: utf-8 -*-
# © 2020 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Helpdesk Factor Libre',
    'summary': "Split first name and last name for non company partners",
    'version': '11.0.1.0.1',
    'author': "Alberto Esteban",
    'license': "AGPL-3",
    'maintainer': 'Camptocamp, Acsone',
    'category': 'Helpdesk',
    'website': 'https://odoo-community.org/',
    'depends': ['mail'],
    'data': [
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_tags_views.xml',
        'views/inherit_res_partner_views.xml',
        'views/helpdesk_ticket_stage_views.xml',
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/helpdesk_data.xml'
        ],
    'installable': True,
}
