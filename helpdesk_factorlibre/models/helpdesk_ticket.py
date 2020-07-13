# -*- coding: utf-8 -*-
# © 2020 Alberto Esteban
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

#Imports
from odoo import models, fields, _, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
#Clases
class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    def _get_default_priority(self):
        return "1"
    
    name = fields.Char(
        string='Tittle',
        required=True,
    )
    description = fields.Html(
        string='Description',
    )
    assigned_date = fields.Datetime(
        string='Assigned Date',
        compute='_compute_assigned_date',
        store=True,
        )
    
    closed_date = fields.Datetime(string='Closed Date')
    
    priority = fields.Selection(selection=[
        ('0', _('Low')),
        ('1', _('Medium')),
        ('2', _('High')),
    ], 
    string='Priority',
    default=_get_default_priority,
    )
    ticket_number = fields.Integer(
        string='Ticket number',
    )
    user_id = fields.Many2one(
        string = "asigned to",
        comodel_name = "res.users",
        ondelete = "restrict"
    )
    user_ids = fields.Many2many(
        comodel_name='res.users',
        related='team_id.user_ids',
        string='Users')
    partner_id = fields.Many2one(
        string = "Customer",
        comodel_name = "res.partner",
        ondelete="restrict"
    )
    partner_name = fields.Char(
        string = "Customer Name",
    )
    partner_mail = fields.Char(
        string = "Customer Mail",
    )
    
    tag_ids = fields.Many2many(
        string = "Tags",
        comodel_name = "helpdesk.ticket.tag",
    )
    
    team_id = fields.Many2one(
        "helpdesk.ticket.team",
    )
    
    unattended = fields.Boolean(related='stage_id.unattended')
    
    color = fields.Integer(string='Color Index')
    
    
    @api.multi
    def assign_to_me(self):
        self.write({'user_id': self.env.user.id})
        
    @api.multi
    @api.onchange('team_id', 'user_id')
    def _onchange_dominion_user_id(self):
        if self.user_id:
            if self.user_id and self.user_ids and \
                    self.user_id not in self.user_ids:
                self.update({
                    'user_id': False
                })
                return {'domain': {'user_id': []}}
        if self.team_id:
            return {'domain': {'user_id': [('id', 'in', self.user_ids.ids)]}}
        else:
            return {'domain': {'user_id': []}}
        
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for record in self:
            partner = record.partner_id
            if partner:
                record.update({
                    'partner_name': partner.name,
                    'partner_mail': partner.email,
                })
    @api.depends('user_id')
    def _compute_assigned_date(self):
        self.assigned_date = fields.Datetime.now()
        
        
    @api.model
    def create(self,vals):
        if vals.get("partner_id") and ("partner_name" not in vals or "partner_mail" not in vals):
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals.setdefault("partner_name", partner.name)
            vals.setdefault("partner_mail", partner.email)
            
        res = super().create(vals)
        return res