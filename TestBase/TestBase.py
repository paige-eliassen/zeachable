import os
import unittest
import logging

class TestBase(unittest.TestCase):

    @classmethod
    def setUp(self):

        if TestBase.setup_done:
            return
        TestBase.setup_done = True

        # here i have set runtime variables. configure into a try / except for remote run that is parameterize if had
        # more time

        self.run_type = 'local'
        self.project = os.environ["project"]
        self.env = 'test'







