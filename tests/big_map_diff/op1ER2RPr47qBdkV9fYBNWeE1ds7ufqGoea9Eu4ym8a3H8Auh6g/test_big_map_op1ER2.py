from unittest import TestCase

from tests import get_data
from pytezos.michelson.contract import ContractStorage


class BigMapCodingTestop1ER2(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_op1ER2(self):    
        section = get_data(
            path='big_map_diff/op1ER2RPr47qBdkV9fYBNWeE1ds7ufqGoea9Eu4ym8a3H8Auh6g/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/op1ER2RPr47qBdkV9fYBNWeE1ds7ufqGoea9Eu4ym8a3H8Auh6g/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
