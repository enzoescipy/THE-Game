hero = Character("hero", 400, 800, 3)
hero.add_spell(BloodShield)
hero.add_spell(BloodSpear)
hero.add_spell(WeakenGas)
hero.add_spell(RedPoisonSplay)
hero.add_spell(CausingBleeding)

hero.add_spell(ArcaneShield)
hero.add_spell(ArcaneArrow)
hero.add_spell(ArcaneAmplify)
hero.add_spell(ManaBurst)
hero.add_spell(Overflow)

hero.add_spell(ThrowGreenDice)
hero.add_spell(ManaCirculation)
hero.add_spell(LowClassEarthSpiritsEmploy)

hero.add_spell(OwnerKick)

slime1 = Character("슬라임1", 15, 15, 3)
slime2 = Character("슬라임2", 15, 15, 3)
monsterlist = [slime1, slime2]

for i in range(len(monsterlist)):
    monsterlist[i].add_spell(SlimeGuard)
    monsterlist[i].add_spell(SlimeJump)
    monsterlist[i].add_spell(SlimePowerJump)

self.printt('주사위 마법사의 모험에 오신것을 환영합니다.')
self.printt('작은 슬라임 이 전투를 걸어왔다!')
self.printt('마법사의 붉은 피와 푸른 마나가 마력을 담은 주사위의 형상을 이루기 시작하였다.')
self.printt('마법사의 두 눈은 상대의 체력과 기력/마나를 주사위의 형태로 파악해내기 시작하였다.')

self.printt('')

Store.Open_Store(hero, self)

while (Fight.fight_end == False):
    monster_brainlist = [Slimebrain.slimebrain1, Slimebrain.slimebrain1]
    monster_availbrainlist = [Slimebrain.slimeavailbrain1, Slimebrain.slimeavailbrain1]
    Fight.big_fight(hero, monsterlist, monster_brainlist, monster_availbrainlist, self)
self.printt('')

self.printt('전투 보상: 1 붉은 마력 주사위, 5 푸른 마력 주사위.')
hero.change_health(hero.health + 1 * Character.healthtodice)
hero.change_mana(hero.mana.value + 5 * Character.manatodice)

Store.Open_Store(hero, self)

#########################################################################################################
stone_golem = Character("스톤 골렘", 50, 30, 4)
monsterlist = [stone_golem]

for i in range(len(monsterlist)):
    monsterlist[i].add_spell(StoneGolemBoom)
    monsterlist[i].add_spell(StoneGolemWall)
    monsterlist[i].add_spell(StoneGolemPowerBoom)

Fight.clear_all(hero, monsterlist)

self.printt('')
self.printt('강력한 스톤 골렘이 전투를 걸어왔다!')

self.printt('')
while (Fight.fight_end == False):
    monster_brainlist = [Stone_golembrain.stone_golembrain1]
    monster_availbrainlist = [Stone_golembrain.stone_golemavailbrain1]
    Fight.big_fight(hero, monsterlist, monster_brainlist, monster_availbrainlist, self)
self.printt('')
