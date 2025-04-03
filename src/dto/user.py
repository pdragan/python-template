from pydantic import BaseModel, field_validator

class LoginRequest(BaseModel, extra='ignore'):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, v):
        if v == '':
            raise ValueError('Username is required.')
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long.')
        return v

    @field_validator('password')
    def validate_password(cls, v):
        if v == '':
            raise ValueError('Password is required.')
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        return v