from monster_algorithm import *

class Fight:

    hero_using_manadice_list = []
    hero_using_healthdice_list = []
    hero_using_green_list = []

    nTurn = -1

    fight_end = False #전투 종료 여부

    @classmethod
    def clear_all(cls, hero, monsterlist,myapp):
        cls.clear_nomal_all(hero, monsterlist)
        cls.clear_character_all(hero, monsterlist)
        cls.clear_fight_all(hero, monsterlist, myapp)
        cls.clear_action_all(hero, monsterlist,myapp)
        cls.clear_observer_all()
        cls.clear_turn_all(hero,monsterlist,myapp)
        cls.clear_heroGUI_all(myapp)
        cls.clear_mn1GUI_all(myapp)
        cls.clear_mn2GUI_all(myapp)
        cls.clear_mn3GUI_all(myapp)
        cls.Victory = False

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
    def clear_fight_all(cls, hero, monsterlist, myapp):
        cls.nTurn = -1
        hero.all_turn_buff_list = []
        hero.turn_buff_list = []
        for i in range(len(monsterlist)):
            monsterlist[i].all_turn_buff_list = []
            monsterlist[i].turn_buff_list = []


    @classmethod
    def clear_turn_all(cls,hero,monsterlist,myapp):
        myapp.allturnbuffte.clear()
        myapp.turnbuffte.clear()
        myapp.mn1allturnbuffte.clear()
        myapp.mn1turnbuffte.clear()
        myapp.mn2allturnbuffte.clear()
        myapp.mn2turnbuffte.clear()
        myapp.mn3allturnbuffte.clear()
        myapp.mn3turnbuffte.clear()
        myapp.actionbuffte.clear()
        myapp.mn1actionbuffte.clear()
        myapp.mn2actionbuffte.clear()
        myapp.mn3actionbuffte.clear()

        myapp.spelluselistte.clear()
        myapp.mn1spelluselistte.clear()
        myapp.mn2spelluselistte.clear()
        myapp.mn3spelluselistte.clear()


    @classmethod
    def clear_action_all(cls,hero,monsterlist,myapp):
        hero.attack = []
        hero.direction = []
        hero.defence = 0
        for i in range(len(monsterlist)):
            monsterlist[i].attack = []
            monsterlist[i].direction = []
            monsterlist[i].defence = 0
        myapp.attackte.clear()
        myapp.mn1attackte.clear()
        myapp.mn2attackte.clear()
        myapp.mn3attackte.clear()
        myapp.attackte.clear()
        myapp.mn1attackte.clear()
        myapp.mn2attackte.clear()
        myapp.mn3attackte.clear()

        myapp.resactlied.clear()
        myapp.resbluedicelied.clear()
        myapp.reshealthlied.clear()
        myapp.resmaxactlied.clear()
        myapp.resreddicelied.clear()
        myapp.resmanalied.clear()

    @classmethod
    def clear_observer_all(cls):
        for i in range(len(ObserverCenter.observing_list)):
            ObserverCenter.observing_list[i].initialize()
        ObserverCenter.observing_list = []

    @classmethod
    def clear_heroGUI_all(cls,myapp):
        myapp.namelied.clear()
        myapp.healthlied.clear()
        myapp.reddicelied.clear()
        myapp.manalied.clear()
        myapp.bluedicelied.clear()
        myapp.maxactlied.clear()
        myapp.actlied.clear()
        myapp.redrollresultlied.clear()
        myapp.bluerollresultlied.clear()
        myapp.greenrollresultlied.clear()
        myapp.spelluselistte.clear()
        myapp.allturnbuffte.clear()
        myapp.turnbuffte.clear()
        myapp.actionbuffte.clear()
        myapp.attackte.clear()
        myapp.defencelied.clear()
        myapp.faultbtn.setEnabled(True)

    @classmethod
    def clear_mn1GUI_all(cls,myapp):
        myapp.mn1namelied.clear()
        myapp.mn1healthlied.clear()
        myapp.mn1reddicelied.clear()
        myapp.mn1manalied.clear()
        myapp.mn1bluedicelied.clear()
        myapp.mn1maxactlied.clear()
        myapp.mn1actlied.clear()
        myapp.mn1redrollresultlied.clear()
        myapp.mn1bluerollresultlied.clear()
        myapp.mn1greenrollresultlied.clear()
        myapp.mn1spelluselistte.clear()
        myapp.mn1allturnbuffte.clear()
        myapp.mn1turnbuffte.clear()
        myapp.mn1actionbuffte.clear()
        myapp.mn1attackte.clear()
        myapp.mn1defencelied.clear()
        myapp.mn1faultbtn.setEnabled(True)

    @classmethod
    def clear_mn2GUI_all(cls, myapp):
        myapp.mn2namelied.clear()
        myapp.mn2healthlied.clear()
        myapp.mn2reddicelied.clear()
        myapp.mn2manalied.clear()
        myapp.mn2bluedicelied.clear()
        myapp.mn2maxactlied.clear()
        myapp.mn2actlied.clear()
        myapp.mn2redrollresultlied.clear()
        myapp.mn2bluerollresultlied.clear()
        myapp.mn2greenrollresultlied.clear()
        myapp.mn2spelluselistte.clear()
        myapp.mn2allturnbuffte.clear()
        myapp.mn2turnbuffte.clear()
        myapp.mn2actionbuffte.clear()
        myapp.mn2attackte.clear()
        myapp.mn2defencelied.clear()
        myapp.mn2faultbtn.setEnabled(True)

    @classmethod
    def clear_mn3GUI_all(cls, myapp):
        myapp.mn3namelied.clear()
        myapp.mn3healthlied.clear()
        myapp.mn3reddicelied.clear()
        myapp.mn3manalied.clear()
        myapp.mn3bluedicelied.clear()
        myapp.mn3maxactlied.clear()
        myapp.mn3actlied.clear()
        myapp.mn3redrollresultlied.clear()
        myapp.mn3bluerollresultlied.clear()
        myapp.mn3greenrollresultlied.clear()
        myapp.mn3spelluselistte.clear()
        myapp.mn3allturnbuffte.clear()
        myapp.mn3turnbuffte.clear()
        myapp.mn3actionbuffte.clear()
        myapp.mn3attackte.clear()
        myapp.mn3defencelied.clear()
        myapp.mn3faultbtn.setEnabled(True)

    @classmethod
    def show_stat_and_spell_list(cls,hero,monsterlist,myapp): # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        hero.show_stat(monsterlist,myapp)

        for i in range(len(monsterlist)):
            monsterlist[i].show_stat(monsterlist,myapp)


    @classmethod
    def monster_spell_list_decide(cls,monster,monster_brain): #상대가 사용할 스킬 인스턴스 리스트를 채우는 메소드. 이때 버프 목록 1회 초기화
        #ex)Slimebrain.slimebrain1 넣기. 단, 절대로 뇌를 '호출' 하지 말것.즉 Slimebrain.slimebrain1(monsterlist) 이렇게 넣으면 ㅈ댐.
        monster.spell_use_list = monster_brain(monster)
        monster.buff_list_init()

    @classmethod
    def monster_dice_activate(cls,monster,monster_availbrain):
        monster_availbrain(monster)

    @classmethod
    def hero_spell_list_show(cls,hero,myapp): # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.

        myapp.reshealthlied.setText(str(sum(cls.hero_using_healthdice_list) * Character.healthtodice))
        myapp.resreddicelied.setText(str(sum(cls.hero_using_healthdice_list)))
        myapp.resmanalied.setText(str(sum(cls.hero_using_manadice_list) * Character.manatodice))
        myapp.resbluedicelied.setText(str(sum(cls.hero_using_manadice_list)))
        myapp.resactlied.setText(str(sum(cls.hero_using_green_list)))
        myapp.resmaxactlied.setText(str(hero.max_act_point))

        myapp.spelluselistte.clear()
        for spell in hero.spell_use_list_mapping("name"):
            myapp.spelluselistte.append(str(spell))

    @classmethod
    def turn_buff_list_show(cls,hero,monsterlist,myapp):
        try:
            myapp.turnbuffte.clear()
            for buff in hero.turn_buff_list:
                for bu in buff:
                    myapp.turnbuffte.insertPlainText(bu.name + bu.showname)
                myapp.turnbuffte.insertPlainText("\n")
            myapp.mn1turnbuffte.clear()
            for buff in monsterlist[0].turn_buff_list:
                for bu in buff:
                    myapp.mn1turnbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn1turnbuffte.insertPlainText("\n")
            myapp.mn2turnbuffte.clear()
            for buff in monsterlist[1].turn_buff_list:
                for bu in buff:
                    myapp.mn2turnbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn2turnbuffte.insertPlainText("\n")
            myapp.mn3turnbuffte.clear()
            for buff in monsterlist[2].turn_buff_list:
                for bu in buff:
                    myapp.mn3turnbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn3turnbuffte.insertPlainText("\n")
        except IndexError:
            pass

        try:
            myapp.allturnbuffte.clear()
            for buff in hero.all_turn_buff_list:
                myapp.allturnbuffte.append(buff.name + buff.showname)
            myapp.mn1allturnbuffte.clear()
            for buff in monsterlist[0].all_turn_buff_list:
                myapp.mn1allturnbuffte.append(buff.name + buff.showname)
            myapp.mn2allturnbuffte.clear()
            for buff in monsterlist[1].all_turn_buff_list:
                myapp.mn2allturnbuffte.append(buff.name + buff.showname)
            myapp.mn3allturnbuffte.clear()
            for buff in monsterlist[2].all_turn_buff_list:
                myapp.mn3allturnbuffte.append(buff.name + buff.showname)
        except IndexError:
            pass



        monsallturnbufftrue = False
        for monster in monsterlist:
            if monster.all_turn_buff_list != []:
                monsallturnbufftrue = True

        monsturnbufftrue = False
        for monster in monsterlist:
            if monster.turn_buff_list != []:
                monsturnbufftrue = True

        if len(hero.all_turn_buff_list) != 0 or monsallturnbufftrue == True:
            myapp.printt("이번 전투 동안, 현재 턴을 포함한 모든 턴에 특수한 효과가 걸릴 것이 감지됩니다.")
        if len(hero.all_turn_buff_list) != 0:
            myapp.printt("영웅에게,")
            for i in range(len(hero.all_turn_buff_list)):
                print("{0} : {1}".format(hero.all_turn_buff_list[i].name, hero.all_turn_buff_list[i].showname))
        for i in range(len(monsterlist)):
            if len(monsterlist[i].all_turn_buff_list) != 0:
                myapp.printt("{0}번째 적 {1}에게,".format(i, monsterlist[i].name))
                for j in range(len(monsterlist[i].all_turn_buff_list)):
                    print("{0} : {1}".format(monsterlist[i].all_turn_buff_list[j].name,
                                             monsterlist[i].all_turn_buff_list[j].showname))


        if len(hero.turn_buff_list) != 0 or monsturnbufftrue == True:
            myapp.printt("또한, 이번 턴 혹은 이후 턴에 적 또는 당신에게 특수한 효과가 걸릴 것이 감지됩니다.")
        if len(hero.turn_buff_list) != 0:
            myapp.printt("영웅에게,")
            for i in range(len(hero.turn_buff_list)):
                if i == 0:
                    print("이번 턴:")
                else:
                    print("{0}턴 후:".format(i))
                for j in range(len(hero.turn_buff_list[i])):
                    print("{0} : {1}".format(hero.turn_buff_list[i][j].name, hero.turn_buff_list[i][j].showname))
        for i in range(len(monsterlist)):
            if len(monsterlist[i].turn_buff_list) != 0:
                myapp.printt("{0}번째 적 {1}에게,".format(i, monsterlist[i].name))
                for p in range(len(monsterlist[i].turn_buff_list)):
                    if p == 0:
                        print("이번 턴:")
                    else:
                        print("{0}턴 후:".format(p))
                    for j in range(len(monsterlist[i].turn_buff_list[p])):
                        print("{0} : {1}".format(monsterlist[i].turn_buff_list[p][j].name,
                                                 monsterlist[i].turn_buff_list[p][j].showname))

    @classmethod
    def hero_spell_list_decide(cls,hero,i,namelist,myapp): # 내가 사용할 스킬 리스트를 채우는 메소드. 이때 버프 목록 1회 초기화.
        #주사위의 개수를 저장하는 리스트를 채운 뒤, 이를 통해 유저가 입력한 스킬을 사용하기에 자원이 부족하다면 에러 문자열 출력하는 코드도 있음.
        # name에는 사용할 주문의 이름.
        myapp.printt('*')
        name = myapp.inputt('사용할 마법의 이름은?')
        hero.spell_use_list.append(hero.use_spell(name))
        if hero.spell_use_list[i] == "Error!":
            myapp.printt('그런 마법을 배운 적이 있었나...? 기억이 나지 않는다.')
            hero.spell_use_list.pop()
            return 'Error!'

        # 사용할 보조 주사위의 개수를 입력받고, 모든 주사위를 적절히 활성화시킴.
        if hero.spell_use_list[i].main_resource_kinds == "red":
            try:
                subnum = int(myapp.inputt("보조 주사위로서 초록 주사위를 최소 1개 사용해야 하며, 추가로 최대 {0}개 더 사용 가능. ".format(len(hero.spell_use_list[i].green_dice_list) - 1) + "\n" + "추가 융합할 보조 주사위 개수는?"))
            except ValueError:
                myapp.printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
            if subnum == 0:
                hero.spell_use_list[i].avail_all("red")
                hero.spell_use_list[i].green_dice_list[0].activate()
                hero.spell_use_list[i].direc_decide(namelist, myapp)
            elif 0 < subnum < len(hero.spell_use_list[i].green_dice_list):
                hero.spell_use_list[i].avail_all("red")
                for j in range(subnum + 1):
                    hero.spell_use_list[i].green_dice_list[j].activate()
                hero.spell_use_list[i].direc_decide(namelist,myapp)
            else:
                myapp.printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
        elif hero.spell_use_list[i].main_resource_kinds == "blue":
            try:
                subnum = int(myapp.inputt("보조 주사위로서 초록 주사위를 최소 1개 사용해야 하며, 추가로 최대 {0}개 더 사용 가능. ".format(len(hero.spell_use_list[i].green_dice_list) - 1) + "\n" + "추가 융합할 보조 주사위 개수는?"))
            except ValueError:
                myapp.printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
            if subnum == 0:
                hero.spell_use_list[i].avail_all("blue")
                hero.spell_use_list[i].green_dice_list[0].activate()
                hero.spell_use_list[i].direc_decide(namelist, myapp)
            elif 0 < subnum < len(hero.spell_use_list[i].green_dice_list):
                hero.spell_use_list[i].avail_all("blue")
                for j in range(subnum + 1):
                    hero.spell_use_list[i].green_dice_list[j].activate()
                hero.spell_use_list[i].direc_decide(namelist,myapp)
            else:
                myapp.printt("추가 융합할 보조 주사위 개수를 잘못 입력했습니다.")
                hero.spell_use_list.pop()
                return "Error!"
        elif hero.spell_use_list[i].main_resource_kinds == "green" and hero.spell_use_list[i].only_one_green == False:
            subkinds = myapp.inputt("보조 주사위로서 최대 붉은 주사위 {0}개, 푸른 주사위 {1}개를 융합 가능.".format(len(hero.spell_use_list[i].red_dice_list),len(hero.spell_use_list[i].blue_dice_list)) + "\n" + "융합할 보조 주사위의 종류는? red/blue")
            if subkinds == "red":
                try:
                    subnum = int(myapp.inputt("융합할 보조 주사위 개수는?"))
                except ValueError:
                    myapp.printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
                if subnum == 0:
                    hero.spell_use_list[i].avail_all("green")
                    hero.spell_use_list[i].direc_decide(namelist, myapp)
                elif 0 < subnum <= len(hero.spell_use_list[i].red_dice_list):
                    hero.spell_use_list[i].avail_all("green")
                    for j in range(subnum):
                        hero.spell_use_list[i].red_dice_list[j].activate()
                    hero.spell_use_list[i].direc_decide(namelist, myapp)
                else:
                    myapp.printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
            elif subkinds == "blue":
                try:
                    subnum = int(myapp.inputt("융합할 보조 주사위 개수는?"))
                except ValueError:
                    myapp.printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
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
                    myapp.printt("융합할 보조 주사위 개수를 잘못 입력했습니다.")
                    hero.spell_use_list.pop()
                    return "Error!"
            else:
                myapp.printt("유효한 입력값이 아닙니다.")
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
            myapp.printt('아무래도 푸른 마력 주사위가 부족한 듯 하다.')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'
        elif sum(cls.hero_using_healthdice_list) > hero.health_dice or sum(
                cls.hero_using_healthdice_list) == hero.health_dice and hero.health_dice * Character.healthtodice == hero.health:
            myapp.printt('붉은 마나 주사위를 사용하려 하자, 당신의 심장이 욱신거리기 시작한다!')
            myapp.printt('아무래도 남은 체력을 전부 사용하는것은 좋지 않을 듯 하다...')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'
        elif sum(cls.hero_using_green_list) > hero.act_point:
            myapp.printt('아무래도 초록 마력 주사위가 부족한 듯 하다.')
            cls.hero_using_manadice_list.pop()
            cls.hero_using_green_list.pop()
            cls.hero_using_healthdice_list.pop()
            hero.spell_use_list.pop()
            return 'Error!'

        # 버프 목록을 초기화시킴
        hero.buff_list_init()

        myapp.printt('*')

    @classmethod
    def turn_buff_hero_monster(cls,hero,monsterlist,myapp):
        try:
            myapp.turnbuffte.clear()
            myapp.turnbuffte.append(str(hero.turn_buff_list))
            myapp.mn1turnbuffte.clear()
            myapp.mn1turnbuffte.append(str(monsterlist[0].turn_buff_list))
            myapp.mn2turnbuffte.clear()
            myapp.mn2turnbuffte.append(str(monsterlist[1].turn_buff_list))
            myapp.mn3turnbuffte.clear()
            myapp.mn3turnbuffte.append(str(monsterlist[2].turn_buff_list))
        except IndexError:
            pass

        try:
            myapp.allturnbuffte.clear()
            myapp.allturnbuffte.append(str(hero.all_turn_buff_list))
            myapp.mn1allturnbuffte.clear()
            myapp.mn1allturnbuffte.append(str(monsterlist[0].all_turn_buff_list))
            myapp.mn2allturnbuffte.clear()
            myapp.mn2allturnbuffte.append(str(monsterlist[1].all_turn_buff_list))
            myapp.mn3allturnbuffte.clear()
            myapp.mn3allturnbuffte.append(str(monsterlist[2].all_turn_buff_list))
        except IndexError:
            pass


        if len(hero.all_turn_buff_list) != 0:
            myapp.printt("이번 전투 에(모든 턴에), 당신에게 특수한 효과가 발동되었습니다.")
            for buff in hero.all_turn_buff_list:
                myapp.printt("{0} : {1}".format(buff.name, buff.showname))
            for buff in hero.all_turn_buff_list:
                buff.use(hero,monsterlist,myapp)

        for i in range(len(monsterlist)):
            if len(monsterlist[i].all_turn_buff_list) != 0:
                myapp.printt("이번 전투 에(모든 턴에),{0}번 몬스터 {1}에게 특수한 효과가 발동되었습니다.".format(i, monsterlist[i].name))
                for buff in monsterlist[i].all_turn_buff_list:
                    myapp.printt("{0} : {1}".format(buff.name, buff.showname))
                for buff in monsterlist[i].all_turn_buff_list:
                    buff.use(hero, monsterlist,myapp)



        if len(hero.turn_buff_list) != 0:
            myapp.printt("이번 턴에, 당신에게 특수한 효과가 발동되었습니다.")
            for buff in hero.turn_buff_list[0]:
                myapp.printt("{0} : {1}".format(buff.name, buff.showname))
            for buff in hero.turn_buff_list[0]:
                buff.use(hero,monsterlist,myapp)
            hero.turn_buff_list.pop(0)

        for i in range(len(monsterlist)):
            if len(monsterlist[i].turn_buff_list) != 0:
                myapp.printt("이번 턴에, 적에게 특수한 효과가 발동되었습니다.")
                for buff in monsterlist[i].turn_buff_list[0]:
                    myapp.printt("{0} : {1}".format(buff.name, buff.showname))
                for buff in monsterlist[i].turn_buff_list[0]:
                    buff.use(hero, monsterlist,myapp)
                monsterlist[i].turn_buff_list.pop(0)

    @classmethod
    def observercenter(cls,myapp):
        if ObserverCenter.observing_list != []:
            myapp.printt("이번 전투 에(모든 턴에) 발동에 특수한 조건이 걸려있는 효과가 감지되었습니다.")

            #신문물 시도!
            for var in ObserverCenter.observing_list:
                if var.observer != []:
                    for stack in var.observer:
                        for obslist in stack[1]:
                            for obs in obslist:
                                if obs[5] == True:
                                    obs[6](var.observer,myapp)
                if var.always_observer != []:
                    for obs in var.always_observer:
                        if obs[5] == True:
                            obs[6](var.always_observer,myapp)

            '''
            for var in ObserverCenter.observing_list:
                myapp.printt("{0} : ".format(var.name))
                if var.observer != []:
                    myapp.printt("다음 효과들은 {0}가 1,2,3...회 변경되면 x회 적용되고 나서 사라집니다. 적용 시 조건에 맞지 않으면 발동이 보류됩니다.".format(var.name))
                    for i in range(len(var.observer)):
                        myapp.printt("{0} : {1}".format(var.observer[i][0], var.observer[i][1].showname))
                        test = []
                        for j in range(len(var.observer[i][2])):
                            test.append(len(var.observer[i][2][j]))
                        myapp.printt("x회: {0}".format(test))

                if var.always_observer != []:
                    myapp.printt("다음 효과들은 {0}가 변경되면 이번 전투동안 항상 적용되고 사라지지 않습니다. 적용 시 조건에 맞지 않으면 발동이 보류됩니다.".format(var.name))
                    for j in range(len(var.always_observer)):
                        myapp.printt("{0} : {1}".format(var.always_observer[j][1], var.always_observer[j][3].showname))
            '''


    @classmethod
    def hero_monster_use_resource(cls,hero,monsterlist,i, myapp):# 마법의 사용 대가를 치루는 코드. 전투 중간에 마나나 체력이 부족해졌을 시에 마법 사용을 거부하는 역할도 추가됨.

        try:
            hero.spell_use_list[i].pay_price(hero, monsterlist, myapp)
        except IndexError:
            hero.fault_bool = True
            myapp.faultbtn.setEnabled(False)

        for j in range(len(monsterlist)):
            try:
                monsterlist[j].spell_use_list[i].pay_price(hero, monsterlist, myapp)
            except IndexError:
                monsterlist[j].fault_bool = True
                if j == 0:
                    myapp.mn1faultbtn.setEnabled(False)
                elif j == 1:
                    myapp.mn2faultbtn.setEnabled(False)
                elif j == 2:
                    myapp.mn3faultbtn.setEnabled(False)









    @classmethod
    def roll_hero_monster(cls, i, hero, monsterlist, myapp):  # 영웅과 적의 스킬을 사용,(그 뒤 버프 목록 갱신,) 행동력이 부족하다면 행동 불능상태로 만드는 코드.
        # i는 몇번째 행동인지 인자. (0번째, 1번째...)

        try:
            myapp.spelluselistte.clear()
            for spellname in hero.spell_use_list_mapping("name"):
                myapp.spelluselistte.append(str(spellname))
            myapp.mn1spelluselistte.clear()
            for spellname in monsterlist[0].spell_use_list_mapping("name"):
                myapp.mn1spelluselistte.append(str(spellname))
            myapp.mn2spelluselistte.clear()
            for spellname in monsterlist[1].spell_use_list_mapping("name"):
                myapp.mn2spelluselistte.append(str(spellname))
            myapp.mn3spelluselistte.clear()
            for spellname in monsterlist[2].spell_use_list_mapping("name"):
                myapp.mn3spelluselistte.append(str(spellname))
        except IndexError:
            pass


        try:
            myapp.actionbuffte.clear()
            for buff in hero.buff_list:
                for bu in buff:
                    myapp.actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.actionbuffte.insertPlainText('\n')
            myapp.mn1actionbuffte.clear()
            for buff in monsterlist[0].buff_list:
                for bu in buff:
                    myapp.mn1actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn1actionbuffte.insertPlainText('\n')
            myapp.mn2actionbuffte.clear()
            for buff in monsterlist[1].buff_list:
                for bu in buff:
                    myapp.mn2actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn2actionbuffte.insertPlainText('\n')
            myapp.mn3actionbuffte.clear()
            for buff in monsterlist[2].buff_list:
                for bu in buff:
                    myapp.mn3actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn3actionbuffte.insertPlainText('\n')
        except IndexError:
            pass

        try:
            if hero.fault_bool == False:
                hero.spell_use_list[i].use(hero, monsterlist, myapp)
                hero.buff_list_init()

        except IndexError:  # 인덱스 에러가 뜨면 사용할 마법 인스턴스 리스트 인덱스 길이보다 전투 번째수가 많으므로 행동 불능 상태로 만드는 코드.
            hero.fault_bool = True
            myapp.faultbtn.setEnabled(False)


        for j in range(len(monsterlist)):
            try:
                if monsterlist[j].fault_bool == False:
                    monsterlist[j].spell_use_list[i].use(hero, monsterlist, myapp)
                    monsterlist[j].buff_list_init()

            except IndexError:  # 마찬가지로 행동 불능 상태로 만드는 코드.
                monsterlist[j].fault_bool = True
                if j == 0:
                    myapp.mn1faultbtn.setEnabled(False)
                elif j == 1:
                    myapp.mn2faultbtn.setEnabled(False)
                elif j == 2:
                    myapp.mn3faultbtn.setEnabled(False)





    @classmethod
    def action_buff_hero_monster(cls, i, hero, monsterlist,myapp):

        try:
            if len(hero.buff_list[i]) != 0:
                myapp.printt("이번 행동에, 당신에게 특수한 효과가 부여되었습니다.")
                for j in range(len(hero.buff_list[i])):
                    myapp.printt("{0} : {1}".format(hero.buff_list[i][j].name, hero.buff_list[i][j].showname))
                for j in range(len(hero.buff_list[i])):
                    hero.buff_list[i][j].use(hero, monsterlist,myapp)

        except IndexError:
            hero.fault_bool = True
            myapp.faultbtn.setEnabled(False)

        for j in range(len(monsterlist)):
            try:
                if len(monsterlist[j].buff_list[i]) != 0:
                    myapp.printt("이번 행동에, {0}번째 적 {1} 에게 특수한 효과가 부여되었습니다.".format(j, monsterlist[j].name))
                    for p in range(len(monsterlist[j].buff_list[i])):
                        myapp.printt("{0} : {1}".format(monsterlist[j].buff_list[i][p].name, monsterlist[j].buff_list[i][p].showname))
                    for p in range(len(monsterlist[j].buff_list[i])):
                        monsterlist[j].buff_list[i][p].use(hero, monsterlist,myapp)


            except IndexError:
                monsterlist[j].fault_bool = True
                if j == 0:
                    myapp.mn1faultbtn.setEnabled(False)
                elif j == 1:
                    myapp.mn2faultbtn.setEnabled(False)
                elif j == 2:
                    myapp.mn3faultbtn.setEnabled(False)

        try:
            myapp.actionbuffte.clear()
            for buff in hero.buff_list:
                for bu in buff:
                    myapp.actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.actionbuffte.insertPlainText('\n')
            myapp.mn1actionbuffte.clear()
            for buff in monsterlist[0].buff_list:
                for bu in buff:
                    myapp.mn1actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn1actionbuffte.insertPlainText('\n')
            myapp.mn2actionbuffte.clear()
            for buff in monsterlist[1].buff_list:
                for bu in buff:
                    myapp.mn2actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn2actionbuffte.insertPlainText('\n')
            myapp.mn3actionbuffte.clear()
            for buff in monsterlist[2].buff_list:
                for bu in buff:
                    myapp.mn3actionbuffte.insertPlainText(bu.name + bu.showname)
                myapp.mn3actionbuffte.insertPlainText('\n')
        except IndexError:
            pass


    @classmethod
    def atk_def_skill_to_character(cls,i,hero,monsterlist,myapp): #최종 공격력과 방어력(캐릭터 공방력)을 결정.
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

        try:
            myapp.attackte.clear()
            for i in range(len(hero.attack)):
                myapp.attackte.append(str(hero.direction[i]) + " / " + str(hero.attack[i]))
            myapp.defencelied.setText("0")
            myapp.defencelied.setText(str(int(myapp.defencelied.text()) + hero.defence))

            myapp.mn1attackte.clear()
            for i in range(len(monsterlist[0].attack)):
                myapp.mn1attackte.append(str(monsterlist[0].direction[i]) + " / " + str(monsterlist[0].attack[i]))
            myapp.mn1defencelied.setText("0")
            myapp.mn1defencelied.setText(str(int(myapp.mn1defencelied.text()) + monsterlist[0].defence))

            myapp.mn2attackte.clear()
            for i in range(len(monsterlist[1].attack)):
                myapp.mn2attackte.append(str(monsterlist[1].direction[i]) + " / " + str(monsterlist[1].attack[i]))
            myapp.mn2defencelied.setText("0")
            myapp.mn2defencelied.setText(str(int(myapp.mn2defencelied.text()) + monsterlist[1].defence))

            myapp.mn3attackte.clear()
            for i in range(len(monsterlist[2].attack)):
                myapp.mn3attackte.append(str(monsterlist[2].direction[i]) + " / " + str(monsterlist[2].attack[i]))
            myapp.mn3defencelied.setText("0")
            myapp.mn3defencelied.setText(str(int(myapp.mn3defencelied.text()) + monsterlist[2].defence))
        except IndexError:
            pass



    @classmethod
    def small_fight(cls, hero, monsterlist,myapp):  # 방어력과 공격력을 서로 겨루게 한 뒤 피해를 입히거나 입게 하는 메소드. 마찬가지로 행동 불능에 따른 상황 역시 고려한다.
        monsternamelist = []
        for monster in monsterlist:
            monsternamelist.append(monster.name)
        myapp.printt("전투가 시작된다.")

        if hero.fault_bool == False:
            myapp.printt("당신은 몬스터들에게 공격을 할 준비를 한다.")
            if len(hero.attack) != len(hero.direction):
                raise Exception

            for i in range(len(hero.attack)):
                monster = monsterlist[monsternamelist.index(hero.direction[i])]
                index = monsternamelist.index(hero.direction[i])
                myapp.printt("당신|공격력 {0} >>|| 방어력 {1}|몬스터 ({2}) ".format(hero.attack[i],monster.defence, hero.direction[i]))
                if hero.attack[i] > monster.defence:
                    monster.change_health(monster.health + monster.defence - hero.attack[i],monsterlist,myapp)
                    monster.defence = 0
                    myapp.printt("방어 관통! 적에게 데미지가 들어왔다.")
                elif hero.attack[i] <= monster.defence:
                    monster.defence -= hero.attack[i]
                    myapp.printt("공격 막힘! 적의 방어력이 대신 깎였다.")
                if index == 0:
                    for i in range(len(monsterlist[index].attack)):
                        myapp.mn1attackte.append(
                            str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                    myapp.mn1defencelied.setText("0")
                    myapp.mn1defencelied.setText(str(int(myapp.mn1defencelied.text()) + monsterlist[index].defence))
                elif index == 1:
                    for i in range(len(monsterlist[index].attack)):
                        myapp.mn2attackte.append(
                            str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                    myapp.mn2defencelied.setText("0")
                    myapp.mn2defencelied.setText(str(int(myapp.mn2defencelied.text()) + monsterlist[index].defence))
                elif index == 2:
                    for i in range(len(monsterlist[index].attack)):
                        myapp.mn3attackte.append(
                            str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                    myapp.mn3defencelied.setText("0")
                    myapp.mn3defencelied.setText(str(int(myapp.mn3defencelied.text()) + monsterlist[index].defence))
        else:
            myapp.printt("당신은 행동 불능, 몬스터들에게 공격할 수 없었다.")
            if hero.attack != [] and hero.direction != []:
                myapp.printt("그러나, 당신에겐 왠지 모르게 공격력이 부여되어 있다.")
                if len(hero.attack) != len(hero.direction):
                    raise Exception

                for i in range(len(hero.attack)):
                    monster = monsterlist[monsternamelist.index(hero.direction[i])]
                    index = monsternamelist.index(hero.direction[i])
                    myapp.printt(
                        "당신|공격력 {0} >>|| 방어력 {1}|몬스터 ({2}) ".format(hero.attack[i], monster.defence, hero.direction[i]))
                    if hero.attack[i] > monster.defence:
                        monster.change_health(monster.health + monster.defence - hero.attack[i],monsterlist,myapp)
                        monster.defence = 0
                        myapp.printt("방어 관통! 적에게 데미지가 들어왔다.")
                    elif hero.attack[i] <= monster.defence:
                        monster.defence -= hero.attack[i]
                        myapp.printt("공격 막힘! 적의 방어력이 대신 깎였다.")
                    if index == 0:
                        myapp.mn1attackte.clear()
                        for i in range(len(monsterlist[index].attack)):
                            myapp.mn1attackte.append(str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                        myapp.mn1defencelied.setText('0')
                        myapp.mn1defencelied.setText(str(int(myapp.mn1defencelied.text()) + monsterlist[index].defence))
                    elif index == 1:
                        myapp.mn2attackte.clear()
                        for i in range(len(monsterlist[index].attack)):
                            myapp.mn2attackte.append(str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                        myapp.mn1defencelied.setText('0')
                        myapp.mn2defencelied.setText(str(int(myapp.mn2defencelied.text()) + monsterlist[index].defence))
                    elif index == 2:
                        myapp.mn3attackte.clear()
                        for i in range(len(monsterlist[index].attack)):
                            myapp.mn3attackte.append(str(monsterlist[index].direction[i]) + " / " + str(monsterlist[index].attack[i]))
                        myapp.mn1defencelied.setText('0')
                        myapp.mn3defencelied.setText(str(int(myapp.mn3defencelied.text()) + monsterlist[index].defence))

        myapp.printt("이제, 몬스터들이 당신에게 공격을 할 준비를 한다.")
        for i in range(len(monsterlist)):
            ismonsatknone = False
            if monsterlist[i].attack == []:
                ismonsatknone = True
            if monsterlist[i].fault_bool == False:
                if ismonsatknone == True:
                    myapp.printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, 0, monsterlist[i].name))

                else:
                    myapp.printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, monsterlist[i].attack[0], monsterlist[i].name))

                    if monsterlist[i].attack[0] > hero.defence:
                        hero.change_health(hero.health + hero.defence - monsterlist[i].attack[0],monsterlist,myapp)
                        hero.defence = 0
                        myapp.printt("방어 관통! 당신에게 데미지가 들어갔다.")
                    elif monsterlist[i].attack[0] <= hero.defence:
                        hero.defence -= monsterlist[i].attack[0]
                        myapp.printt("공격 막힘! 당신의 방어력이 대신 깎였다.")
                    myapp.attackte.clear()
                    for i in range(len(hero.attack)):
                        myapp.attackte.append(str(hero.direction[i]) + " / " + str(hero.attack[i]))
                    myapp.defencelied.setText("0")
                    myapp.defencelied.setText(str(int(myapp.defencelied.text()) + hero.defence))

            else:
                myapp.printt("몬스터 {0}은 행동 불능, 공격하지 못한다.".format(monsterlist[i].name))
                if monsterlist[i].attack != [] and monsterlist[i].direction != []:
                    myapp.printt("그러나, 적에겐 왠지 모르게 공격력이 부여되어 있다.")
                    ismonsatknone = False
                    if monsterlist[i].attack == []:
                        ismonsatknone = True
                    if monsterlist[i].fault_bool == False:
                        if ismonsatknone == True:
                            myapp.printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, 0, monsterlist[i].name))

                        else:
                            myapp.printt("당신|방어력 {0} ||<< 공격력 {1}|몬스터({2})".format(hero.defence, monsterlist[i].attack[0],
                                                                             monsterlist[i].name))

                            if monsterlist[i].attack[0] > hero.defence:
                                hero.change_health(hero.health + hero.defence - monsterlist[i].attack[0],monsterlist,myapp)
                                hero.defence = 0
                                myapp.printt("방어 관통! 당신에게 데미지가 들어갔다.")
                            elif monsterlist[i].attack[0] <= hero.defence:
                                hero.defence -= monsterlist[i].attack[0]
                                myapp.printt("공격 막힘! 당신의 방어력이 대신 깎였다.")
                            myapp.attackte.clear()
                            for i in range(len(hero.attack)):
                                myapp.attackte.append(str(hero.direction[i]) + " / " + str(hero.attack[i]))
                            myapp.defencelied.setText('0')
                            myapp.defencelied.setText(str(int(myapp.defencelied.text()) + hero.defence))



    @classmethod
    def lose_win_define(cls,hero,monsterlist,myapp): #체력 상태에 따른 승패를 판정하는 메소드. 승패 bool 속성을 건드린다.
        indexlist = []
        if hero.health <= 0:
            myapp.printt('당신은 몬스터에게 패배했습니다...')
            myapp.printt('game over!')
            raise Exception("패배!")
        for i in range(len(monsterlist)):
            if monsterlist[i].health <= 0:
                myapp.printt("몬스터 {0}, 넉다운!".format(monsterlist[i].name))
                monsterlist[i] = None
                indexlist.append(i)
        i = 0
        while i < len(monsterlist):
            if monsterlist[i] == None:
                monsterlist.pop(i)
                i -= 1
            i += 1

        for index in indexlist:
            if index == 0:
                cls.clear_mn1GUI_all(myapp)
            elif index == 1:
                cls.clear_mn2GUI_all(myapp)
            elif index == 2:
                cls.clear_mn2GUI_all(myapp)


        if monsterlist == []:
            myapp.printt("당신은 몬스터들로부터 승리하였습니다!")
            myapp.printt("승리!")
            cls.fight_end = True

    @classmethod
    def use_bag(cls,hero,monsterlist,myapp):
        open_or_not = myapp.inputt("가방을 여시겠습니까? (y/n)")

        myapp.bagte.clear()
        for itemname in hero.bag_name_list:
            myapp.bagte.append(itemname)
        myapp.moneylied.setText(str(hero.money))

        if open_or_not == "y":
            while len(hero.bag_list) != 0:
                use_item_name = myapp.inputt("어떤 아이템을 사용하시겠습니까? (가방을 닫을려면 0)")

                if use_item_name == "0":
                    myapp.printt("가방을 닫았습니다.")
                    break

                for i in hero.bag_list:
                    if i.name == use_item_name:
                        i.use(hero,monsterlist , myapp)
                        break
                    elif use_item_name != "0" and i.name != use_item_name and hero.bag_list.index(i) == len(hero.bag_list) - 1:  # 해당 아이템이 가방에 없을 경우
                        myapp.printt("잘못 입력하였습니다.")

                myapp.bagte.clear()
                for itemname in hero.bag_name_list:
                    myapp.bagte.append(itemname)

        myapp.bagte.clear()
        for itemname in hero.bag_name_list:
            myapp.bagte.append(itemname)
        myapp.moneylied.setText(str(hero.money))




##############################################진짜 전투 부분.지금까지 사용한 모든 메서드 총집합!##########################
    @classmethod
    def big_fight(cls,hero,monsterlist,monster_brainlist,monster_availbrainlist,myapp): #한 턴을 진행한다.
        cls.nTurn += 1
        myapp.printt("{0}번째 턴!".format(cls.nTurn))

        #전투 참가자들의 이름을 띄운다.
        myapp.namelied.setText("용사")
        try:
            myapp.mn1namelied.setText(monsterlist[0].name)
            myapp.mn2namelied.setText(monsterlist[1].name)
            myapp.mn3namelied.setText(monsterlist[2].name)
        except IndexError:
            pass


        #사용한 변수들을 초기화한다.
        cls.clear_nomal_all(hero, monsterlist)

        #캐릭터들의 파라미터를 초기화한다.
        cls.clear_character_all(hero, monsterlist)

        #행동 관련 파라미터를 초기화한다.
        cls.clear_action_all(hero,monsterlist,myapp)

        #턴 관련(주로 버프들)의 GUI 출력상태를 초기화한다.
        cls.clear_turn_all(hero, monsterlist, myapp)

        # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        myapp.printt('*')
        cls.show_stat_and_spell_list(hero, monsterlist,myapp)
        myapp.printt('*')

        # 가방
        cls.use_bag(hero,monsterlist,myapp)

        # 나와 상대의 스탯을 출력하고, 사용 가능한 마법의 이름 리스트를 채운 뒤 출력.
        myapp.printt('*')
        cls.show_stat_and_spell_list(hero, monsterlist,myapp)
        myapp.printt('*')
        # 마법의 설명을 출력.
        myapp.printt("당신이 사용 가능한 마법들의 설명을 무조건 들으십쇼.")
        myapp.skilscriptte.clear()
        for spell in hero.spell_list:

            myapp.skilscriptte.append('*')
            myapp.skilscriptte.append("스킬 이름:" + spell.name)
            myapp.skilscriptte.append("스킬 상세:" + spell.showname)
            myapp.skilscriptte.append("스킬 설명:" + spell.crazyname)
            myapp.skilscriptte.append('*')
        # 턴 단위의 버프가 앞으로 적용된다면, 이를 출력한다
        cls.turn_buff_list_show(hero,monsterlist,myapp)

        # 특정 조건 만족시 발동되는 효과가 있다면, 이를 출력한다.
        cls.observercenter(myapp)

        for i in range(len(monsterlist)):
            # >>적이 사용할 스킬 인스턴스 리스트를 채우기. 이때 행동 단위 버프 갱신
            cls.monster_spell_list_decide(monsterlist[i], monster_brainlist[i])

            # >>적이 사용할 스킬 인스턴스 리스트 내의 주사위를 활성화시킴(의미:사용할 주사위 결정)
            cls.monster_dice_activate(monsterlist[i], monster_availbrainlist[i])


        #>>내가 사용할 스킬 인스턴스 리스트를 채우기. 그리고 내부 주사위 활성화시키기.(의미: 사용할 주사위 결정) 이때 행동 단위 버프 갱신
        j = 0
        while (hero.act_point > sum(cls.hero_using_green_list)):
            myapp.printt('*')
            cls.hero_spell_list_show(hero,myapp) # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.
            myapp.printt('*')
            namelist = ['hero']
            for i in range(len(monsterlist)):
                namelist.append(monsterlist[i].name)

            if cls.hero_spell_list_decide(hero,j,namelist,myapp) != None: # 내가 사용할 스킬 리스트를 채우는 메소드. 사용 예정인 마나, 체력, 행동점수
        #주사위의 개수를 저장하는 리스트를 채운 뒤, 이를 통해 유저가 입력한 스킬을 사용하기에 자원이 부족하다면 에러 문자열 출력. 또한,
        #스킬 인스턴스들 내부 주사위들을 유저가 원하는 만큼 규칙에 의거해 활성화시킴. 이를 통해 주사위를 얼마나 사용할것인지 예정시킴
                pass
            else:
                j += 1
        cls.hero_spell_list_show(hero,myapp) # 사용 예정인 마법, 마나, 체력을 출력하는 메소드.

        #턴 단위 버프를 적용한다.
        cls.turn_buff_hero_monster(hero,monsterlist,myapp)


        i = 0
        # 선택한 주문대로 전투를 시작한다.
        while True: #한 행동 진행.
            # 행동불능 상태 복구
            hero.fault_bool = False
            myapp.faultbtn.setEnabled(True)
            for j in range(len(monsterlist)):
                monsterlist[j].fault_bool = False
            myapp.mn1faultbtn.setEnabled(True)
            myapp.mn2faultbtn.setEnabled(True)
            myapp.mn3faultbtn.setEnabled(True)


            # 미리 행동불능 여부 재판단
            if len(hero.spell_use_list) <= i:
                hero.fault_bool = True
                myapp.faultbtn.setEnabled(False)
            for j in range(len(monsterlist)):
                if len(monsterlist[j].spell_use_list) <= i:
                    monsterlist[j].fault_bool = True
                    if j == 0:
                        myapp.mn1faultbtn.setEnabled(True)
                    elif j == 1:
                        myapp.mn2faultbtn.setEnabled(True)
                    elif j == 2:
                        myapp.mn3faultbtn.setEnabled(True)


            #둘 다 행동불능에 빠졌을 경우 이번 턴 종료
            monsterfaultall = True
            for monster in monsterlist:
                if monster.fault_bool == False:
                    monsterfaultall = False
            if hero.fault_bool == True and monsterfaultall == True:
                # 전투 종료시엔 반드시 행동력 초기화,행동불능 상태 복구
                hero.fault_bool = False
                myapp.faultbtn.setEnabled(True)

                hero.act_point = hero.max_act_point
                for i in range(len(monsterlist)):
                    monsterlist[i].fault_bool = False
                    monsterlist[i].act_point = monsterlist[i].max_act_point
                    if i == 0:
                        myapp.mn1faultbtn.setEnabled(True)
                    elif i == 1:
                        myapp.mn2faultbtn.setEnabled(True)
                    elif i == 2:
                        myapp.mn3faultbtn.setEnabled(True)

                myapp.printt('=============================================================')
                break

            # n번째 행동!
            myapp.printt('=============================================================')


            myapp.printt('{0}번째 행동!'.format(i))

            # 대가 사용, 활성화된 주사위를 참고하여.
            cls.hero_monster_use_resource(hero, monsterlist,i, myapp)  # 마법의 사용 대가를 치루는 코드. 전투 중간에 마나나 체력이 부족해졌을 시에 마법 사용을 거부하는 역할도 추가됨.

            # 주사위 굴리기 and 사용하기, 표시하기, 스킬로 인해 발생한 공격력 및 방어력 표시와 기타 잡다한 스킬 사용시 표시해야할 것들 표시. 행동 단위 버프 1회 더 갱신
            myapp.printt('')
            cls.roll_hero_monster(i,hero,monsterlist, myapp) # 영웅과 적의 방어/공격량을 정하고(주사위를 실질적으로 "사용"), 행동력이 부족하다면 행동 불능상태로 만드는 코드.

            # 행동 단위에 적용되는 버프/디버프 사용
            myapp.printt('')
            cls.action_buff_hero_monster(i, hero, monsterlist,myapp)

            #최종 공격력, 방어력을 결정
            myapp.printt('')
            cls.atk_def_skill_to_character(i,hero,monsterlist,myapp)

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
            myapp.printt('')
            cls.small_fight(hero, monsterlist,myapp) #방어력과 공격력을 서로 겨루게 한 뒤 피해를 입히거나 입게 하는 메소드. 행동 불능에 따른 상황을 고려한다.

            #공격력, 방어력과 같은, 매 행동마다 초기화 해야 하는 변수들만 따로 다시 초기화 한다.
            cls.clear_action_all(hero,monsterlist,myapp)

            # 승패를 판단한다. #체력 상태에 따른 승패를 판정하는 메소드. 승패 bool 속성을 건드린다.
            cls.lose_win_define(hero,monsterlist,myapp)


            if cls.fight_end == True:
                # 전투 종료시엔 반드시 행동력 초기화
                hero.act_point = hero.max_act_point
                # 행동불능 상태 복구
                hero.fault_bool = False
                myapp.faultbtn.setEnabled(True)
                break

            #몇번째인지 나타내주는 i에 1더하기.
            i += 1





