from src.math_operation import add,substract
def test_add():
    assert add(1,2)==3
    assert add(-1,1)==0
    
def test_substract():
    assert substract(4,3)==1
    assert substract(1,1)==0
    assert substract(-1,1)==-2