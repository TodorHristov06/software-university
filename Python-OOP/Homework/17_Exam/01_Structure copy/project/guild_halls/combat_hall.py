from project.guild_halls.base_guild_hall import BaseGuildHall

class CombatHall(BaseGuildHall):
    @property
    def max_member_count(self): # type: ignore
        return 3

    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if member.skill_level >= min_skill_level_value and member.role == "Warrior":
                member.gold += 300