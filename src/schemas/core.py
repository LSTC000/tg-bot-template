from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CoreModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DateTimeMixin(BaseModel):
    created_at: datetime = Field(..., description="DateTime of create record")
    updated_at: datetime = Field(..., description="DateTime of update record")
