import pytest
from userreg import UserRegistration

@pytest.fixture
def user():
    return UserRegistration()

def test_password_validation(user):
    user.password_validation('Abcd$1234')
    assert user.password == 'Abcd$1234'

def test_invalid_password_validation(user):
    with pytest.raises(ValueError):
        user.password_validation('xjk2')

def test_firstname_validation(user):
    user.firstname_validation('Joshi')
    assert user.firstname == 'Joshi'

def test_invalid_firstname_validation(user):
    with pytest.raises(ValueError):
        user.firstname_validation('oshi')

def test_lastname_validation(user):
    user.lastname_validation('Karan')
    assert user.lastname == 'Karan'

def test_invalid_lastname_validation(user):
    with pytest.raises(ValueError):
        user.lastname_validation('Ka')

# Add similar corrections to other test cases...
