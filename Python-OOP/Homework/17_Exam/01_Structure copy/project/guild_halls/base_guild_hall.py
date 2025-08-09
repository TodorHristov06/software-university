from abc import ABC, abstractmethod

class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members = []

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        value = value.strip()
        if len(value) < 2 or not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Guild hall alias is invalid!")
        self._alias = value

    def calculate_total_gold(self) -> int:
        return sum(member.gold for member in self.members)

    def status(self) -> str:
        member_tags = sorted([member.tag for member in self.members])
        members_str = " *".join(member_tags) if member_tags else "N/A"
        return f"Guild hall: {self.alias}; Members: {members_str}; Total gold: {self.calculate_total_gold()}"

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass