from spell_list_of_class import *

class RedDice(Item):
    def __init__(self):
        cls = RedDice
        super().__init__(cls)
    name = "붉은 마나 주사위"
    showname = "붉은 마나 주사위를 하나 추가합니다."

    temp_atk = 0
    temp_def = 0

    price = 500

    def use(self, hero):
        hero.change_health(hero.health + 1 * Character.healthtodice)
        hero.bag_list.pop(hero.bag_name_list.index("붉은 마나 주사위"))
        hero.bag_name_list.remove("붉은 마나 주사위")
        printt("붉은 마나 주사위를 사용했습니다.")


class BlueDice(Item):
    def __init__(self):
        cls = BlueDice
        super().__init__(cls)
    name = "푸른 마나 주사위"
    showname = "푸른 마나 주사위를 하나 추가합니다."

    temp_atk = 0
    temp_def = 0

    price = 100

    def use(self, hero):
        hero.change_mana(hero.mana.value + 1 * Character.manatodice)
        hero.bag_list.pop(hero.bag_name_list.index("푸른 마나 주사위"))
        hero.bag_name_list.remove("푸른 마나 주사위")
        printt("푸른 마나 주사위를 사용했습니다.")