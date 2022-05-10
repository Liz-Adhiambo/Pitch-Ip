import unittest
from pitchblog.models import Post

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Post(1,'Interview pitch','2022-05-10', 'this is an interview pitch')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Post))