import pytest
from django.test import Client
from .models import Band

@pytest.fixture
def client():
    # Creates Client (browser mock-up) for tests.
    return Client()




