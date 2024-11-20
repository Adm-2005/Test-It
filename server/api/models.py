import re
import torch
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from api.utils.objectId import PydanticObjectId
from werkzeug.security import check_password_hash, generate_password_hash

class Session(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    project_id: Optional[PydanticObjectId] = Field(None)
    name: str
    scope: str
    context: Optional[str] = Field(default="")
    inputImages: List[str] = Field(default_factory=list)
    inputCode: Optional[str] = Field(default="")
    output: Optional[str]
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(tz=datetime.timezone.utc))
    updated_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(tz=datetime.timezone.utc))

    def set_image(self, images: List[torch.Tensor]):
        for image in images:
            if not isinstance(image, torch.Tensor):
                raise ValueError("All images must be torch.Tensor objects")
            flattened_image = image.flatten().tolist()
            self.inputImages.append(flattened_image)

    def get_image_tensor(self) -> List[torch.Tensor]:
        return [torch.Tensor(image) for image in self.inputImages]

    @property
    def slug(self):
        cleaned_name = re.sub(r'[^a-zA-Z0-9\s-]', '', self.name)
        slug = cleaned_name.lower().replace(" ", "-").strip("-")
        return slug

    def update_timestamp(self):
        self.updated_at = datetime.datetime.now(tz=datetime.timezone.utc)

    def to_json(self):
        return jsonable_encoder(self)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)
        return data

class Project(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    user_id: Optional[PydanticObjectId] = Field(None)
    name: str
    organization: Optional[str] = Field(default="")
    sessions: List[PydanticObjectId] = Field(default_factory=list)
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(tz=datetime.timezone.utc))
    updated_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(tz=datetime.timezone.utc))

    @property
    def slug(self):
        cleaned_name = re.sub(r'[^a-zA-Z0-9\s-]', '', self.name)
        slug = cleaned_name.lower().replace(" ", "-").strip("-")
        return slug

    def update_timestamp(self):
        self.updated_at = datetime.datetime.now(tz=datetime.timezone.utc)

    def to_json(self):
        return jsonable_encoder(self)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)
        return data

class User(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    full_name: str
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
    username: str = Field(..., min_length=3, max_length=30)
    hashed_password: Optional[str] = Field(None)
    projects: List[PydanticObjectId] = Field(default_factory=list)

    def set_password(self, password: str):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.hashed_password, password)

    def to_json(self, exclude_password=True):
        user_data = jsonable_encoder(
            self,
            custom_encoder={PydanticObjectId: str}, 
        )
        if exclude_password:
            user_data.pop('hashed_password', None)
        return user_data
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)
        return data