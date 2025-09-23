import src.task5 as task5

def test_books_list():

    #list check
    assert isinstance(task5.fav_books, list)
    assert isinstance(task5.fav_books[:3], list)

def test_students_dict():

    #dic check
    assert isinstance(task5.student_data, dict)

