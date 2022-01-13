from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from xyz_lib_a.foo import bar


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


def f():
    print(bar())

    return bar()
