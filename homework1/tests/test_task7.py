# test_task7.py
import os
import src.task7 as task7

def test_plot(tmp_path):
    output_file = tmp_path
    result = task7.plot(str(output_file))
    
    # file path check
    assert result == str(output_file)

    # file check
    assert os.path.exists(result)

    # file not empty
    assert os.path.getsize(result) > 0
