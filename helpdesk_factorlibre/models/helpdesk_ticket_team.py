from odoo import api, fields, models


class HelpdeskTeam(models.Model):

    _name = 'helpdesk.ticket.team'
    _description = 'Helpdesk Ticket Team'

    name = fields.Char(
        string='Name',
    )
    team_id = fields.Integer(
        string='Team Id',
    )
    
    