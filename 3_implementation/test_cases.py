# from graph import *
from analysis import get_ps, top_performer, average, fail
import pytest

ps = get_ps()


@pytest.fixture
def s():
    return get_ps(99003655)


def test_student(s):
    
    assert s.average() == [[8.1, 15.7, 23.5, 30.8, 38.8, 46.2], [8.0, 16.1, 23.9, 31.9, 39.2, 47.0], [
        7.5, 15.9, 23.9, 31.4, 39.4, 47.0], [8.6, 16.9, 24.8, 32.6, 39.2, 47.1]]

    assert s.fail() == [[10, 8, 9, 9, 9, 8], [10, 9, 7, 9, 8, 7], [
        7, 9, 8, 7, 9, 7], [10, 7, 9, 8, 9, 7]]


def test_faculty(f):
    assert f.average() == [[8.1, 15.7, 23.5, 30.8, 38.8, 46.2], [8.0, 16.1, 23.9, 31.9, 39.2, 47.0], [
        7.5, 15.9, 23.9, 31.4, 39.4, 47.0], [8.6, 16.9, 24.8, 32.6, 39.2, 47.1]]
    assert f.top_performer() == [53, 52, 48, 47, 46]
    assert f.get_ps() == ['ashish.pareek@ltts.com', 'lalit.bhardwaj@ltts.com', 'ashish.nayak@ltts.com', 'prashantsudhir.bagal@ltts.com', 'aakarsh.mehta@ltts.com', 'yash.jhajharia@ltts.com',
                            'manzar.hussain@ltts.com', 'digendrakumar.sahu@ltts.com', 'ankitkumar.yadav@ltts.com', 'manu.nadar@ltts.com']
