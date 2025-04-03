import pytest
from pydantic_core._pydantic_core import ValidationError

from src.dto.user import LoginRequest


def test_success() -> None:
    req = LoginRequest(
        username="testuser",
        password="testpassword"
    )

    assert req.username == "testuser"
    assert req.password == "testpassword"

@pytest.mark.parametrize(
    'username, password, expected_error',
    [
        ('ab', 'securepassword', 'Username must be at least 3 characters long.'),  # Too short username
        ('testuser', 'short', 'Password must be at least 8 characters long.'),  # Too short password
    ],
)
def test_create_user_request(username: str, password: str, expected_error: str) -> None:
    with pytest.raises(ValidationError) as excinfo:
        LoginRequest(username=username, password=password)
    assert expected_error in str(excinfo.value)