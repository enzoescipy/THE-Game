
from item_list_of_class import *


class Slimebrain:

    @classmethod
    def slimebrain1(cls,monster_instance): # monster_instance에는 몬스터 인스턴스를 넣으세요.
        temp_spell_list = []

        temp_spell_list.append(monster_instance.use_spell('물컹거리기'))
        temp_spell_list.append(monster_instance.use_spell('막기'))
        if monster_instance.mana_dice >= len(monster_instance.use_spell('집어삼키기').blue_dice_list):
            temp_spell_list.append(monster_instance.use_spell('집어삼키기'))
        else:
            temp_spell_list.append(monster_instance.use_spell('물컹거리기'))

        return temp_spell_list
    @classmethod
    def slimeavailbrain1(cls,monster_instance):
        for i in range(len(monster_instance.spell_use_list)):
            monster_instance.spell_use_list[i].avail_all("red")
            monster_instance.spell_use_list[i].avail_all("blue")
            monster_instance.spell_use_list[i].avail_all("green")


class Stone_golembrain:

    @classmethod
    def stone_golembrain1(cls,monster_instance):
        temp_spell_list = []

        temp_spell_list.append(monster_instance.use_spell('돌벽 세우기'))
        temp_spell_list.append(monster_instance.use_spell('내려찍기'))
        temp_spell_list.append(monster_instance.use_spell('돌벽 세우기'))
        if monster_instance.mana_dice >= len(monster_instance.use_spell('지진파 발산').blue_dice_list):
            temp_spell_list.append(monster_instance.use_spell('지진파 발산'))
        else:
            temp_spell_list.append(monster_instance.use_spell('돌벽 세우기'))

        return temp_spell_list

    @classmethod
    def stone_golemavailbrain1(cls, monster_instance):
        for i in range(len(monster_instance.spell_use_list)):
            monster_instance.spell_use_list[i].avail_all("red")
            monster_instance.spell_use_list[i].avail_all("blue")
            monster_instance.spell_use_list[i].avail_all("green")

##test##
