from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.warrior import Warrior
from project.guild_members.mage import Mage

class GuildMaster:
    def __init__(self):
        self.members = []
        self.guild_halls = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int) -> str:
        if member_type not in ["Warrior", "Mage"]:
            raise ValueError("Invalid member type!")
        
        if any(member.tag == member_tag for member in self.members):
            raise ValueError(f"{member_tag} has already been added!")
        
        if member_type == "Warrior":
            self.members.append(Warrior(member_tag, member_gold))
        else:
            self.members.append(Mage(member_tag, member_gold))
        
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str) -> str:
        if guild_hall_type not in ["CombatHall", "MagicTower"]:
            raise ValueError("Invalid guild hall type!")
        
        if any(hall.alias == guild_hall_alias for hall in self.guild_halls):
            raise ValueError(f"{guild_hall_alias} has already been added!")
        
        if guild_hall_type == "CombatHall":
            self.guild_halls.append(CombatHall(guild_hall_alias))
        else:
            self.guild_halls.append(MagicTower(guild_hall_alias))
        
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str) -> str:
        hall = next((h for h in self.guild_halls if h.alias == guild_hall_alias), None)
        if not hall:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")
        
        member = next((m for m in self.members if m.role == member_type), None)
        if not member:
            raise ValueError("No available members of the type!")
        
        if len(hall.members) >= hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."
        
        self.members.remove(member)
        hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall, sessions_number: int) -> str:
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()
        
        total_skill = sum(member.skill_level for member in guild_hall.members)
        return f"{guild_hall.alias} members have {total_skill} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall, member_tag: str) -> str:
        member = next((m for m in guild_hall.members if m.tag == member_tag), None)
        if not member or member.skill_level == 10:
            return "The unassignment process was canceled."
        
        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int) -> str:
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)
        
        sorted_halls = sorted(
            self.guild_halls,
            key=lambda h: (-len(h.members), h.alias)
        )
        
        status_lines = [
            f">>>{hall.status()}"
            for hall in sorted_halls
        ]
        
        return (
            "<<<Guild Updated Status>>>\n"
            f"Unassigned members count: {len(self.members)}\n"
            f"Guild halls count: {len(self.guild_halls)}\n"
            + "\n".join(status_lines)
        )