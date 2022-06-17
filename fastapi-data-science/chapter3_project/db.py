from typing import Dict

from chapter3_project.models.users import User
from chapter3_project.models.posts import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()