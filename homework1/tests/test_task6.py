import os
import src.task6 as task6

def test_word_count():
    test_file = task6.count
    
    #conforming count
    assert test_file == 127