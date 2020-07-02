# -*- coding: utf-8 -*-
# © 2020 Alberto Esteban
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

#Imports
from odoo import models, fields, _

#Clases
class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    
    name = fields.Char(
        string='Tittle',
    )
    description = fields.Text(
        string='Description',
    )
