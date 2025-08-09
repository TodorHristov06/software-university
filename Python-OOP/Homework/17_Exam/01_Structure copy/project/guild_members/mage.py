from project.guild_members.base_guild_member import BaseGuildMember

class Mage(BaseGuildMember):
    def __init__(self, tag: str, gold: int):
        super().__init__(tag, gold, "Mage", 1)

    def practice(self):
        self.skill_level = min(self.skill_level * 2, 10)