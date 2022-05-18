# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsersBase(BaseModel):
    name: str


class Users(UsersBase):
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ScoresBase(BaseModel):
    score: int
    user_id: str


class Scores(ScoresBase):
    score_id: str
    user_name: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
