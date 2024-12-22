class Hero:
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg

    def describe(self):
        return f"{self.name} is a {self.role} with {self.dmg_type} power."

hero_mm1 = Hero("Lesley", "marksman", "attack damage", "2490", "115")
hero_fighter1 = Hero("Zilong", "fighter", "attack damage", "2689", "123")
hero_mg1 = Hero("Kagura", "mage", "magic damage", "2496", "130")
hero_ass1 = Hero("Hayabusa", "assassin", "attack damage", "2429", "117")
hero_sup1 = Hero("Diggie", "support", "magic damage", "2468", "115")

for hero in [hero_mm1, hero_fighter1, hero_mg1, hero_ass1, hero_sup1]:
    print(f"""
    {hero.name}
    {hero.role}
    {hero.dmg_type}
    {hero.health} HP
    {hero.auto_atk_dmg} basic attack damage
    {hero.describe()}
    """)