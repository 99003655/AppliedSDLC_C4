from analysis import*
import pytest

data = pd.read_excel("presurvey.xlsx")


def test_case1():
    assert average() == [37.1333333, 37.1333333, 37.13333333, 34.46666667]


def test_case2():
    assert minimum() == [37.13333333, 37.133333333, 37.13333333, 34.4666667]
    pass 


def test_case3():
    assert average() == [7, 9, 8, 1, 2, 5]
    pass


def test_case4():
    assert top_performer() == [5.8, 6.2, 7.5, 8.2, 3.7, 7.7]
    pass


def test_case5():
    assert fail() == [5.2, 6.4, 7.0, 8.6, 7.7, 3.5]
    pass


def test_case6():
    assert get_PSno() == ['99003655', '99003706', '99003708', '99003718', '99003608'] 
    pass

