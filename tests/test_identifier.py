import sys

import pytest

sys.path.append('src/')
from Identifier import Identifier


class TestIdentifier:
    
    @pytest.fixture(scope='module')
    def setUp(self):
        obj = Identifier()
        return obj
    
    def test_identifierNull(self, setUp):
        assert setUp.validateIdentifier(" dfsdfsd") == False

    def test_identifierOneCharacter(self, setUp): 
        assert setUp.validateIdentifier("A") == True 
        
    def test_identifierLimit(self, setUp): 
        assert setUp.validateIdentifier("A12345") == True 
    
    def test_identifierBurst(self, setUp): 
        assert setUp.validateIdentifier("A12345678") == False 
        
    def test_identifierStartNumber(self, setUp): 
        assert setUp.validateIdentifier("1") == False 
        
    
    