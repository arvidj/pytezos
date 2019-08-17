from unittest import TestCase

from tests import get_data
from pytezos.operation.forge import forge_operation_group


class OperationForgingTestooQESF(TestCase):

    def setUp(self):
        self.maxDiff = None
        
    def test_forge_ooQESF(self):
        expected = get_data(
            path='operations/ooQESFgttq6iVBodwbsBpPVdzWceUzG3pYuCmpygmufNRa98ntc/forged.hex')
        actual = forge_operation_group(get_data(
            path='operations/ooQESFgttq6iVBodwbsBpPVdzWceUzG3pYuCmpygmufNRa98ntc/unsigned.json'))
        self.assertEqual(expected, actual)
