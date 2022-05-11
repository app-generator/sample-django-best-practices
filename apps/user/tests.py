import pytest

from apps.user.models import User


@pytest.mark.django_db
def test_create_user():
    data_user = {
        "username": "test_user",
        "email": "test@gmail.com",
        "password": "test_password",
    }
    
    user = User.objects.create_user(**data_user)
    
    assert data_user["username"] == user.username
    assert data_user["email"] == user.email
    
