import unittest

class TestHelpdeskTicket(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestHelpdeskTicket, cls).setUpClass()
        
        helpdesk_ticket = cls.env['helpdesk.ticket']
        user_admin = cls.env.ref('base.admin')
        user_demo = cls.env.ref('base.admin')

        tickets = cls.env['res.users']
        cls.ticket_test = tickets.create({
            'name': 'Test 1',
            'description': 'Ticket test',
        })
        
    def test_helpdesk_ticket_name(self):
        self.assertNotEquals(self.ticket.name, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a name.')
