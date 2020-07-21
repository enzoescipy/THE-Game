from monster_algorithm import *

class Fight:

    hero_using_manadice_list = []
    hero_using_healthdice_list = []
    hero_using_green_list = []

    nTurn = -1

    fight_end = False #전투 종료 여부

    @classmethod
    def clear_all(cls, hero, monsterlist):
        cls.clear_nomal_all(hero, monsterlist)
        cls.clear_character_all(hero, monsterlist)
        cls.clear_turn_all(hero, monsterlist)
        cls.clear_action_all(hero, monsterlist)
        cls.clear_observer_all()
        #cls.Victory = False

    @classmethod
    def clear_nomal_all(cls, hero, monsterlist): #사용할 변수들을 초기화하는 메서드.

        hero.spell_use_list_initialize()
        hero.atk_initialize()
        hero.fault_initialize()
        hero.death_initialize()

        for i in range(len(monsterlist)):
            monsterlist[i].spell_use_list_initialize()
            monsterlist[i].atk_initialize()
            monsterlist[i].fault_initialize()
            monsterlist[i].death_initialize()

        cls.hero_using_manadice_list = []
        cls.hero_using_healthdice_list = []
        cls.hero_using_green_list = []

        cls.fight_end = False
    @classmethod
    def clear_character_all(cls, hero, monsterlist):
        hero.atk_bool = True
        hero.fault_bool = False
        hero.death = False
        hero.act_point = hero.max_act_point
        hero.spell_use_list = []
        hero.buff_list = []
        for i in range(len(monsterlist)):
            monsterlist[i].act_point = monsterlist[i].max_act_point
            monsterlist[i].spell_use_list = []
            monsterlist[i].buff_list = []
            monsterlist[i].atk_bool = True
            monsterlist[i].fault_bool = False
            monsterlist[i].death = False

    @classmethod
    def clear_turn_all(cls,hero,monsterlist):
        cls.nTurn = -1
        hero.all_turn_buff_list = []
        hero.turn_buff_list = []
        for i in range(len(monsterlist)):
            monsterlist[i].all_turn_buff_list = []
            monsterlist[i].turn_buff_list = []

    @classmethod
    def clear_action_all(cls,hero,monsterlist):
        hero.attack = []
        hero.direction = []
        hero.defence = 0
        for i in range(len(monsterlist)):
            monsterlist[i].attack = []
            monsterlist[i].direction = []
            monsterlist[i].defence = 0


    @classmethod
    def clear_observer_all(cls):
        for i in range(len(ObserverCenter.observing_list)):
            ObserverCenter.observing_list[i].initialize()
        ObserverCenter.observing_list = []

    @classmethod
    def show_stat_and_spell_list(cls,hero,monsterlist): # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        printt("나의...")
        hero.show_stat()
        print('사용 가능한 마법:', end='')
        printt(hero.spell_list_mapping("name"))

        for i in range(len(monsterlist)):
            printt('{0}번째 상대, {1}의...'.format(i, monsterlist[i].name))
            monsterlist[i].show_stat()


    @classmethod
    def monster_spell_list_decide(cls,monster,monster_brain): #상대가 사용할 스킬 인스턴스 리스트를 채우는 메소드. 이때 버프 목록 1회 초기화
        #ex)Slimebrain.slimebrain1 넣기. 단, 절대로 뇌를 '호출' 하지 말것.즉 Slimebrain.slimebrain1(monsterlist) 이렇게 넣으면 ㅈ댐.
        monster.spell_use_list = monster_brain(monster)
        monster.buff_list_init()

    @classmethod
    def monster_dice_activate(cls,monster,monster_availbrain):
        monster_availbrain(monster)

    @classmethod
    def hero_spell_list_show(cls,hero): # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.
        printt('현재 사용 예정인 푸른 마력 주사위 : {0}'.format(sum(cls.hero_using_manadice_list)))
        printt('현재 사용 예정인 붉은 마력 주사위 : {0}'.format(sum(cls.hero_using_healthdice_list)))
        printt('현재 사용 예정인 초록 마력 주사위 : {0} / {1}'.format(sum(cls.hero_using_green_list), hero.max_act_point))
        printt('현재 사용 예정인 마법 : {0}'.format(hero.spell_use_list_mapping("name")))

    @classmethod
    def turn_buff_list_show(cls,hero,monsterlist):
        monsallturnbufftrue = False
        for monster in monsterlist:
            if monster.all_turn_buff_list != []:
                monsallturnbufftrue = True

        monsturnbufftrue = False
        for monster in monsterlist:
            if monster.turn_buff_list != []:
                monsturnbufftrue = True

        if len(hero.all_turn_buff_list) != 0 or monsallturnbufftrue == True:
            printt("이번 전투 동안, 현재 턴을 포함한 모든 턴에 특수한 효과가 걸릴 것이 감지됩니다.")
        if len(hero.all_turn_buff_list) != 0:
            printt("영웅에게,")
            for i in range(len(hero.all_turn_buff_list)):
                print("{0} : {1}".format(hero.all_turn_buff_list[i].name, hero.all_turn_buff_list[i].showname))
        for i in range(len(monsterlist)):
            if len(monsterlist[i].all_turn_buff_list) != 0:
                printt("{0}번째 적 {1}에게,".format(i, monsterlist[i].name))
                for j in range(len(monsterlist[i].all_turn_buff_list)):
                    print("{0} : {1}".format(monsterlist[i].all_turn_buff_list[j].name,
                                             monsterlist[i].all_turn_buff_list[j].showname))


        if len(hero.turn_buff_list) != 0 or monsturnbufftrue == True:
            printt("또한, 이번 턴 혹은 이후 턴에 적 또는 당신에게 특수한 효과가 걸릴 것이 감지됩니다.")
        if len(hero.turn_buff_list) != 0:
            printt("영웅에게,")
            for i in range(len(hero.turn_buff_list)):
                if i == 0:
                    print("이번 턴:")
                else:
                    print("{0}턴 후:".format(i))
                for j in range(len(hero.turn_buff_list[i])):
                    print("{0} : {1}".format(hero.turn_buff_list[i][j].name, hero.turn_buff_list[i][j].showname))
        for i in range(len(monsterlist)):
            if len(monsterlist[i].turn_buff_list) != 0:
                printt("{0}번째 적 {1}에게,".format(i, monsterlist[i].name))
                for p in range(len(monsterlist[i].turn_buff_list)):
                    if p == 0:
                        print("이번 턴:")
                    else:
                        print("{0}턴 후:".format(p))
                    for j in range(len(monsterlist[i].turn_buff_list[p])):
                        print("{0} : {1}".format(monsterlist[i].turn_buff_list[p][j].name,
                                                 monsterlist[i].turn_buff_list[p][j].showname))

    @classmethod
    def hero_spell_list_decide(cls,hero,i,namelist): # 내가 사용할 스킬 리스트를 채우는 메소드. 이때 버프 목록 1회 초기화.
        #주사위의 개수를 저장하는 리스트를 채운 뒤, 이를 통해 유저가 입력한 스킬을 사용하기에 자원이 부족하다면 에러 문자열 출력하는 코드도 있음.
        # name에는 사용할 주문의 이름.
        printt('*')
        name = input('사용할 마법의 이름은?')
        hero.spell_use_list.append(hero.use_spell(name))
        if hero.spell_use_list[i] == "Error!":
            printt('그런 마법을 배운 적이 있었나...? 기억이 나지 않는다.')
            hero.spell_use_list.pop()
            return 'Error!'

        # 사용할 보조 주사위의 개수를 입력받고, 모든 주사위를 적절히 활성화시킴.
        if hero.spell_use_list[i].main_resource_kinds == "red":
            printt("보조 주사위로서 초록 주사위를 최소 1개 사용해야 하며, 추가로 최대 {0}개 더 사용 가능. ".format(
                len(hero.spell_use_list[i].green_dice_list) - 1))
            try:
                subnum = int(input("추가 융합할 보조 주사위 개수는?"))
            except ValueError:
                printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
            if subnum == 0:
                hero.spell_use_list[i].avail_all("red")
                hero.spell_use_list[i].green_dice_list[0].activate()
                hero.spell_use_list[i].direc_decide(namelist)
            elif 0 < subnum < len(hero.spell_use_list[i].green_dice_list):
                hero.spell_use_list[i].avail_all("red")
                for j in range(subnum + 1):
                    hero.spell_use_list[i].green_dice_list[j].activate()
                hero.spell_use_list[i].direc_decide(namelist)
            else:
                printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
        elif hero.spell_use_list[i].main_resource_kinds == "blue":
            printt("보조 주사위로서 초록 주사위를 최소 1개 사용해야 하며, 추가로 최대 {0}개 더 사용 가능. ".format(
                len(hero.spell_use_list[i].green_dice_list) - 1))
            try:
                subnum = int(input("추가 융합할 보조 주사위 개수는?"))
            except ValueError:
                printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
            if subnum == 0:
                hero.spell_use_list[i].avail_all("blue")
                hero.spell_use_list[i].green_dice_list[0].activate()
                hero.spell_use_list[i].direc_decide(namelist)
            elif 0 < subnum < len(hero.spell_use_list[i].green_dice_list):
                hero.spell_use_list[i].avail_all("blue")
                for j in range(subnum + 1):
                    hero.spell_use_list[i].green_dice_list[j].activate()
                hero.spell_use_list[i].direc_decide(namelist)
            else:
                printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
        elif hero.spell_use_list[i].main_resource_kinds == "green" and hero.spell_use_list[i].only_one_green == False:
            printt("보조 주사위로서 최대 붉은 주사위 {0}개, 푸른 주사위 {1}개를 융합 가능.".format(len(hero.spell_use_list[i].red_dice_list),
                                                                         len(hero.spell_use_list[i].blue_dice_list)))
            subkinds = input("융합할 보조 주사위의 종류는? red/blue")
            if subkinds == "red":
                try:
                    subnum = int(input("융합할 보조 주사위 개수는?"))
                except ValueError:
                    printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
                if subnum == 0:
                    hero.spell_use_list[i].avail_all("green")
                    hero.spell_use_list[i].direc_decide(namelist)
                elif 0 < subnum <= len(hero.spell_use_list[i].red_dice_list):
                    hero.spell_use_list[i].avail_all("green")
                    for j in range(subnum):
                        hero.spell_use_list[i].red_dice_list[j].activate()
                    hero.spell_use_list[i].direc_decide(namelist)
                else:
                    printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
            elif subkinds == "blue":
                try:
                    subnum = int(input("융합할 보조 주사위 개수는?"))
                except ValueError:
                    printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
                if subnum == 0:
                    hero.spell_use_list[i].avail_all("green")
                    hero.spell_use_list[i].direc_decide(namelist)
                elif 0 < subnum <= len(hero.spell_use_list[i].blue_dice_list):
                    hero.spell_use_list[i].avail_all("green")
                    for j in range(subnum):
                        hero.spell_use_list[i].blue_dice_list[j].activate()
                    hero.spell_use_list[i].direc_decide(namelist)
                else:
                    printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
            else:
                printt("유효한 입력값이 아닙니다.")
                hero.spell_use_list.pop()
                return "Error!"
        elif hero.spell_use_list[i].only_one_green == True:
            print("초록색 주사위를 던지자!")
            hero.spell_use_list[i].avail_all("green")
            hero.spell_use_list[i].direc_decide(namelist)

        # 영웅이 사용할 마나/체력/행동점수 주사위의 개수를 리스트에 저장. 원리: 전단계에서 활성화시킨 주사위의 수를 셈.
        cls.hero_using_healthdice_list.append(hero.spell_use_list[i].avail_count("red"))
        cls.hero_using_manadice_list.append(hero.spell_use_list[i].avail_count("blue"))
        cls.hero_using_green_list.append(hero.spell_use_list[i].avail_count("green"))

        # 사용 가능한 자원보다 요구자원이 많을 때 "Error!"을 반환.
        if sum(cls.hero_using_manadice_list) > hero.mana_dice:
            printt('아무래도 푸른 마력 주사위가 부족한 듯 하다.')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'
        elif sum(cls.hero_using_healthdice_list) > hero.health_dice or sum(
                cls.hero_using_healthdice_list) == hero.health_dice and hero.health_dice * Character.healthtodice == hero.health:
            printt('붉은 마나 주사위를 사용하려 하자, 당신의 심장이 욱신거리기 시작한다!')
            printt('아무래도 남은 체력을 전부 사용하는것은 좋지 않을 듯 하다...')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'
        elif sum(cls.hero_using_green_list) > hero.act_point:
            printt('아무래도 초록 마력 주사위가 부족한 듯 하다.')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'

        # 버프 목록을 초기화시킴
        hero.buff_list_init()

        printt('*')

    @classmethod
    def turn_buff_hero_monster(cls,hero,monsterlist):
        if len(hero.all_turn_buff_list) != 0:
            printt("이번 전투 에(모든 턴에), 당신에게 특수한 효과가 발동되었습니다.")
            for buff in hero.all_turn_buff_list:
                printt("{0} : {1}".format(buff.name, buff.showname))
            for buff in hero.all_turn_buff_list:
                buff.use(hero,monsterlist)

        for i in range(len(monsterlist)):
            if len(monsterlist[i].all_turn_buff_list) != 0:
                printt("이번 전투 에(모든 턴에),{0}번 몬스터 {1}에게 특수한 효과가 발동되었습니다.".format(i, monsterlist[i].name))
                for buff in monsterlist[i].all_turn_buff_list:
                    printt("{0} : {1}".format(buff.name, buff.showname))
                for buff in monsterlist[i].all_turn_buff_list:
                    buff.use(hero, monsterlist)




        if len(hero.turn_buff_list) != 0:
            printt("이번 턴에, 당신에게 특수한 효과가 발동되었습니다.")
            for buff in hero.turn_buff_list[0]:
                printt("{0} : {1}".format(buff.name, buff.showname))
            for buff in hero.turn_buff_list[0]:
                buff.use(hero,monsterlist)
            hero.turn_buff_list.pop(0)

        for i in range(len(monsterlist)):
            if len(monsterlist[i].turn_buff_list) != 0:
                printt("이번 턴에, 적에게 특수한 효과가 발동되었습니다.")
                for buff in monsterlist[i].turn_buff_list[0]:
                    printt("{0} : {1}".format(buff.name, buff.showname))
                for buff in monsterlist[i].turn_buff_list[0]:
                    buff.use(hero, monsterlist)
                monsterlist[i].turn_buff_list.pop(0)

    @classmethod
    def observercenter(cls):
        if ObserverCenter.observing_list != []:
            printt("이번 전투 에(모든 턴에) 발동에 특수한 조건이 걸려있는 효과가 감지되었습니다.")

            #신문물 시도!
            for var in ObserverCenter.observing_list:
                if var.observer != []:
                    for stack in var.observer:
                        for obslist in stack[1]:
                            for obs in obslist:
                                if obs[5] == True:
                                    obs[6](var.observer)
                if var.always_observer != []:
                    for obs in var.always_observer:
                        if obs[5] == True:
                            obs[6](var.always_observer)

            '''
            for var in ObserverCenter.observing_list:
                printt("{0} : ".format(var.name))
                if var.observer != []:
                    printt("다음 효과들은 {0}가 1,2,3...회 변경되면 x회 적용되고 나서 사라집니다. 적용 시 조건에 맞지 않으면 발동이 보류됩니다.".format(var.name))
                    for i in range(len(var.observer)):
                        printt("{0} : {1}".format(var.observer[i][0], var.observer[i][1].showname))
                        test = []
                        for j in range(len(var.observer[i][2])):
                            test.append(len(var.observer[i][2][j]))
                        printt("x회: {0}".format(test))

                if var.always_observer != []:
                    printt("다음 효과들은 {0}가 변경되면 이번 전투동안 항상 적용되고 사라지지 않습니다. 적용 시 조건에 맞지 않으면 발동이 보류됩니다.".format(var.name))
                    for j in range(len(var.always_observer)):
                        printt("{0} : {1}".format(var.always_observer[j][1], var.always_observer[j][3].showname))
            '''


    @classmethod
    def hero_monster_use_resource(cls,hero,monsterlist,i):# 마법의 사용 대가를 치루는 코드. 전투 중간에 마나나 체력이 부족해졌을 시에 마법 사용을 거부하는 역할도 추가됨.

        try:
            hero.spell_use_list[i].pay_price(hero, monsterlist)
        except IndexError:
            hero.fault_bool = True

        for j in range(len(monsterlist)):
            try:
                monsterlist[j].spell_use_list[i].pay_price(hero, monsterlist)
            except IndexError:
                monsterlist[j].fault_bool = True









    @classmethod
    def roll_hero_monster(cls, i, hero, monsterlist):  # 영웅과 적의 스킬을 사용,(그 뒤 버프 목록 갱신,) 행동력이 부족하다면 행동 불능상태로 만드는 코드.
        # i는 몇번째 행동인지 인자. (0번째, 1번째...)


        try:
            if hero.fault_bool == False:
                hero.spell_use_list[i].use(hero, monsterlist)
                hero.buff_list_init()

        except IndexError:  # 인덱스 에러가 뜨면 사용할 마법 인스턴스 리스트 인덱스 길이보다 전투 번째수가 많으므로 행동 불능 상태로 만드는 코드.
            hero.fault_bool = True


        for j in range(len(monsterlist)):
            try:
                if monsterlist[j].fault_bool == False:
                    monsterlist[j].spell_use_list[i].use(hero, monsterlist)
                    monsterlist[j].buff_list_init()

            except IndexError:  # 마찬가지로 행동 불능 상태로 만드는 코드.
                monsterlist[j].fault_bool = True

    @classmethod
    def action_buff_hero_monster(cls, i, hero, monsterlist):

        try:
            if len(hero.buff_list[i]) != 0:
                printt("이번 행동에, 당신에게 특수한 효과가 부여되었습니다.")
                for j in range(len(hero.buff_list[i])):
                    printt("{0} : {1}".format(hero.buff_list[i][j].name, hero.buff_list[i][j].showname))
                for j in range(len(hero.buff_list[i])):
                    hero.buff_list[i][j].use(hero, monsterlist)

        except IndexError:
            hero.fault_bool = True

        for j in range(len(monsterlist)):
            try:
                if len(monsterlist[j].buff_list[i]) != 0:
                    printt("이번 행동에, {0}번째 적 {1} 에게 특수한 효과가 부여되었습니다.".format(j, monsterlist[j].name))
                    for p in range(len(monsterlist[j].buff_list[i])):
                        printt("{0} : {1}".format(monsterlist[j].buff_list[i][p].name, monsterlist[j].buff_list[i][p].showname))
                    for p in range(len(monsterlist[j].buff_list[i])):
                        monsterlist[j].buff_list[i][p].use(hero, monsterlist)


            except IndexError:
                monsterlist[j].fault_bool = True


    @classmethod
    def atk_def_skill_to_character(cls,i,hero,monsterlist): #최종 공격력과 방어력(캐릭터 공방력)을 결정.
        if hero.fault_bool == False:
            hero.attack += hero.spell_use_list[i].temp_atk
            hero.direction += hero.spell_use_list[i].temp_direc
            hero.defence += hero.spell_use_list[i].temp_def
        for j in range(len(hero.attack)):
            if hero.attack[j] < 0:
                hero.attack[j] = 0
        if hero.defence < 0:
            hero.defence = 0

        for k in range(len(monsterlist)):
            if monsterlist[k].fault_bool == False:
                monsterlist[k].attack += monsterlist[k].spell_use_list[i].temp_atk
                monsterlist[k].direction += monsterlist[k].spell_use_list[i].temp_direc
                monsterlist[k].defence += monsterlist[k].spell_use_list[i].temp_def
            for j in range(len(monsterlist[k].attack)):
                if monsterlist[k].attack[j] < 0:
                    monsterlist[k].attack[j] = 0
            if monsterlist[k].defence < 0:
                monsterlist[k].defence = 0

    @classmethod
    def small_fight(cls, hero, monsterlist):  # 방어력과 공격력을 서로 겨루게 한 뒤 피해를 입히거나 입게 하는 메소드. 마찬가지로 행동 불능에 따른 상황 역시 고려한다.
        monsternamelist = []
        for monster in monsterlist:
            monsternamelist.append(monster.name)
        printt("전투가 시작된다.")

        if hero.fault_bool == False:
            printt("당신은 몬스터들에게 공격을 할 준비를 한다.")
            if len(hero.attack) != len(hero.direction):
                raise Exception

            for i in range(len(hero.attack)):
                monster = monsterlist[monsternamelist.index(hero.direction[i])]
                printt("당신|공격력 {0} >>|| 방어력 {1}|몬스터 ({2}) ".format(hero.attack[i],monster.defence, hero.direction[i]))
                if hero.attack[i] > monster.defence:
                    monster.change_health(monster.health + monster.defence - hero.attack[i])
                    monster.defence = 0
                    printt("방어 관통! 적에게 데미지가 들어왔다.")
                elif hero.attack[i] <= monster.defence:
                    monster.defence -= hero.attack[i]
                    printt("공격 막힘! 적의 방어력이 대신 깎였다.")
        else:
            printt("당신은 행동 불능, 몬스터들에게 공격할 수 없었다.")
            if hero.attack != [] and hero.direction != []:
                printt("그러나, 당신에겐 왠지 모르게 공격력이 부여되어 있다.")
                if len(hero.attack) != len(hero.direction):
                    raise Exception

                for i in range(len(hero.attack)):
                    monster = monsterlist[monsternamelist.index(hero.direction[i])]
                    printt(
                        "당신|공격력 {0} >>|| 방어력 {1}|몬스터 ({2}) ".format(hero.attack[i], monster.defence, hero.direction[i]))
                    if hero.attack[i] > monster.defence:
                        monster.change_health(monster.health + monster.defence - hero.attack[i])
                        monster.defence = 0
                        printt("방어 관통! 적에게 데미지가 들어왔다.")
                    elif hero.attack[i] <= monster.defence:
                        monster.defence -= hero.attack[i]
                        printt("공격 막힘! 적의 방어력이 대신 깎였다.")

        printt("이제, 몬스터들이 당신에게 공격을 할 준비를 한다.")
        for i in range(len(monsterlist)):
            ismonsatknone = False
            if monsterlist[i].attack == []:
                ismonsatknone = True
            if monsterlist[i].fault_bool == False:
                if ismonsatknone == True:
                    printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, 0, monsterlist[i].name))

                else:
                    printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, monsterlist[i].attack[0], monsterlist[i].name))

                    if monsterlist[i].attack[0] > hero.defence:
                        hero.change_health(hero.health + hero.defence - monsterlist[i].attack[0])
                        hero.defence = 0
                        printt("방어 관통! 당신에게 데미지가 들어갔다.")
                    elif monsterlist[i].attack[0] <= hero.defence:
                        hero.defence -= monsterlist[i].attack[0]
                        printt("공격 막힘! 당신의 방어력이 대신 깎였다.")

            else:
                printt("몬스터 {0}은 행동 불능, 공격하지 못한다.".format(monsterlist[i].name))
                if monsterlist[i].attack != [] and monsterlist[i].direction != []:
                    printt("그러나, 적에겐 왠지 모르게 공격력이 부여되어 있다.")
                    ismonsatknone = False
                    if monsterlist[i].attack == []:
                        ismonsatknone = True
                    if monsterlist[i].fault_bool == False:
                        if ismonsatknone == True:
                            printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, 0, monsterlist[i].name))

                        else:
                            printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, monsterlist[i].attack[0],
                                                                             monsterlist[i].name))

                            if monsterlist[i].attack[0] > hero.defence:
                                hero.change_health(hero.health + hero.defence - monsterlist[i].attack[0])
                                hero.defence = 0
                                printt("방어 관통! 당신에게 데미지가 들어갔다.")
                            elif monsterlist[i].attack[0] <= hero.defence:
                                hero.defence -= monsterlist[i].attack[0]
                                printt("공격 막힘! 당신의 방어력이 대신 깎였다.")

        printt('나의 남은 붉은 마력 주사위:{0}개 (체력 {1})'.format(hero.health_dice, hero.health))
        for monster in monsterlist:
            printt('상대 {0}의 붉은 마력 주사위:{1}개 (체력 {2})'.format(monster.name,monster.health_dice, monster.health))


    @classmethod
    def lose_win_define(cls,hero,monsterlist): #체력 상태에 따른 승패를 판정하는 메소드. 승패 bool 속성을 건드린다.
        if hero.health <= 0:
            printt('당신은 몬스터에게 패배했습니다...')
            printt('game over!')
            raise Exception("패배!")
        for i in range(len(monsterlist)):
            if monsterlist[i].health <= 0:
                printt("몬스터 {0}, 넉다운!".format(monsterlist[i].name))
                monsterlist[i] = None
        i = 0
        while i < len(monsterlist):
            if monsterlist[i] == None:
                monsterlist.pop(i)
                i -= 1
            i += 1

        if monsterlist == []:
            printt("당신은 몬스터들로부터 승리하였습니다!")
            printt("승리!")
            cls.fight_end = True

    @classmethod
    def use_bag(cls,hero):
        open_or_not = input("가방을 여시겠습니까? (y/n)")
        if open_or_not == "y":
            while len(hero.bag_list) != 0:
                print("가방:", hero.bag_name_list)
                use_item_name = input("어떤 아이템을 사용하시겠습니까? (가방을 닫을려면 0)")

                if use_item_name == "0":
                    printt("가방을 닫았습니다.")
                    break

                for i in hero.bag_list:
                    if i.name == use_item_name:
                        i.use(hero)
                        break
                    elif use_item_name != "0" and i.name != use_item_name and hero.bag_list.index(i) == len(hero.bag_list) - 1:  # 해당 아이템이 가방에 없을 경우
                        printt("잘못 입력하였습니다.")





##############################################진짜 전투 부분.지금까지 사용한 모든 메서드 총집합!##########################
    @classmethod
    def big_fight(cls,hero,monsterlist,monster_brainlist,monster_availbrainlist): #한 턴을 진행한다.

        cls.nTurn += 1
        printt("{0}번째 턴!".format(cls.nTurn))
        #사용한 변수들을 초기화한다.
        cls.clear_nomal_all(hero, monsterlist)

        #캐릭터들의 파라미터를 초기화한다.
        cls.clear_character_all(hero, monsterlist)

        #행동 관련 파라미터를 초기화한다.
        cls.clear_action_all(hero,monsterlist)

        # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        printt('*')
        cls.show_stat_and_spell_list(hero, monsterlist)
        printt('*')

        # 가방
        cls.use_bag(hero)

        # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        printt('*')
        cls.show_stat_and_spell_list(hero, monsterlist)
        printt('*')
        # 마법의 설명을 듣을 것인지 묻고, 마법의 설명을 출력.
        ask = input("사용 가능한 마법들의 설명을 들으시겠습니까? y/n")
        if ask == "y":
            for spell in hero.spell_list:
                print('*')
                printt("스킬 이름:" + spell.name)
                printt("스킬 상세:" + spell.showname)
                printt("스킬 설명:" + spell.crazyname)
                print('*')

        # 턴 단위의 버프가 앞으로 적용된다면, 이를 출력한다
        cls.turn_buff_list_show(hero,monsterlist)

        # 특정 조건 만족시 발동되는 효과가 있다면, 이를 출력한다.
        cls.observercenter()

        for i in range(len(monsterlist)):
            # >>적이 사용할 스킬 인스턴스 리스트를 채우기. 이때 행동 단위 버프 갱신
            cls.monster_spell_list_decide(monsterlist[i], monster_brainlist[i])

            # >>적이 사용할 스킬 인스턴스 리스트 내의 주사위를 활성화시킴(의미:사용할 주사위 결정)
            cls.monster_dice_activate(monsterlist[i], monster_availbrainlist[i])


        #>>내가 사용할 스킬 인스턴스 리스트를 채우기. 그리고 내부 주사위 활성화시키기.(의미: 사용할 주사위 결정) 이때 행동 단위 버프 갱신
        j = 0
        while (hero.act_point > sum(cls.hero_using_green_list)):
            printt('*')
            cls.hero_spell_list_show(hero) # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.
            printt('*')
            namelist = ['hero']
            for i in range(len(monsterlist)):
                namelist.append(monsterlist[i].name)

            if cls.hero_spell_list_decide(hero,j,namelist) != None: # 내가 사용할 스킬 리스트를 채우는 메소드. 사용 예정인 마나, 체력, 행동점수
        #주사위의 개수를 저장하는 리스트를 채운 뒤, 이를 통해 유저가 입력한 스킬을 사용하기에 자원이 부족하다면 에러 문자열 출력. 또한,
        #스킬 인스턴스들 내부 주사위들을 유저가 원하는 만큼 규칙에 의거해 활성화시킴. 이를 통해 주사위를 얼마나 사용할것인지 예정시킴
                pass
            else:
                j += 1
        cls.hero_spell_list_show(hero) # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.

        #턴 단위 버프를 적용한다.
        cls.turn_buff_hero_monster(hero,monsterlist)


        i = 0
        # 선택한 주문대로 전투를 시작한다.
        while True: #한 행동 진행.
            # 행동불능 상태 복구
            hero.fault_bool = False
            for j in range(len(monsterlist)):
                monsterlist[j].fault_bool = False


            # 미리 행동불능 여부 재판단
            if len(hero.spell_use_list) <= i:
                hero.fault_bool = True
            for j in range(len(monsterlist)):
                if len(monsterlist[j].spell_use_list) <= i:
                    monsterlist[j].fault_bool = True


            #둘 다 행동불능에 빠졌을 경우 이번 턴 종료
            monsterfaultall = True
            for monster in monsterlist:
                if monster.fault_bool == False:
                    monsterfaultall = False
            if hero.fault_bool == True and monsterfaultall == True:
                # 전투 종료시엔 반드시 행동력 초기화,행동불능 상태 복구
                hero.fault_bool = False
                hero.act_point = hero.max_act_point
                for i in range(len(monsterlist)):
                    monsterlist[i].fault_bool = False
                    monsterlist[i].act_point = monsterlist[i].max_act_point

                printt('=============================================================')
                break

            # n번째 행동!
            printt('=============================================================')


            printt('{0}번째 행동!'.format(i))

            # 대가 사용, 활성화된 주사위를 참고하여.
            cls.hero_monster_use_resource(hero, monsterlist,i)  # 마법의 사용 대가를 치루는 코드. 전투 중간에 마나나 체력이 부족해졌을 시에 마법 사용을 거부하는 역할도 추가됨.

            # 주사위 굴리기 and 사용하기, 표시하기, 스킬로 인해 발생한 공격력 및 방어력 표시와 기타 잡다한 스킬 사용시 표시해야할 것들 표시. 행동 단위 버프 1회 더 갱신
            printt('')
            cls.roll_hero_monster(i,hero,monsterlist) # 영웅과 적의 방어/공격량을 정하고(주사위를 실질적으로 "사용"), 행동력이 부족하다면 행동 불능상태로 만드는 코드.

            # 행동 단위에 적용되는 버프/디버프 사용
            printt('')
            cls.action_buff_hero_monster(i, hero, monsterlist)

            #최종 공격력, 방어력을 결정
            printt('')
            cls.atk_def_skill_to_character(i,hero,monsterlist)

            # 주사위 표시
            #cls.hero_monsterlist_show_dice(i,hero,monsterlist)
            # >>마법 인스턴스에 임시 저장되어있는 주사위를 굴린 결과를 그대로 출력해주는 코드.
            # >>다만, 걸리는 점이 있다면 같은 마법을 중복해서 사용할 경우에는 임시 저장된 결과가 덮어씌워지지 않으면 문제가 발생하므로 불만.
            # >>이를 해결하기 위하여 .use메소드를 사용할 때에 이전에 남아있던 .dice속성의 정보를 없애도록 하였으나 임시방편임은 마찬가지.
            ###수정### 주사위 굴리기 단계로 통폐합됨

            # 공격/방어 판정 및 공격력 방어력 표시
            #cls.attack_defence_decide(i,hero,monsterlist) #몬스터와 영웅의 공격/방어여부를 결정하고, 방어력과 공격력, 사용한 자원의 종류를 출력하는 메소드. 행동 불능이면 건너뛴다.
            ###이놈도 통폐합###
            # 전투 판정
            printt('')
            cls.small_fight(hero, monsterlist) #방어력과 공격력을 서로 겨루게 한 뒤 피해를 입히거나 입게 하는 메소드. 행동 불능에 따른 상황을 고려한다.

            #공격력, 방어력과 같은, 매 행동마다 초기화 해야 하는 변수들만 따로 다시 초기화 한다.
            cls.clear_action_all(hero,monsterlist)

            # 승패를 판단한다. #체력 상태에 따른 승패를 판정하는 메소드. 승패 bool 속성을 건드린다.
            cls.lose_win_define(hero,monsterlist)


            if cls.fight_end == True:
                # 전투 종료시엔 반드시 행동력 초기화
                hero.act_point = hero.max_act_point
                # 행동불능 상태 복구
                hero.fault_bool = False
                break

            #몇번째인지 나타내주는 i에 1더하기.
            i += 1





