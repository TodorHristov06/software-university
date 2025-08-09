from abc import ABC, abstractmethod

class BaseGuildMember(ABC):
    def __init__(self, tag: str, gold: int, role: str, skill_level: int):
        self.tag = tag
        self.gold = gold
        self.role = role
        self.skill_level = skill_level

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        if not value.isalnum():
            raise ValueError("Tag must contain only letters and digits!")
        self._tag = value

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        if value < 0:
            raise ValueError("Gold must be a non-negative integer!")
        self._gold = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if not value.strip():
            raise ValueError("Role cannot be empty!")
        self._role = value

    @property
    def skill_level(self):
        return self._skill_level

    @skill_level.setter
    def skill_level(self, value):
        if not 1 <= value <= 10:
            raise ValueError("Skill level is out of range!")
        self._skill_level = value

    @abstractmethod
    def practice(self):
        pass