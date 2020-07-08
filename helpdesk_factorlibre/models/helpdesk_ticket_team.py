from odoo import api, fields, models


class HelpdeskTeam(models.Model):

    _name = 'helpdesk.ticket.team'
    _description = 'Helpdesk Ticket Team'

    name = fields.Char(
        string='Name',
    )
    
    members = fields.Many2one(
        string='Members'
    )
    
    active = fields.Boolean(default=True)
    
