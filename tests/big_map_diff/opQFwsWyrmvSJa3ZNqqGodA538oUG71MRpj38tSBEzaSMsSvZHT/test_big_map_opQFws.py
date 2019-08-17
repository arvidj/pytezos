from unittest import TestCase

from tests import get_data
from pytezos.michelson.contract import ContractStorage


class BigMapCodingTestopQFws(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opQFws(self):    
        section = get_data(
            path='big_map_diff/opQFwsWyrmvSJa3ZNqqGodA538oUG71MRpj38tSBEzaSMsSvZHT/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opQFwsWyrmvSJa3ZNqqGodA538oUG71MRpj38tSBEzaSMsSvZHT/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
