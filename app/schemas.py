from pydantic import BaseModel, ConfigDict, Field


class RegisterRequest(BaseModel):
    org_name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)


class LoginRequest(BaseModel):
    org_name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class RefreshRequest(BaseModel):
    refresh_token: str = Field(..., min_length=1)


class RoomCreateRequest(BaseModel):
    name: str = Field(..., min_length=1)
    capacity: int = Field(..., gt=0)
    hourly_rate_cents: int = Field(..., ge=0)


class BookingCreateRequest(BaseModel):
    room_id: int = Field(..., gt=0)
    start_time: str = Field(..., min_length=1)
    end_time: str = Field(..., min_length=1)