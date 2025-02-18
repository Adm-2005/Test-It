# external imports
import pytz
import datetime as dt
from pydantic import Field 
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

# internal imports
from api.db.base_models import Serialization
from api.db.pydantic_objectid import PydanticObjectId

class User(Serialization):
    id: Optional[PydanticObjectId] = Field(alias='_id', default=None)
    first_name: Optional[str] = Field(default='')
    last_name: Optional[str] = Field(default='')
    email: str 
    username: str 
    password_hash: str
    created_at: dt.datetime = Field(default=lambda: dt.datetime.now(tz=pytz.timezone('Asia/Kolkata')))

    def get_password_hash(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)