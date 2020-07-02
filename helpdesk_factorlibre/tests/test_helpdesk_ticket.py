from odoo.tests import common

class TestTicket(common.TransitionCase):
    def setUp(cls):
        super(TestTicket, cls).setUpClass()
        helpdesk_ticket = cls.env['helpdesk.ticket']
        cls.user_admin = cls.env.ref('base.user_root')
        cls.user_demo = cls.env.ref('base.user_demo')
        cls.stage_closed = cls.env.ref(
            'helpdesk_factorlibre.helpdesk_ticket_stage_done'
        )

        cls.ticket = helpdesk_ticket.create({
            'name': 'Test 1',
            'description': 'Ticket test',
        })
    
    def test_helpdesk_ticket_name(self):
        self.assertNotEquals(self.ticket.name, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a name.')