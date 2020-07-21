from tool import *

class Character:
    manatodice = 5 # 마나주사위 1개는 마나 5
    healthtodice = 5 # 체력주사위 1개는 체력 5
    def __init__(self, name, health, mana, max_act_point):
        self.name = name
        self.health = health
        self.health_dice = 0
        self.change_health(None)

        self.mana = UpgradedVar(name + ".mana", mana)
        self.mana_dice = 0
        self.change_mana(None)

        self.max_act_point = max_act_point
        self.act_point = max_act_point

        self.spell_list = []
        self.spell_use_list = []
        self.buff_list = []
        self.all_turn_buff_list = []
        self.turn_buff_list = []

        self.atk_bool = True
        self.fault_bool = False
        self.death = False

        self.defence = 0
        self.attack = []
        self.direction = []

        self.money = 1000
        self.bag_list = []
        self.bag_name_list = []

    def show_stat(self,monsterlist,myapp):
        if self not in monsterlist:
            myapp.healthlied.setText(str(self.health))
            myapp.reddicelied.setText(str(self.health_dice))
            myapp.manalied.setText(str(self.mana.value))
            myapp.bluedicelied.setText(str(self.mana_dice))
            myapp.maxactlied.setText(str(self.max_act_point))
            myapp.actlied.setText(str(self.act_point))
        elif self in monsterlist:
            index = monsterlist.index(self)
            if index == 0:
                myapp.mn1healthlied.setText(str(self.health))
                myapp.mn1reddicelied.setText(str(self.health_dice))
                myapp.mn1manalied.setText(str(self.mana.value))
                myapp.mn1bluedicelied.setText(str(self.mana_dice))
                myapp.mn1maxactlied.setText(str(self.max_act_point))
                myapp.mn1actlied.setText(str(self.act_point))
            elif index == 1:
                myapp.mn2healthlied.setText(str(self.health))
                myapp.mn2reddicelied.setText(str(self.health_dice))
                myapp.mn2manalied.setText(str(self.mana.value))
                myapp.mn2bluedicelied.setText(str(self.mana_dice))
                myapp.mn2maxactlied.setText(str(self.max_act_point))
                myapp.mn2actlied.setText(str(self.act_point))
            elif index == 2:
                myapp.mn3healthlied.setText(str(self.health))
                myapp.mn3reddicelied.setText(str(self.health_dice))
                myapp.mn3manalied.setText(str(self.mana.value))
                myapp.mn3bluedicelied.setText(str(self.mana_dice))
                myapp.mn3maxactlied.setText(str(self.max_act_point))
                myapp.mn3actlied.setText(str(self.act_point))


    def add_spell(self, spell):
        self.spell_list.append(spell)

    def use_spell(self, spell_name):  # self.spell_list 에서 spell_name을 name 속성으로 가진 스킬 클래스를 찾고 해당 스킬 클래스의 인스턴스를 반환하는 메서드
        spell_name_list = []
        for i in self.spell_list:
            spell_name_list.append(i.name)
        if spell_name in spell_name_list:
            index = spell_name_list.index(spell_name)
        else:
            return "Error!"
        return self.spell_list[index]()

    def buff_list_init(self): #버프 리스트의 길이를 사용할 마법 리스트의 길이로 맞춘다.
            delta = len(self.spell_use_list) - len(self.buff_list)
            if delta < 0:
                return "Error!"
            elif delta == 0:
                return
            for j in range(delta):
                self.buff_list.append([])

    def buff_list_add(self, actindex, buff): #버프 리스트의 actindex 번째 행동에 버프를 추가한다.
        if actindex < len(self.buff_list):
            self.buff_list[actindex].append(buff)
        else:
            return "Error!"

    def buff_list_in(self, buff): #버프 리스트에 해당 버프가 있는지 알아낸다.
        buffin = False
        for list in self.buff_list:
            if buff in list:
                buffin = True
        return buffin

    def buff_list_find(self, buff): # 버프 리스트에서 해당 버프가 몇번째 행동의 버프인지 찾아낸다.
        buffindex = -1
        for i in range(len(self.buff_list)):
            if buff in self.buff_list[i]:
                buffindex = i
        if buffindex == -1:
            return "Error!"
        return buffindex

    def turn_buff_list_add(self,priority,buff): #참고: priority는 0부터 시작하는 실행 우선순위. "2차원형 스택"
        if priority < len(self.turn_buff_list):
            self.turn_buff_list[priority].append(buff)
        elif priority >= len(self.turn_buff_list):
            delta = priority - len(self.turn_buff_list) + 1
            if delta < 0:
                return "Error!"
            for i in range(delta):
                self.turn_buff_list.append([])
            self.turn_buff_list[priority].append(buff)

    def turn_buff_list_in(self, buff):
        buffin = False
        for list in self.turn_buff_list:
            if buff in list:
                buffin = True
        return buffin

    def turn_buff_list_find(self, buff):
        buffindex = -1
        for i in range(len(self.turn_buff_list)):
            if buff in self.turn_buff_list[i]:
                buffindex = i
        if buffindex == -1:
            return "Error!"
        return buffindex

    def change_health(self, health, monsterlist=None, myapp=None):  # 음수를 넣으면 에러 반환, 이외의 0과 양의 정수를 넣으면 그것으로 체력값 변동, None 넣으면 갱신
        if health == None:
            self.health_dice = int(self.health / Character.healthtodice)
        elif health <= 0:
            self.health = 0
            self.health_dice = 0
            self.fault_bool = True
            return 'Error!'
        elif health > 0:
            self.health = health
            self.health_dice = int(self.health / Character.healthtodice)

        if monsterlist == None or myapp == None:
            return

        index = None
        if self in monsterlist:
            index = monsterlist.index(self)
        else:
            index = -1

        if index == -1:
            myapp.healthlied.setText(str(self.health))
            myapp.reddicelied.setText(str(self.health_dice))
        elif index == 0:
            myapp.mn1healthlied.setText(str(self.health))
            myapp.mn1reddicelied.setText(str(self.health_dice))
        elif index == 1:
            myapp.mn2healthlied.setText(str(self.health))
            myapp.mn2reddicelied.setText(str(self.health_dice))
        elif index == 2:
            myapp.mn3healthlied.setText(str(self.health))
            myapp.mn3reddicelied.setText(str(self.health_dice))



    def change_mana(self, mana,monsterlist=None, myapp=None):  # 음수를 넣으면 시스템 에러를 띄운다. 따라서 이에 대한 예외처리를 반드시 해야만 한다.
        if mana == None:
            self.mana_dice = int(self.mana.value / Character.manatodice)
        elif mana < 0:
            raise Exception("음수의 마나값을 입력받았습니다. 관리자 호출 요망.")
        elif mana >= 0:
            self.mana.change(mana)
            self.mana_dice = int(self.mana.value / Character.manatodice)

        if monsterlist == None or myapp == None:
            return

        index = None
        if self in monsterlist:
            index = monsterlist.index(self)
        else:
            index = -1

        if index == -1:
            myapp.manalied.setText(str(self.mana.value))
            myapp.bluedicelied.setText(str(self.mana_dice))
        elif index == 0:
            myapp.mn1manalied.setText(str(self.mana.value))
            myapp.mn1bluedicelied.setText(str(self.mana_dice))
        elif index == 1:
            myapp.mn2manalied.setText(str(self.mana.value))
            myapp.mn2bluedicelied.setText(str(self.mana_dice))
        elif index == 2:
            myapp.mn3manalied.setText(str(self.mana.value))
            myapp.mn3bluedicelied.setText(str(self.mana_dice))


    def change_actpoint(self, actpoint,monsterlist=None, myapp=None):
        if actpoint == None:
            pass
        elif actpoint < 0:
            self.act_point = 0
            return "Error!"
        elif actpoint >= 0:
            self.act_point = actpoint

        if monsterlist == None or myapp == None:
            return

        index = None
        if self in monsterlist:
            index = monsterlist.index(self)
        else:
            index = -1

        if index == -1:
            myapp.maxactlied.setText(str(self.max_act_point))
            myapp.actlied.setText(str(self.act_point))
        elif index == 0:
            myapp.mn1maxactlied.setText(str(self.max_act_point))
            myapp.mn1actlied.setText(str(self.act_point))
        elif index == 1:
            myapp.mn2maxactlied.setText(str(self.max_act_point))
            myapp.mn2actlied.setText(str(self.act_point))
        elif index == 2:
            myapp.mn3maxactlied.setText(str(self.max_act_point))
            myapp.mn3actlied.setText(str(self.act_point))

        #주의. 항상 체력을 바꿔서 체력 주사위를 바꿀 것. 즉, 방어 주문을 사용할 시에 그 댓가를 self.health_dice 의 값을 직접
        #바꾸어서 치루게 하면 오류 발생. 반드시 주사위 사용 수 * 환산비율 만큼의 체력을 use_health 메서드로 없애는 식으로 접근할것.

        #주의 2. 항상 change류 함수 2가지는 if ...리턴값... != None 문과 같이 사용하여 'Error!'를 어떻게 처리할지 결정할것. 예를 들어서, 마나를 소모해서
        #주문을 쓰려 하는데 마나가 부족한 상황이면 그냥 넘기면 될 것이고, 최후의 일격으로 체력이 바닥났다면 게임을 끝내야할 것이다.

    def spell_use_list_mapping(self, spell_attribute_str):
        temp = []
        for spell in self.spell_use_list:
            temp.append(eval("spell." + spell_attribute_str))
        return temp

    def spell_list_mapping(self, spell_attribute_str):
        temp = []
        for spell in self.spell_list:
            temp.append(eval("spell." + spell_attribute_str))
        return temp

    def spell_use_list_initialize(self):
        self.spell_use_list = []

    def atk_initialize(self):
        self.atk_bool = True

    def fault_initialize(self):
        self.fault_bool = False

    def death_initialize(self):
        self.death = False





class Spell:
    name = None
    main_resource_kinds = None
    showname = None
    crazyname = None

    blue_roll = False
    red_roll = False
    green_roll = False
    only_one_green = False

    temp_direc = []
    temp_atk = []
    temp_def = 0


    ismother = True

    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def __init__(self,cls):  # ex) (라이트닝 슛, - , 2d+1) 즉 전부 문자열로 받아야함. # u
        self.name = cls.name
        self.main_resource_kinds = cls.main_resource_kinds
        self.showname = cls.showname
        self.crazyname = cls.crazyname

        self.blue_roll = cls.blue_roll
        self.red_roll = cls.red_roll
        self.green_roll = cls.green_roll
        self.only_one_green = cls.only_one_green

        self.temp_atk = copy.copy(cls.temp_atk)
        self.temp_direc = copy.copy(cls.temp_direc)
        self.temp_def = cls.temp_def

        self.ismother = True

        self.red_dice_list = copy.deepcopy(cls.red_dice_list)
        self.blue_dice_list = copy.deepcopy(cls.blue_dice_list)
        self.green_dice_list = copy.deepcopy(cls.green_dice_list)

    def copy(self):
        copyed = copy.deepcopy(self)
        copyed.ismother = False
        return copyed

    def avail_all(self, name):
        if name == "red":
            for i in range(len(self.red_dice_list)):
                self.red_dice_list[i].activate()
        elif name == "blue":
            for i in range(len(self.blue_dice_list)):
                self.blue_dice_list[i].activate()
        elif name == "green":
            for i in range(len(self.green_dice_list)):
                self.green_dice_list[i].activate()

    def roll_all(self,name):
        if name == "red":
            for i in range(len(self.red_dice_list)):
                self.red_dice_list[i].roll()
        elif name == "blue":
            for i in range(len(self.blue_dice_list)):
                self.blue_dice_list[i].roll()
        elif name == "green":
            for i in range(len(self.green_dice_list)):
                self.green_dice_list[i].roll()

    def roll_all_color(self):
        if self.red_roll == True:
            self.roll_all("red")
        if self.blue_roll == True:
            self.roll_all("blue")
        if self.green_roll == True:
            self.roll_all("green")

    def pay_price(self,hero,monsterlist,myapp):
        owner = None
        ownertype = ""
        for i in range(len(monsterlist)):
            if self in monsterlist[i].spell_use_list:
                owner = monsterlist[i]
                ownertype = "monster"
        if self in hero.spell_use_list:
            owner = hero
            ownertype = "hero"
        if owner == None:
            raise Exception("parameter_class-Spell-pay_price")



        if owner.fault_bool == True:
            myapp.printt('당신은 가만히 있었다...')
        else:
            myapp.printt('{0}을 사용하는 대가는... {1} 붉은 마력 주사위, {2} 푸른 마력 주사위, {3} 초록 마력 주사위.'.format(self.name,
                                                                                          self.avail_count("red"),
                                                                                          self.avail_count("blue"),
                                                                                          self.avail_count("green")))
            if owner.mana.value + (-1) * self.avail_count("blue") * Character.manatodice < 0: # .change_mana메서드는 바꿀 마나가 음수면 경고 문자열 출력하므로, 이를 이용.
                myapp.printt('그러나 대가를 치를 푸른 마력 주사위가 부족하여 아무런 행동도 할 수 없었다...')
                owner.fault_bool = True
                return
            elif owner.health + (-1) * self.avail_count("red") * Character.healthtodice <= 0:
                myapp.printt('그러나 대가를 치를 붉은 마력 주사위가 부족하여 아무런 행동도 할 수 없었다...')
                owner.fault_bool = True
                return
            elif owner.act_point - self.avail_count("green") < 0:
                myapp.printt('그러나 대가를 치를 초록 마력 주사위가 부족하여 아무런 행동도 할 수 없었다...')
                owner.fault_bool = True
                return

            owner.change_mana(owner.mana.value + (-1) * self.avail_count("blue") * Character.manatodice,monsterlist,myapp)
            owner.change_health(owner.health + (-1) * self.avail_count("red") * Character.healthtodice,monsterlist,myapp)
            owner.change_actpoint(owner.act_point - self.avail_count("green"),monsterlist,myapp)

            owner.show_stat(monsterlist,myapp)





    def get_dice_num_list(self, name):
        d = []
        if name == "red":
            for dice in self.red_dice_list:
                if dice.available == True:
                    d.append(dice.num)
        elif name == "blue":
            for dice in self.blue_dice_list:
                if dice.available == True:
                    d.append(dice.num)
        elif name == "green":
            for dice in self.green_dice_list:
                if dice.available == True:
                    d.append(dice.num)
        return d

    def avail_count(self, name):
        availablelist = []
        if name == "red":
            for dice in self.red_dice_list:
                availablelist.append(dice.available)
        elif name == "blue":
            for dice in self.blue_dice_list:
                availablelist.append(dice.available)
        elif name == "green":
            for dice in self.green_dice_list:
                availablelist.append(dice.available)
        return availablelist.count(True)

    def use_before_calc(self,hero,monsterlist,myapp):
        index = None
        for monster in monsterlist:
            if self in monster.spell_use_list:
                myapp.printt("몬스터 {0} 은(는) {1}을 시전했다.".format(monster.name, self.name))
                myapp.printt("이윽고는 당신을 향해,", end='')
                index = monsterlist.index(monster)

        if self in hero.spell_use_list:
            myapp.printt("당신은 {0}을 시전했다.".format(self.name))
            myapp.printt("주문 시전을 위해,", end='')
            index = -1

        no_roll = True
        if self.avail_count("red") != 0 and self.red_roll == True:
            myapp.printt("차분하게 붉은 마력 주사위를 굴렸다.")
            myapp.printt("{0}(들)이 나왔다!".format(self.get_dice_num_list("red")))
            no_roll = False
        if self.avail_count("blue") != 0 and self.blue_roll == True:
            myapp.printt("차분하게 푸른 마력 주사위를 굴렸다.")
            myapp.printt("{0}(들)이 나왔다!".format(self.get_dice_num_list("blue")))
            no_roll = False
        if self.avail_count("green") != 0 and self.avail_count("green") != 1 and self.green_roll == True:
            myapp.printt("차분하게 초록 마력 주사위를 굴렸다.")
            temp = self.get_dice_num_list("green")
            temp.pop(0)
            myapp.printt("{0}(들)이 나왔다!".format(temp))
            no_roll = False
        if no_roll == True:
            myapp.printt("음...아무런 주사위도 굴리지 않았다.")


        if index == -1:
            myapp.redrollresultlied.setText(str(self.get_dice_num_list("red")))
            myapp.bluerollresultlied.setText(str(self.get_dice_num_list("blue")))
            myapp.greenrollresultlied.setText(str(self.get_dice_num_list("green")))
        elif index == 0:
            myapp.mn1redrollresultlied.setText(str(self.get_dice_num_list("red")))
            myapp.mn1bluerollresultlied.setText(str(self.get_dice_num_list("blue")))
            myapp.mn1greenrollresultlied.setText(str(self.get_dice_num_list("green")))
        elif index == 1:
            myapp.mn2redrollresultlied.setText(str(self.get_dice_num_list("red")))
            myapp.mn2bluerollresultlied.setText(str(self.get_dice_num_list("blue")))
            myapp.mn2greenrollresultlied.setText(str(self.get_dice_num_list("green")))
        elif index == 2:
            myapp.mn3redrollresultlied.setText(str(self.get_dice_num_list("red")))
            myapp.mn3bluerollresultlied.setText(str(self.get_dice_num_list("blue")))
            myapp.mn3greenrollresultlied.setText(str(self.get_dice_num_list("green")))

        #if self.temp_atk != 0:
        #    myapp.printt("이번 행동에 미리 {0}의 공격력이 부여되어 있음을 느꼈다.".format(self.temp_atk))
        #if self.temp_def != 0:
        #    myapp.printt("이번 행동에 미리 {0}의 방어력이 부여되어 있음을 느꼈다.".format(self.temp_def))
    def use_after_calc(self,hero,monsterlist,myapp):
        monstertrue = False
        index = None
        if self in hero.spell_use_list:
            myapp.printt("당신에게서 ", end='')
            index = -1
        for monster in monsterlist:
            if self in monster.spell_use_list:
                myapp.printt("몬스터로부터 ", end='')
                monstertrue = True
                index = monsterlist.index(monster)


        if monstertrue == True:
            ismonsatkzero = False
            ismonsatknone = False
            if self.temp_atk == []:
                ismonsatkzero = True
                ismonsatknone = True
            elif self.temp_atk[0] == 0:
                ismonsatkzero = True



            if ismonsatkzero == True and self.temp_def == 0:
                myapp.printt("아무런 방어력도, 공격력도 만들어지지 않았다.")
            elif self.only_one_green == True or self.main_resource_kinds == 'Nothing':
                if ismonsatknone == True:
                    myapp.printt('{0}의 공격력과 {1}의 방어력이 만들어졌다...'.format(0, self.temp_def))
                else:
                    myapp.printt('{0}의 공격력과 {1}의 방어력이 만들어졌다...'.format(self.temp_atk[0], self.temp_def))
            elif self.main_resource_kinds == 'red':
                myapp.printt('붉게 타오르는 양의 마력이 {0}의 공격력과 {1}의 방어력을 만들어냈다...'.format(self.temp_atk[0], self.temp_def))
            elif self.main_resource_kinds == 'blue':
                myapp.printt('푸르게 솟아오르는 음의 마력이 {0}의 공격력과 {1}의 방어력을 만들어냈다...'.format(self.temp_atk[0], self.temp_def))
            elif self.main_resource_kinds == 'green':
                myapp.printt('초록색의 뻗어나오는 조화의 마력이 {0}의 공격력과 {1}의 방어력을 만들어냈다...'.format(self.temp_atk[0], self.temp_def))

            if index == 0:
                myapp.mn1attackte.clear()
                for i in range(len(self.temp_atk)):
                    myapp.mn1attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                myapp.mn1defencelied.setText('0')
                myapp.mn1defencelied.setText(str(int(myapp.mn1defencelied.text()) + self.temp_def))
            elif index == 1:
                myapp.mn2attackte.clear()
                for i in range(len(self.temp_atk)):
                    myapp.mn2attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                myapp.mn2defencelied.setText('0')
                myapp.mn2defencelied.setText(str(int(myapp.mn2defencelied.text()) + self.temp_def))
            elif index == 2:
                myapp.mn3attackte.clear()
                for i in range(len(self.temp_atk)):
                    myapp.mn3attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                myapp.mn3defencelied.setText('0')
                myapp.mn3defencelied.setText(str(int(myapp.mn3defencelied.text()) + self.temp_def))
        else:
            if self.temp_atk == [] and self.temp_def == 0:
                myapp.printt("아무런 방어력도, 공격력도 만들어지지 않았다.")

                myapp.attackte.clear()
                for i in range(len(self.temp_atk)):
                    myapp.attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                myapp.defencelied.setText("0")
                myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))

                return

            if self.main_resource_kinds == 'red':
                myapp.printt('붉게 타오르는 양의 마력이 ',end='')
            elif self.main_resource_kinds == 'blue':
                myapp.printt('푸르게 솟아오르는 음의 마력이 ',end='')
            elif self.main_resource_kinds == 'green':
                myapp.printt('초록색의 뻗어나오는 조화의 마력이 ',end='')

            if self.temp_atk == [] and self.temp_def != 0:
                myapp.printt("{0}의 방어력을 만들어냈다.".format(self.temp_def))

                myapp.attackte.clear()
                for i in range(len(self.temp_atk)):
                    myapp.attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                myapp.defencelied.setText("0")
                myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))

                return
            elif self.temp_atk != [] and self.temp_def != 0:
                myapp.printt("{0}의 방어력을 만들어냈다. 또한,".format(self.temp_def))
                myapp.printt("적 {0} 에게 각각 {1}의 공격을 가하였다.".format(self.temp_direc, self.temp_atk))
            elif self.temp_atk != [] and self.temp_def == 0:
                myapp.printt("적 {0} 에게 각각 {1}의 공격을 가하였다.".format(self.temp_direc, self.temp_atk))

            myapp.attackte.clear()
            for i in range(len(self.temp_atk)):
                myapp.attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
            myapp.defencelied.setText("0")
            myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))

    def use(self,hero,monsterlist,myapp):  # 굴려진 다이스를 가지고 실제 주문력, 방어력을 계산\
        pass

    def direc_decide(self,namelist,myapp):
        pass
class Item:
    name = None
    showname = None

    temp_atk = 0
    temp_def = 0

    price = 0

    ismother = True

    def __init__(self,cls):  # ex) (라이트닝 슛, - , 2d+1) 즉 전부 문자열로 받아야함. # u
        self.name = cls.name
        self.showname = cls.showname

        self.temp_atk = cls.temp_atk
        self.temp_def = cls.temp_def

        self.price = cls.price

        self.ismother = True

    def buy(self,hero,myapp):
        if hero.money - self.price < 0:
            myapp.printt("돈이 부족합니다.")
        else:
            hero.money -= self.price
            hero.bag_list.append(self)
            hero.bag_name_list.append(self.name)

    def use(self,hero,monsterlist,myapp):
        pass


class Dice:
    def __init__(self,color):
        self.num = None ##값을 변경하기 전에 반드시 available 를 확인!
        self.available = False
        self.color = color #"red", "blue", "green"

    def activate(self):
        self.available = True

    def deactivate(self):
        self.num = None
        self.available = False


    def roll(self):
        if self.available == True:
            self.num = random.randrange(1,7)
        else:
            return


##test##