class NotInRange(Exception):
    def __init__(self,message = "value not in range"):
        self.message=message
        super().__init__(self.message)
        
        
def test_range():
    a=12
    if a not in range(10,20):
        raise NotInRange
    else:
        assert True
        

