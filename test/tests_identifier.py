
from ..src.Identifier import Identifier


class TestIdentifier:
    
   
    
    def identifierNull(self):
        assert Identifier.validateIdentifier(" dfsdfsd") == False

    def identifierOneCharacter(self): 
        assert Identifier.validateIdentifier("A") == True 
        
    def identifierLimit(self): 
        assert Identifier.validateIdentifier("A12345") == True 
    
    def identifierBurst(self): 
        assert Identifier.validateIdentifier("A12345678") == False 
        
    def identifierStartNumber(self): 
        assert Identifier.validateIdentifier("1") == False 
        
    
    