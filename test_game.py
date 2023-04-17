import Game
def test_1(): 
    val = [3, 6, 3, 7, 10, 8, 1, 10, 10, 9, 0, 7, 3, 4, 4, 10, 9, 0]
    result = Game.Play(val)
    assert result == 155
def test_2(): 
    val = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    result = Game.Play(val)
    assert result == 300
def test_3(): 
    val = [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6]
    result = Game.Play(val)
    assert result == 133

