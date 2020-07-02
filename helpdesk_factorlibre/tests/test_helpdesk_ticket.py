import unittest

class TestHelpdeskTicket(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestHelpdeskTicket, cls).setUpClass()
        helpdesk_ticket = cls.env['helpdesk.ticket']
        cls.user_admin = cls.env.ref('base.user_root')
        cls.user_demo = cls.env.ref('base.user_demo')
        cls.stage_closed = cls.env.ref(
            'helpdesk_mgmt.helpdesk_ticket_stage_done'
        )

        cls.ticket = helpdesk_ticket.create({
            'name': 'Test 1',
            'description': 'Ticket test',
        })
        
    def test_helpdesk_ticket_name(self):
        super(self.assertNotEquals(self.helpdesk.ticket.name, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a name.'))