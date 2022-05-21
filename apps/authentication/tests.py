import pytest

from django.contrib.auth import authenticate

from apps.authentication.forms import LoginForm, SignUpForm
from apps.user.models import User

# Adding a new user for fixtures
@pytest.fixture
def user():
    data_user = {
        "username": "test_user",
        "email": "test@gmail.com",
        "password": "test_password",
        }
    
    return User.objects.create_user(**data_user)

# authentication form class tests

class TestLoginForm:
    
    def test_form_is_valid(self):
        form = LoginForm(data={
            "username": "test_user",
            "password": "test_password",
        })
        
        assert form.is_valid()
    
    @pytest.mark.django_db            
    def test_login_non_existent_user(self):
        form = LoginForm(data={
            "username": "test_user",
            "password": "test_password",
        })
        
        assert form.is_valid()
        
        assert authenticate(**form.cleaned_data) is None
        
    @pytest.mark.django_db            
    def test_login(self, user):
        form = LoginForm(data={
            "username": user.username,
            "password": "test_password",
        })
        
        assert form.is_valid()
        
        assert authenticate(**form.cleaned_data) is not None    
        
    @pytest.mark.django_db            
    def test_login_with_wrong_password(self, user):
        form = LoginForm(data={
            "username": "test_user",
            "password": "test_password_wrong",
        })
        
        assert form.is_valid()
        
        assert authenticate(**form.cleaned_data) is None
        
        
class TestSignUpForm:
    
    @pytest.mark.django_db        
    def test_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "email": "test_user@yopmail.com",
            "password1": "kola1234",
            "password2": "kola1234",
        }
        
        form = SignUpForm(data=form_data)
        assert form.is_valid()
        
    @pytest.mark.django_db    
    def test_weak_password(self):
        form_data = {
            "username": "test_user",
            "email": "test_user@yopmail.com",
            "password1": "12345",
            "password2": "12345",
        }
        
        form = SignUpForm(data=form_data)
        assert not form.is_valid()
        
    @pytest.mark.django_db    
    def test_with_existing_email(self, user):
        
        form_data = {
            "username": "test_user",
            "email": user.email,
            "password1": "kola1234",
            "password2": "kola1234",
        }
        
        form = SignUpForm(data=form_data)
        assert not form.is_valid()
        
        