
from parameter_class import *
##붉은 마법
class BloodSpear(Spell):
    def __init__(self):
        cls = BloodSpear
        super().__init__(cls)
    name = "피의 창"
    main_resource_kinds = "red"
    showname = "붉은 주사위 1개 요구, 대상 하나에게 공격력(d+8)로 공격, 초록 주사위 1개 추가 융합 가능, 추가 융합된 초록 주사위 1개당 체력 5 회복"
    crazyname = "솟아오른 피로 만든 창으로 적을 꿰뚫습니다. 피가 어디서 나왔는지는...누구에게도 비밀이랍니다! 초록 주사위를 사용하면 체력 소모를 상쇄합니다."
    red_dice_list = [Dice("red")]
    blue_dice_list = []
    green_dice_list = [Dice("green"),Dice("green")]
    blue_roll = False
    red_roll = True
    green_roll = False

    def direc_decide(self,namelist,myapp): #namelist는 전투에 참여중인 모든 캐릭터의 이름태그 목록
        namelistcopy = copy.copy(namelist)
        namelistcopy.pop(namelist.index("hero"))
        myapp.printt("선택 가능 대상 : {0}".format(namelistcopy))
        while (1):
            direc = myapp.inputt("공격할 대상의 이름을 선택하여 주세요.")
            if direc in namelistcopy:
                break
            myapp.printt("잘못된 대상입니다.")
            direc = None

        self.temp_direc.append(direc)

    def use(self,hero,monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")

        if r_ac != 1 or g_ac == 0:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                rd = self.get_dice_num_list("red")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(rd[0] + 5)
                super().use_after_calc(hero, monsterlist,myapp)

            elif g_ac == 2:
                rd = self.get_dice_num_list("red")
                hero.change_health(hero.health + 5,monsterlist,myapp)
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(rd[0] + 5)
                myapp.printt("또한, 깊게 뻗어나오는 초록색 마력은 5의 체력을 회복시켰다.")
class BloodShield(Spell):
    def __init__(self):
        cls = BloodShield
        super().__init__(cls)
    name = "피의 방패"
    main_resource_kinds = "red"
    showname = "붉은 주사위 1개 요구, 방어력(d+10)획득, 초록 주사위 1개 추가 융합 가능, 추가 융합된 초록 주사위 1개당 체력 5 회복"
    crazyname = "피로 만든 단순하지만 강력한 방어막을 두릅니다. 고작 핏덩어리인데, 왜이렇게 질길까요? 초록 주사위를 사용하면 체력 소모를 상쇄합니다."
    red_dice_list = [Dice("red")]
    blue_dice_list = []
    green_dice_list = [Dice("green"), Dice("green")]
    blue_roll = False
    red_roll = True
    green_roll = False

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")

        if r_ac != 1 or g_ac == 0:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                rd = self.get_dice_num_list("red")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def +=  rd[0] + 10
                super().use_after_calc(hero, monsterlist,myapp)
            elif g_ac == 2:
                rd = self.get_dice_num_list("red")
                hero.change_health(hero.health + 5,monsterlist,myapp)
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def +=  rd[0] + 10
                super().use_after_calc(hero, monsterlist,myapp)

                myapp.printt("또한, 깊게 뻗어나오는 초록색 마력은 5의 체력을 회복시켰다.")

class WeakenGas(Spell):
    def __init__(self):
        cls = WeakenGas
        super().__init__(cls)

    name = "약화 가스"  # 스킬 이름
    main_resource_kinds = "red"  # 메인 주사위 색
    showname = "붉은 주사위 1개 요구, 모든 상대방의 남은 행동 전부에 약화 3 부여(약화 : 최종 공격력/방어력에 2를 깎는다.), 초록 주사위 1개 추가 융합 가능, 추가 융합된 초록 주사위 1개당 약화 2 부여 "  # 스킬 상세설명
    crazyname = "자욱한 붉은색 가스를 적을 향해 살포하여, 적의 행동을 방해합니다. 어...? 바람이 내쪽으로 부네??"  # 약을 한사발 빤 스킬 설명
    red_dice_list = [Dice("red")]  # 붉은 주사위 최대 소모량
    blue_dice_list = []  # 푸른 주사위 최대 소모량
    green_dice_list = [Dice("green"), Dice("green")]  # 녹색 주사위 최대 소모량. 참고로, "최대" 소모량임. 서브 주사위로 사용시에도 항상 최대임을 감안!
    blue_roll = False  # 부 주사위로 사용될 때, 푸른 주사위의 눈금값이 필요한지 여부
    red_roll = False  # 마찬가지
    green_roll = False  # 마찬가지
    only_one_green = False  # 초록 주사위 던지기처럼, 초록주사위 단 한개만 사용하고 다른 대가가 없는 스킬인지 여부. 이런 스킬은 무미건조한 대사가 출력되게 설정되어 있음.

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):  # use 메소드 오버라이딩
        self.roll_all_color()
        r_ac = self.avail_count("red")  # 활성화된 붉은 주사위의 개수
        g_ac = self.avail_count("green")  # 활성화된 초록 주사위의 개수.
        b_ac = self.avail_count("blue")  # 활성화된 파랑 주사위의 개수. 여기서 '활성화된' 이란, 유저가 사용하겠다고 결정한 과 같은 의미. 특히 서브 주사위에서 중요함!
        if r_ac != 1 or g_ac == 0:  # 이런식으로 예외처리.
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                super().use_before_calc(hero, monsterlist,myapp)
                for j in range(len(monsterlist)):
                    for i in range(hero.spell_use_list.index(self) , len(monsterlist[j].buff_list)):
                        monsterlist[j].buff_list_add(i, Weaken(3))
                    myapp.printt("붉은 약화 가스가 적 {0} 을 향해 분출되어 남은 모든 행동에 3의 약화를 가했다!".format(monsterlist[j].name))
                super().use_after_calc(hero, monsterlist,myapp)
            elif g_ac == 2:
                super().use_before_calc(hero, monsterlist,myapp)
                for j in range(len(monsterlist)):
                    for i in range(hero.spell_use_list.index(self) , len(monsterlist[j].buff_list)):
                        monsterlist[j].buff_list_add(i, Weaken(5))
                    myapp.printt("붉은 약화 가스가 적 {0} 을 향해 분출되어 남은 모든 행동에 5의 약화를 가했다!".format(monsterlist[j].name))

                super().use_after_calc(hero, monsterlist,myapp)

            ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.

#약화
class Weaken(Spell):
    def __init__(self,weaken_amount):
        cls = Weaken
        super().__init__(cls)
        #추가 파라미터
        self.weaken_amount = weaken_amount

    name = "약화"
    main_resource_kinds = "Nothing"
    showname = "[약화 가스]의 효과로 발생한 자욱한 붉은색 가스가 공격력과 방어력을 감소시킵니다."
    crazyname = "피아를 가리지 않는다고 합니다..."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []

    def use(self, hero, monsterlist,myapp):
        for i in range(len(monsterlist)):
            if monsterlist[i].buff_list_in(self):
                mindex = i
                index = monsterlist[i].buff_list_find(self)
                monsterlist[i].spell_use_list[index].temp_def -= self.weaken_amount
                for j in range(len(monsterlist[i].spell_use_list[index].temp_atk)):
                    monsterlist[i].spell_use_list[index].temp_atk[j] -= self.weaken_amount
                myapp.printt("약화 로 인하여 적의 공격력과 방어력이 {0} 씩 감소되었다!".format(self.weaken_amount))
                if mindex == 0:
                    for i in range(len(self.temp_atk)):
                        myapp.mn1attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                    myapp.mn1defencelied.setText(str(int(myapp.mn1defencelied.text()) + self.temp_def))
                elif mindex == 1:
                    for i in range(len(self.temp_atk)):
                        myapp.mn2attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                    myapp.mn2defencelied.setText(str(int(myapp.mn2defencelied.text()) + self.temp_def))
                elif mindex == 2:
                    for i in range(len(self.temp_atk)):
                        myapp.mn3attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
                    myapp.mn3defencelied.setText(str(int(myapp.mn3defencelied.text()) + self.temp_def))
                break






class RedPoisonSplay(Spell):
    def __init__(self):
        cls = RedPoisonSplay
        super().__init__(cls)

    name = "독극물 살포"
    main_resource_kinds = "red"
    showname = "붉은 주사위 1개 요구, 지정한 적 하나에게 독 3을 다음 3턴간 부여 (독 n: 매 턴 시작 마다 n의 피해를 입힌다.) , 초록 주사위 추가 융합 1개 가능, 융합시 추가 독 2 부여"
    crazyname = "붉은 독극물 방울들이 적 주위를 가득 채웁니다. 만일을 위해 방독면을 꼭 착용하도록 합시다."
    red_dice_list = [Dice("red")]
    blue_dice_list = []
    green_dice_list = [Dice("green"),Dice("green")]
    blue_roll = False
    red_roll = False
    green_roll = False
    only_one_green = False

    def direc_decide(self, namelist,myapp):  # namelist는 전투에 참여중인 모든 캐릭터의 이름태그 목록
        namelistcopy = copy.copy(namelist)
        namelistcopy.pop(namelist.index("hero"))
        myapp.printt("선택 가능 대상 : {0}".format(namelistcopy))
        while (1):
            direc = myapp.inputt("공격할 대상의 이름을 선택하여 주세요.")
            if direc in namelistcopy:
                break
            myapp.printt("잘못된 대상입니다.")
            direc = None

        self.temp_direc.append(direc)

    def use(self,hero,monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")
        b_ac = self.avail_count("blue")
        if g_ac == 0 or r_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                super().use_before_calc(hero, monsterlist,myapp)
                for j in range(len(monsterlist)):
                    for i in range(3):
                        if monsterlist[j].name == self.temp_direc[0]:
                            monsterlist[j].turn_buff_list_add(i, Poison(3))
                    myapp.printt("붉은 독극물이 적을 향해 살포 되어 3 턴 동안 독 3을 받는다!")
                self.temp_direc = []
                super().use_after_calc(hero, monsterlist,myapp)
            elif g_ac == 2:
                super().use_before_calc(hero, monsterlist,myapp)
                for j in range(len(monsterlist)):
                    for i in range(3):
                        if monsterlist[j].name == self.temp_direc[0]:
                            monsterlist[j].turn_buff_list_add(i, Poison(5))
                    myapp.printt("붉은 독극물이 적을 향해 살포 되어 3 턴 동안 독 5을 받는다!")
                self.temp_direc = []
                super().use_after_calc(hero, monsterlist,myapp)
#독
class Poison(Spell):
    def __init__(self,poison_amount):
        cls = Poison
        super().__init__(cls)
        #추가 파라미터
        self.poison_amount = poison_amount  # 독(3) 에 그 3

    name = "독"
    main_resource_kinds = "Nothing"
    showname = "[독극물 살포]의 효과로 발생한 붉은 독극물 방울들이 턴마다 피해를 입힙니다."
    crazyname = "방독면이 없으면... 음..."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []

    def use(self, hero, monsterlist,myapp):
        for i in range(len(monsterlist)):
            if monsterlist[i].turn_buff_list_in(self):
                monsterlist[i].change_health(monsterlist[i].health - self.poison_amount,monsterlist,myapp)
                myapp.printt("독 으로 인하여 적의 체력이 {0} 감소 되었다!".format(self.poison_amount))


class CausingBleeding(Spell):
    def __init__(self):
        cls = CausingBleeding
        super().__init__(cls)

    name = "출혈 유발"
    main_resource_kinds = "red"
    showname = "붉은 주사위 3개 요구, 지정한 적 하나에게 공격력(3d)으로 공격 및 출혈 2를 부여 (출혈 n: 이번 전투 동안, 모든 턴의 시작 마다 n의 피해를 입힌다.) , 초록 주사위 추가 융합 1개 가능, 융합시 추가 출혈 3 부여"
    crazyname = "적에게 깊은 자상을 남깁니다. 엄청나게 쓰라릴 겁니다."
    red_dice_list = [Dice("red"),Dice("red"),Dice("red")]
    blue_dice_list = []
    green_dice_list = [Dice("green"),Dice("green")]
    blue_roll = False
    red_roll = True
    green_roll = False
    only_one_green = False

    def direc_decide(self, namelist,myapp):  # namelist는 전투에 참여중인 모든 캐릭터의 이름태그 목록
        namelistcopy = copy.copy(namelist)
        namelistcopy.pop(namelist.index("hero"))
        myapp.printt("선택 가능 대상 : {0}".format(namelistcopy))
        while (1):
            direc = myapp.inputt("공격할 대상의 이름을 선택하여 주세요.")
            if direc in namelistcopy:
                break
            myapp.printt("잘못된 대상입니다.")
            direc = None

        self.temp_direc.append(direc)

    def use(self,hero,monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")
        b_ac = self.avail_count("blue")
        if g_ac == 0 or r_ac != 3:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            rd = self.get_dice_num_list("red")
            if g_ac == 1:
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(rd[0] + rd[1] + rd[2])
                for i in range(len(monsterlist)):
                    if monsterlist[i].name == self.temp_direc[0]:
                        monsterlist[i].all_turn_buff_list.append(Bleeding(2))
                myapp.printt("적에게 2의 출혈을 일으켰다.")
                super().use_after_calc(hero, monsterlist,myapp)
            elif g_ac == 2:
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(rd[0] + rd[1] + rd[2])
                for i in range(len(monsterlist)):
                    if monsterlist[i].name == self.temp_direc[0]:
                        monsterlist[i].all_turn_buff_list.append(Bleeding(5))
                myapp.printt("적에게 5의 출혈을 일으켰다.")
                super().use_after_calc(hero, monsterlist,myapp)
#출혈
class Bleeding(Spell):
    def __init__(self,bleeding_amount):
        cls = Bleeding
        super().__init__(cls)
        #추가 파라미터
        self.bleeding_amount = bleeding_amount  # 독(3) 에 그 3

    name = "출혈"
    main_resource_kinds = "Nothing"
    showname = "[출혈 유발]의 효과로 발생한 쓰라린 상처가 턴마다 피해를 입힙니다."
    crazyname = "벌어진 상처에서 핏물이 뿜어져 나옵니다. 윽..."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []

    def use(self, hero, monsterlist,myapp):
        for i in range(len(monsterlist)):
            if self in monsterlist[i].all_turn_buff_list:
                monsterlist[i].change_health(monsterlist[i].health - self.bleeding_amount,monsterlist,myapp)
            myapp.printt("출혈로 인하여 적의 체력이 {0} 감소 되었다!".format(self.bleeding_amount))

##푸른 마법
class ArcaneArrow(Spell):
    def __init__(self):
        cls = ArcaneArrow
        super().__init__(cls)
    name = "비전 화살"
    main_resource_kinds = "blue"
    showname = "푸른 주사위 1개 요구, 공격력(d+1)으로 적 하나를 지정하여 공격, 초록 주사위 1개 추가 융합 가능, 추가 융합된 초록 주사위 1개당 공격력 (6) 증가"
    crazyname = "순수한 푸른 마나를 이용해 만든 화살을 쏩니다. 효율은 그리 좋아보이지 않지만, 펑펑 쓸 수 있는 푸른 마나를 이용합니다! 초록 주사위를 융합하면 고정 공격력이 크게 상승합니다."
    red_dice_list = []
    blue_dice_list = [Dice("blue")]
    green_dice_list = [Dice("green"), Dice("green")]
    blue_roll = True
    red_roll = False
    green_roll = False

    def direc_decide(self, namelist,myapp):  # namelist는 전투에 참여중인 모든 캐릭터의 이름태그 목록
        namelistcopy = copy.copy(namelist)
        namelistcopy.pop(namelist.index("hero"))
        myapp.printt("선택 가능 대상 : {0}".format(namelistcopy))
        while (1):
            direc = myapp.inputt("공격할 대상의 이름을 선택하여 주세요.")
            if direc in namelistcopy:
                break
            myapp.printt("잘못된 대상입니다.")
            direc = None

        self.temp_direc.append(direc)

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        b_ac = self.avail_count("blue")
        g_ac = self.avail_count("green")
        if b_ac != 1 or g_ac == 0:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                bd = self.get_dice_num_list("blue")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(bd[0] + 1)
                super().use_after_calc(hero, monsterlist,myapp)

            elif g_ac == 2:
                bd = self.get_dice_num_list("blue")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_atk.append(bd[0] + 7)
                super().use_after_calc(hero, monsterlist,myapp)

                myapp.printt("(당신은 이중 6의 공격력은 초록 마나에 의하여 보강되었음을 느낀다.)")
class ArcaneShield(Spell):
    def __init__(self):
        cls = ArcaneShield
        super().__init__(cls)
    name = "비전 방패"
    main_resource_kinds = "blue"
    showname = "푸른 주사위 1개 요구, 방어력(d+2)획득, 초록 주사위 1개 추가 융합 가능, 추가 융합된 초록 주사위 1개당 방어력 (d) 증가 및 다음 행동에 방어력 (3) 부여"
    crazyname = "순수한 푸른 마나를 이용해 만든 방패를 세웁니다. 초록 주사위를 융합하면 멋진 두 겹의 방패로 변신합니다."
    red_dice_list = []
    blue_dice_list = [Dice("blue")]
    green_dice_list = [Dice("green"), Dice("green")]
    blue_roll = True
    red_roll = False
    green_roll = True

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        b_ac = self.avail_count("blue")
        g_ac = self.avail_count("green")
        if b_ac != 1 or g_ac == 0:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                bd = self.get_dice_num_list("blue")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += bd[0] + 2
                super().use_after_calc(hero, monsterlist,myapp)

            elif g_ac == 2:
                bd = self.get_dice_num_list("blue")
                gd = self.get_dice_num_list("green")
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += bd[0] + gd[1] + 2
                super().use_after_calc(hero, monsterlist,myapp)
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, ArcaneShieldshred())
                myapp.printt("또한, 깊게 뻗어나가는 초록색 마력은 다음 행동의 방어력을 3 증가시켰다.")
#비전 방패의 조각(초록 주사위가 추가 융합된 비전 방패를 마지막 턴에 사용했을 시)
class ArcaneShieldshred(Spell):
    def __init__(self):
        cls = ArcaneShieldshred
        super().__init__(cls)
    name = "비전 방패의 조각"
    main_resource_kinds = "Nothing"
    showname = "[비전 방패]의 효과로 인해 3의 방어력이 제공됩니다."
    crazyname = "비전의 아들딸입니다. 근데 비전 죽었지 않..."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def use(self,hero,monsterlist,myapp):
        hero.defence += 3
        myapp.printt("비전 방패의 조각이 당신의 방어력을 3 증가시켰다!")
        myapp.defencelied.setText('0')
        myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))

class ArcaneAmplify(Spell):
    def __init__(self):
        cls = ArcaneAmplify
        super().__init__(cls)

    name = "비전 증폭" #스킬 이름
    main_resource_kinds = "blue" #메인 주사위 색
    showname = "푸른 주사위 3개 요구, 즉시 초록 주사위 2개를 회복하고 다음 행동의 스킬을 두번 추가로 시전, 초록 주사위 1개 추가 융합 가능, 초록 주사위 추가 융합 시 초록 주사위를 하나 더 회복하고 추가 시전횟수 +1. " # 스킬 상세설명
    crazyname = "다음 주문을 반복하여 시전합니다. 상대의 얼굴을 향해 힘껏 초록 주사위를 3번 던질 수 있습니다. 이게 아닌가?" #약을 한사발 빤 스킬 설명
    red_dice_list = [] #붉은 주사위 최대 소모량
    blue_dice_list = [Dice("blue"),Dice("blue"),Dice("blue")] #푸른 주사위 최대 소모량
    green_dice_list = [Dice("green"),Dice("green")] #녹색 주사위 최대 소모량. 참고로, "최대" 소모량임. 서브 주사위로 사용시에도 항상 최대임을 감안!
    blue_roll = False #부 주사위로 사용될 때, 푸른 주사위의 눈금값이 필요한지 여부
    red_roll = False #마찬가지
    green_roll = False #마찬가지
    only_one_green = False # 초록 주사위 던지기처럼, 초록주사위 단 한개만 사용하고 다른 대가가 없는 스킬인지 여부. 이런 스킬은 무미건조한 대사가 출력되게 설정되어 있음.
    def use(self,hero,monsterlist,myapp): #use 메소드 오버라이딩
        self.roll_all_color()
        r_ac = self.avail_count("red") #활성화된 붉은 주사위의 개수
        g_ac = self.avail_count("green") #활성화된 파랑 주사위의 개수.
        b_ac = self.avail_count("blue") #활성화된 초록 주사위의 개수. 여기서 '활성화된' 이란, 유저가 사용하겠다고 결정한 과 같은 의미. 특히 서브 주사위에서 중요함!
        if b_ac != 3 or g_ac == 0:#이런식으로 예외처리.
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                super().use_before_calc(hero, monsterlist,myapp)
                hero.act_point += 2
                myapp.printt("당신의 초록 주사위가 2개 추가되었다.")
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, Amplify())
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, Amplify())
                myapp.printt("당신의 다음 행동에 증폭 효과가 2개 추가되어 당신이 시전할 스킬을 먼저 복사하여 시전한다.")
                super().use_after_calc(hero, monsterlist,myapp)
                ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.
            elif g_ac == 2:
                super().use_before_calc(hero, monsterlist,myapp)
                hero.act_point += 3
                myapp.printt("당신의 초록 주사위가 3개 추가되었다.")
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, Amplify())
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, Amplify())
                hero.buff_list_add(hero.spell_use_list.index(self) + 1, Amplify())
                myapp.printt("당신의 다음 행동에 증폭 효과가 3개 추가되어 당신이 시전할 스킬을 먼저 복사하여 시전한다.")
                super().use_after_calc(hero, monsterlist,myapp)

#증폭
class Amplify(Spell):
    def __init__(self):
        cls = Amplify
        super().__init__(cls)
    name = "증폭"
    main_resource_kinds = "Nothing"
    showname = "[비전 증폭]의 효과로 현재 주문을 한번 더 시전합니다."
    crazyname = "뽕맛에 취해보세요."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def use(self,hero,monsterlist,myapp):
        myapp.printt("비전 증폭의 효과로 {0}이 시전된다.".format(hero.spell_use_list[hero.buff_list_find(self)].name))
        myapp.printt("[[비전 증폭의 효과 시작:")

        index = hero.buff_list_find(self)

        hero.spell_use_list[index].pay_price(hero, monsterlist,myapp)

        if hero.fault_bool == False:
            hero.spell_use_list[index].use(hero, monsterlist,myapp)

        if hero.fault_bool == False:
            hero.attack += hero.spell_use_list[index].temp_atk
            hero.direction += hero.spell_use_list[index].temp_direc
            hero.defence += hero.spell_use_list[index].temp_def

            for i in range(len(self.temp_atk)):
                myapp.attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
            myapp.defencelied.setText('0')
            myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))

        hero.spell_use_list[index].temp_atk = []
        hero.spell_use_list[index].temp_def = 0


        myapp.printt(":비전 증폭의 효과 종료]]")

class ManaBurst(Spell):
    def __init__(self):
        cls = ManaBurst
        super().__init__(cls)

    name = "마나 폭파"  # 스킬 이름
    main_resource_kinds = "blue"  # 메인 주사위 색
    showname = "푸른 주사위 3개 요구, 방어력(3d-12) 획득. 이 스킬을 사용한 이후 어느 때든 마나를 사용하면 사용한 즉시 행동불능에 빠진 후 사용한 마나만큼 " \
               "무작위 적의 체력을 직접 차감, 초록 주사위 1개 추가 융합 가능, 초록 주사위 융합 시 추가 방어력(12)제공"  # 스킬 상세설명
    crazyname = "제어 불가능한 마나의 흐름을 뻥! 하고 터트립니다. 무지무지하게 강력합니다!"  # 약을 한사발 빤 스킬 설명
    red_dice_list = []  # 붉은 주사위 최대 소모량
    blue_dice_list = [Dice("blue"),Dice("blue"),Dice("blue")]  # 푸른 주사위 최대 소모량
    green_dice_list = [Dice("green"),Dice("green")]  # 녹색 주사위 최대 소모량. 참고로, "최대" 소모량임. 서브 주사위로 사용시에도 항상 최대임을 감안!
    blue_roll = True  # 부 주사위로 사용될 때, 푸른 주사위의 눈금값이 필요한지 여부
    red_roll = False  # 마찬가지
    green_roll = False  # 마찬가지
    only_one_green = False  # 초록 주사위 던지기처럼, 초록주사위 단 한개만 사용하고 다른 대가가 없는 스킬인지 여부. 이런 스킬은 무미건조한 대사가 출력되게 설정되어 있음.

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):  # use 메소드 오버라이딩
        self.roll_all_color()  # 모든 색의 주사위를 굴려주는 메소드. 반드시 제일 먼저 시전한다.
        r_ac = self.avail_count("red")  # 활성화된 붉은 주사위의 개수
        g_ac = self.avail_count("green")  # 활성화된 파랑 주사위의 개수.
        b_ac = self.avail_count("blue")  # 활성화된 초록 주사위의 개수. 여기서 '활성화된' 이란, 유저가 사용하겠다고 결정한 과 같은 의미. 특히 서브 주사위에서 중요함!
        if b_ac != 3 or g_ac == 0:  # 이런식으로 예외처리. 자세한건 다른 예시 스킬들을 참고하자.
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                bd = self.get_dice_num_list("blue")  # 주사위 눈금을 얻는 코드.
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += cut(bd[0] + bd[1] + bd[2] - 9)
                B = Burst()
                hero.mana.observer_add(True,B.show,0,B.use, B.name, lambda old, new, log: (old > new), B, hero, monsterlist, myapp)
                ObserverCenter.observing_center_add(hero.mana)
                myapp.printt("다음 마나를 사용할 때, 스킬 효과 대신 마나 폭파로 인한 피해가 적용된다.")
                super().use_after_calc(hero, monsterlist,myapp)
                ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.
            if g_ac == 2:
                bd = self.get_dice_num_list("blue")  # 주사위 눈금을 얻는 코드.
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += cut(bd[0] + bd[1] + bd[2])
                B = Burst()
                hero.mana.observer_add(True,B.show,0,B.use, B.name, lambda old, new, log: (old > new), B, hero, monsterlist, myapp)
                ObserverCenter.observing_center_add(hero.mana)
                myapp.printt("다음 마나를 사용할 때, 스킬 효과 대신 마나 폭파로 인한 피해가 적용된다.")
                super().use_after_calc(hero, monsterlist,myapp)
                ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.

#폭파
class Burst(Spell):
    def __init__(self):
        cls = Burst
        super().__init__(cls)
    name = "폭파"
    main_resource_kinds = "Nothing"
    showname = "[마나 폭파]의 효과로 차감된 마나만큼 직접 공격합니다."
    crazyname = "뽕맛에 취해보세요2."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def use(self,hero,monsterlist,myapp):
        myapp.specialbuffte.append("마나 폭파 효과 발동됨")
        myapp.printt("마나 폭파의 효과가 발생하였다!")
        hero.fault_bool = True
        myapp.faultbtn.setEnabled(False)
        myapp.printt("용사는 행동불능에 빠졌다!")
        delta = hero.mana.old_value - hero.mana.value
        monster = random.choice(monsterlist)
        monster.change_health(monster.health - delta,monsterlist,myapp)
        myapp.printt("거친 마나가 적 {0}의 방어력을 뚫고 몬스터의 체력을 {1} 없앴다!".format(monster.name,delta))
    def show(self, observer,myapp): #observer에 자신이 속해있는 옵저버 리스트를 넣는다. always형태라도 그대로.
        myapp.printt("폭파 : 다음 마나를 사용할 때, 차감된 마나 만큼 직접 공격한다.")
        myapp.specialbuffte.append("폭파 : 다음 마나를 사용할 때, 차감된 마나 만큼 직접 공격한다.")

class Overflow(Spell): #기본 템플릿 만들기 위함. 절대 깨기 귀찮아서 만든게 아님
    def __init__(self):
        cls = Overflow
        super().__init__(cls)

    name = "오버플로우" #스킬 이름
    main_resource_kinds = "blue" #메인 주사위 색
    showname = "푸른 주사위 4개 요구, 방어력 (4d-10)획득, 이 스킬을 사용한 후 10 이상의 마나를 3회 사용하면 그 즉시 아무런 대가 없이 무작위 적에게 (6d) 의 공격력으로 공격," \
               "초록 주사위 1개 추가 융합 가능, 추가 융합시 공격력을 부여하는 대신 적의 방어를 무시하고 직접 체력을 (6d) 만큼 차감" # 스킬 상세설명
    crazyname = "마나가 거꾸로 솟는 기분입니다." #약을 한사발 빤 스킬 설명
    red_dice_list = [] #붉은 주사위 최대 소모량
    blue_dice_list = [Dice("blue"),Dice("blue"),Dice("blue"),Dice("blue")] #푸른 주사위 최대 소모량
    green_dice_list = [Dice("green"),Dice("green")] #녹색 주사위 최대 소모량. 참고로, "최대" 소모량임. 서브 주사위로 사용시에도 항상 최대임을 감안!
    blue_roll = True #부 주사위로 사용될 때, 푸른 주사위의 눈금값이 필요한지 여부
    red_roll = False #마찬가지
    green_roll = False #마찬가지
    only_one_green = False # 초록 주사위 던지기처럼, 초록주사위 단 한개만 사용하고 다른 대가가 없는 스킬인지 여부. 이런 스킬은 무미건조한 대사가 출력되게 설정되어 있음.

    def direc_decide(self, namelist,myapp):
        return

    def use(self,hero,monsterlist,myapp): #use 메소드 오버라이딩
        self.roll_all_color() # 모든 색의 주사위를 굴려주는 메소드. 반드시 제일 먼저 시전한다.
        r_ac = self.avail_count("red") #활성화된 붉은 주사위의 개수
        g_ac = self.avail_count("green") #활성화된 파랑 주사위의 개수.
        b_ac = self.avail_count("blue") #활성화된 초록 주사위의 개수. 여기서 '활성화된' 이란, 유저가 사용하겠다고 결정한 과 같은 의미. 특히 서브 주사위에서 중요함!
        if b_ac != 4 or g_ac == 0:  # 이런식으로 예외처리. 자세한건 다른 예시 스킬들을 참고하자.
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if g_ac == 1:
                bd = self.get_dice_num_list("blue")  # 주사위 눈금을 얻는 코드.
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += cut(bd[0] + bd[1] + bd[2] + bd[3] - 10)
                myapp.defencelied.setText('0')
                myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))
                Oa = Overflowingatk()
                #참고. 블랭크와 리얼의 조건식 함수는 반드시 서로 같아야만 한다. 이유는 생각해보시라.
                for i in range(2):
                    hero.mana.observer_add(False, None, i, lambda : None, Oa.name,
                                           lambda old, new, log: (old - new >= 10),Oa)
                hero.mana.observer_add(True, Oa.show, 2, Oa.use, Oa.name, lambda old, new, log: (old - new >= 10),
                                       Oa, hero, monsterlist, myapp)
                ObserverCenter.observing_center_add(hero.mana)
                myapp.printt("10 이상의 마나를 3회 사용한 직후, (6d)의 공격력이 가산된다.")
                super().use_after_calc(hero, monsterlist,myapp)
                ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.
            if g_ac == 2:
                bd = self.get_dice_num_list("blue")  # 주사위 눈금을 얻는 코드.
                super().use_before_calc(hero, monsterlist,myapp)
                self.temp_def += cut(bd[0] + bd[1] + bd[2] + bd[3] - 10)
                myapp.defencelied.setText('0')
                myapp.defencelied.setText(str(int(myapp.defencelied.text()) + self.temp_def))
                Oh = Overflowinghealth()
                for i in range(2):
                    hero.mana.observer_add(False, None, i, lambda : None, Oh.name,
                                           lambda old, new, log: (old - new >= 10),Oh)
                hero.mana.observer_add(True, Oh.show, 2, Oh.use, Oh.name, lambda old, new, log: (old - new >= 10),
                                       Oh, hero, monsterlist, myapp)
                ObserverCenter.observing_center_add(hero.mana)
                myapp.printt("10 이상의 마나를 3회 사용한 직후, 적의 체력을(6d)만큼 직접 차감시킨다.")
                super().use_after_calc(hero, monsterlist,myapp)
                ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.
class Overflowingatk(Spell):
    def __init__(self):
        cls = Overflowingatk
        super().__init__(cls)
    name = "오버플로잉atk"
    main_resource_kinds = "Nothing"
    showname = "[오버플로우]의 효과로 (6d)의 공격력을 얻습니다."
    crazyname = "마꺼솟."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def use(self,hero,monsterlist,myapp):
        myapp.specialbuffte.append("오버플로우 효과 발동됨")
        myapp.printt("오버플로우의 효과가 발생하였다!")
        atkplus = [random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)]
        hero.attack.append(sum(atkplus))
        monsternamelist = []
        for monster in monsterlist:
            monsternamelist.append(monster.name)
        monstername = random.choice(monsternamelist)
        hero.direction.append(monstername)
        myapp.printt("{0}들이 나와, {1}의 공격력으로 {2}를 향해 공격한다.".format(atkplus,sum(atkplus),monstername))
        for i in range(len(self.temp_atk)):
            myapp.attackte.append(str(self.temp_direc[i]) + " / " + str(self.temp_atk[i]))
    def show(self, observer,myapp): #observer에 자신이 속해있는 옵저버 리스트를 넣는다. always형태라도 그대로.
        obsnamelist = []
        stackindex = 0
        index = 0
        #자신이 스택의 어느 우선순위에 있는지 찾는다.
        for stack in observer:
            obsnamelist.append(stack[0])
        stackindex = obsnamelist.index(self.name)

        for i in range(len(observer[stackindex][1])):
            for j in range(len(observer[stackindex][1][i])):
                if observer[stackindex][1][i][j][3] == self:
                    index = i
        #본문
        myapp.printt("오버플로우 : 발동되면 (6d)의 공격력이 즉시 가산된다.")
        myapp.printt("(현재 효과가 발동되기 까지 {0}회의 10 이상 마나소모가 필요합니다.)".format(index + 1))
        myapp.specialbuffte.append("오버플로우 : 발동되면 (6d)의 공격력이 즉시 가산된다.")
        myapp.specialbuffte.append("(현재 효과가 발동되기 까지 {0}회의 10 이상 마나소모가 필요합니다.)".format(index + 1))

class Overflowinghealth(Spell):
    def __init__(self):
        cls = Overflowinghealth
        super().__init__(cls)
    name = "오버플로잉health"
    main_resource_kinds = "Nothing"
    showname = "[오버플로우]의 효과로 (6d)의 상대 체력을 차감합니다."
    crazyname = "마꺼솟."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    def use(self,hero,monsterlist,myapp):
        myapp.specialbuffte.append("오버플로우(초록주사위 융합됨) 효과 발동됨")
        myapp.printt("오버플로우의 효과가 발생하였다!")
        healthminus = [random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)]
        monster = random.choice(monsterlist)
        monster.change_health(monster.health - sum(healthminus),monsterlist,myapp)
        myapp.printt("{0}이 나와, {1}의 몬스터 체력이 즉시 감소되었다.".format(healthminus,sum(healthminus)))
    def show(self, observer,myapp): #observer에 자신이 속해있는 옵저버 리스트를 넣는다. always형태라도 그대로.
        obsnamelist = []
        stackindex = 0
        index = 0
        # 자신이 스택의 어느 우선순위에 있는지 찾는다.
        for stack in observer:
            obsnamelist.append(stack[0])
        stackindex = obsnamelist.index(self.name)

        for i in range(len(observer[stackindex][1])):
            for j in range(len(observer[stackindex][1][i])):
                if observer[stackindex][1][i][j][3] == self:
                    index = i
        # 본문
        myapp.printt("오버플로우 : 발동되면 (6d)만큼 방어력을 뚫고 적의 체력을 즉시 차감한다.")
        myapp.printt("(현재 효과가 발동되기 까지 {0}회의 10 이상 마나소모가 필요합니다.)".format(index + 1))
        myapp.specialbuffte.append("오버플로우 : 발동되면 (6d)만큼 방어력을 뚫고 적의 체력을 즉시 차감한다.")
        myapp.specialbuffte.append("(현재 효과가 발동되기 까지 {0}회의 10 이상 마나소모가 필요합니다.)".format(index + 1))

##초록 마법
class ThrowGreenDice(Spell):
    def __init__(self):
        cls = ThrowGreenDice
        super().__init__(cls)
    name = "초록 주사위를 던진다!"
    main_resource_kinds = "green"
    showname = "초록 주사위 1개 요구, 무작위 적에게 공격력(1)로 공격"
    crazyname = "단순하지만 강력한 대화 수단입니다."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = [Dice("green")]
    one_green = True

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        g_ac = self.avail_count("green")
        if g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_atk.append(1)
            monsternamelist = []
            for monster in monsterlist:
                monsternamelist.append(monster.name)
            monstername = random.choice(monsternamelist)
            self.temp_direc.append(monstername)
            super().use_after_calc(hero, monsterlist,myapp)

class ManaCirculation(Spell):
    def __init__(self):
        cls = ManaCirculation
        super().__init__(cls)
    name = "마나 순환"
    main_resource_kinds = "green"
    showname = "초록 주사위 2개 요구, 자체 효과 없음, 빨강/파랑 주사위 중 1종류를 3개 추가 융합 가능, 추가 융합된 (1:붉은 / 2:푸른) 주사위를 굴려 얻은 눈금의 합만큼 (1:마나 / 2:체력) 회복"
    crazyname = "빨강, 파랑, 두 마나를 바꿀 수 있는 마법입니다. 아니 잠깐만, 이것까지 랜덤이면 어떡하냐고!"
    red_dice_list = [Dice("red"),Dice("red"),Dice("red")]
    blue_dice_list = [Dice("blue"),Dice("blue"),Dice("blue")]
    green_dice_list = [Dice("green"), Dice("green")]
    blue_roll = True
    red_roll = True
    green_roll = False

    def direc_decide(self, namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")
        b_ac = self.avail_count("blue")
        if g_ac != 2 or ((r_ac == 0) and (b_ac == 0)) == True or ((r_ac != 0) and (b_ac != 0)) == True:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if (r_ac == 0) and (b_ac != 0):
                bd = self.get_dice_num_list("blue")
                hero.change_health(hero.health + sum(bd),monsterlist,myapp)
                self.use_before_calc(hero, monsterlist,myapp)
                self.use_after_calc(hero, monsterlist,myapp)
                myapp.printt("그리고, 당신은 푸른 마나 주사위를 희생하여 {0}의 체력을 얻었다.".format(sum(bd)))
            elif (r_ac != 0) and (b_ac == 0):
                rd = self.get_dice_num_list("red")
                hero.change_mana(hero.mana.value + sum(rd),monsterlist,myapp)
                self.use_before_calc(hero, monsterlist,myapp)
                self.use_after_calc(hero, monsterlist,myapp)
                myapp.printt("그리고, 당신은  붉은 마나 주사위를 희생하여 {0}의 마나를 얻었다.".format(sum(rd)))
class LowClassEarthSpiritsEmploy(Spell):
    def __init__(self):
        cls = LowClassEarthSpiritsEmploy
        super().__init__(cls)
    name = "하급 대지의 정령 사역"
    main_resource_kinds = "green"
    showname = "초록 주사위 2개 요구, 자체 효과 없음, 빨강/파랑 주사위 중 1종류를 1개 추가 융합 가능, 추가 융합된 (1:붉은 / 2:푸른) 주사위를 굴려 얻은 눈금만큼 (1:공격력 / 2:방어력) 을 가진 하급 대지의 정령이" \
               "4회 대신 행동해줌. 이때 공격 대상은 무작위로 선택됨"
    crazyname = "초록 주사위를 대가로 당신이 행동하지 못할 때 대신 방어/공격을 4회 수행하는 대지의 정령을 부릅니다. 대지의 정령이 사용할 무기나 방패를 들려주지 못한다면, 그저 멀뚱멀뚱 서있을 뿐입니다."
    red_dice_list = [Dice("red")]
    blue_dice_list = [Dice("blue")]
    green_dice_list = [Dice("green"), Dice("green")]
    blue_roll = True
    red_roll = True
    green_roll = False

    def direc_decide(self,namelist,myapp):
        return

    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        r_ac = self.avail_count("red")
        g_ac = self.avail_count("green")
        b_ac = self.avail_count("blue")
        if g_ac != 2 or ((r_ac == 0) and (b_ac == 0)) == True or ((r_ac != 0) and (b_ac != 0)) == True:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            if (r_ac == 0) and (b_ac != 0):
                bd = self.get_dice_num_list("blue")
                for i in range(4):
                    spirit = LowClassEarthSpirit()
                    spirit_def = sum(bd)
                    spirit.temp_def = spirit_def
                    hero.spell_use_list.append(spirit)
                self.use_before_calc(hero, monsterlist,myapp)
                self.use_after_calc(hero, monsterlist,myapp)
                myapp.printt("그리고, 당신은 녹색 마나를 이용하여 4마리의 하급 대지의 정령을 소환하였다!")

            elif (r_ac != 0) and (b_ac == 0):
                rd = self.get_dice_num_list("red")
                for i in range(4):
                    spirit = LowClassEarthSpirit()
                    spirit_atk = sum(rd)
                    spirit.temp_atk.append(spirit_atk)

                    monsternamelist = []
                    for monster in monsterlist:
                        monsternamelist.append(monster.name)
                    monstername = random.choice(monsternamelist)
                    spirit.temp_direc.append(monstername)

                    hero.spell_use_list.append(spirit)

                self.use_before_calc(hero, monsterlist,myapp)
                self.use_after_calc(hero, monsterlist,myapp)
                myapp.printt("그리고, 당신은 녹색 마나를 이용하여 4마리의 하급 대지의 정령을 소환하였다!")
#하급 대지의 정령
class LowClassEarthSpirit(Spell):
    def __init__(self):
        cls = LowClassEarthSpirit
        super().__init__(cls)
    name = "하급 대지의 정령"
    main_resource_kinds = "Nothing"
    showname = "하급 대지의 정령 사역으로 소환된 대지의 정령."
    crazyname = "인간계로 오면서 가지고 있던 지갑을 잃어버렸답니다."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = []
    blue_roll = True
    red_roll = True
    green_roll = False

class OwnerKick(Spell): #기본 템플릿 만들기 위함. 절대 깨기 귀찮아서 만든게 아님
    def __init__(self):
        cls = OwnerKick
        super().__init__(cls)

    name = "영자의 꿀밤" #스킬 이름
    main_resource_kinds = "green" #메인 주사위 색
    showname = "방어력 1000000 * (3d), 또한 모든 적에게 같은 양의 공격력으로 공격, 초록 주사위 3개 소모" # 스킬 상세설명
    crazyname = "넌 죽었다 *발" #약을 한사발 빤 스킬 설명
    red_dice_list = [] #붉은 주사위 최대 소모량
    blue_dice_list = [] #푸른 주사위 최대 소모량
    green_dice_list = [Dice("green"),Dice("green"),Dice("green")] #녹색 주사위 최대 소모량. 참고로, "최대" 소모량임. 서브 주사위로 사용시에도 항상 최대임을 감안!
    blue_roll = False #부 주사위로 사용될 때, 푸른 주사위의 눈금값이 필요한지 여부
    red_roll = False #마찬가지
    green_roll = True #마찬가지
    only_one_green = False # 초록 주사위 던지기처럼, 초록주사위 단 한개만 사용하고 다른 대가가 없는 스킬인지 여부. 이런 스킬은 무미건조한 대사가 출력되게 설정되어 있음.

    def direc_decide(self,namelist,myapp):
        return

    def use(self,hero,monsterlist,myapp): #use 메소드 오버라이딩
        self.roll_all_color() # 모든 색의 주사위를 굴려주는 메소드. 반드시 제일 먼저 시전한다.
        r_ac = self.avail_count("red") #활성화된 붉은 주사위의 개수
        g_ac = self.avail_count("green") #활성화된 파랑 주사위의 개수.
        b_ac = self.avail_count("blue") #활성화된 초록 주사위의 개수. 여기서 '활성화된' 이란, 유저가 사용하겠다고 결정한 과 같은 의미. 특히 서브 주사위에서 중요함!
        if g_ac != 3: #이런식으로 예외처리. 자세한건 다른 예시 스킬들을 참고하자.
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            gd = self.get_dice_num_list("green") #주사위 눈금을 얻는 코드.
            super().use_before_calc(hero, monsterlist,myapp)
            for i in range(len(monsterlist)):
                self.temp_atk.append(1000000 * (gd[0] + gd[1] + gd[2]))# 최종적으로 올릴 공격력, 방어력을 temp.atk와 temp.def 에 쓴 후 그 앞뒤에 before, after use 메소드를 집어넣으면 기본 끗!
                self.temp_direc.append(monsterlist[i].name)
            self.temp_def += 1000000 * (gd[0] + gd[1] + gd[2])
            super().use_after_calc(hero, monsterlist,myapp)
            ##추가. 만일 초록 주사위를 부 주사위로 사용할때 그 눈금값이 필요하다면, 반드시 첫번째 ([0]) 은 무시하고 쓸 것.
################################################################

#slime 마법
class SlimeJump(Spell):
    def __init__(self):
        cls = SlimeJump
        super().__init__(cls)
    name = "물컹거리기"
    main_resource_kinds = "green"
    showname = "자원 소모 없음, 공격력(3) 획득"
    crazyname = "맞아도 아플 것 같지가 않습니다."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = [Dice("green")]
    only_one_green = True
    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        g_ac = self.avail_count("green")
        if g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_atk.append(3)
            self.temp_direc.append("hero")
            super().use_after_calc(hero, monsterlist,myapp)

class SlimeGuard(Spell):
    def __init__(self):
        cls = SlimeGuard
        super().__init__(cls)
    name = "막기"
    main_resource_kinds = "green"
    showname = "자원 소모 없음, 방어력(3) 획득"
    crazyname = "실험 방법: 나이프를 슬라임을 향해 던짐. 실험 결과: 그대로 통과하여 뒷쪽의 사과나무에 박힘."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = [Dice("green")]
    only_one_green = True
    def use(self,hero,monsterlist,myapp):
        self.roll_all_color()
        g_ac = self.avail_count("green")
        if g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_def += 3
            super().use_after_calc(hero, monsterlist,myapp)

class SlimePowerJump(Spell):
    def __init__(self):
        cls = SlimePowerJump
        super().__init__(cls)
    name = "집어삼키기"
    main_resource_kinds = "blue"
    showname = "푸른 주사위 3개 요구, 공격력(3d-3) 획득"
    crazyname = "포근한 엄마의 품으로 되돌아간 느낌입니다."
    red_dice_list = []
    blue_dice_list = [Dice("blue"),Dice("blue"),Dice("blue")]
    green_dice_list = [Dice("green")]
    blue_roll = True
    red_roll = False
    green_roll = False
    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        b_ac = self.avail_count("blue")
        g_ac = self.avail_count("green")
        if b_ac != 3 or g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            bd = self.get_dice_num_list("blue")
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_atk.append(bd[0] + bd[1] + bd[2] - 3)
            self.temp_direc.append("hero")
            super().use_after_calc(hero, monsterlist,myapp)


#stone_golem 마법
class StoneGolemBoom(Spell):
    def __init__(self):
        cls = SlimeJump
        super().__init__(cls)
    name = "내려찍기"
    main_resource_kinds = "green"
    showname = "자원 소모 없음, 공격력(7) 획득"
    crazyname = "맞으면 많이 아플 것 같습니다."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = [Dice("green")]
    only_one_green = True
    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        g_ac = self.avail_count("green")
        if g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_atk.append(7)
            self.temp_direc.append("hero")
            super().use_after_calc(hero, monsterlist,myapp)

class StoneGolemWall(Spell):
    def __init__(self):
        cls = StoneGolemWall
        super().__init__(cls)
    name = "돌벽 세우기"
    main_resource_kinds = "green"
    showname = "자원 소모 없음, 방어력(8) 획득"
    crazyname = "무진장 튼튼하진 않지만, 맨주먹으로 세게 때리면 아픕니다."
    red_dice_list = []
    blue_dice_list = []
    green_dice_list = [Dice("green")]
    only_one_green = True
    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        g_ac = self.avail_count("green")
        if g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_def += 8
            super().use_after_calc(hero, monsterlist, myapp)

class StoneGolemPowerBoom(Spell):
    def __init__(self):
        cls = StoneGolemPowerBoom
        super().__init__(cls)
    name = "지진파 발산"
    main_resource_kinds = "blue"
    showname = "푸른 주사위 6개 요구, 공격력(6d) 획득"
    crazyname = "골렘들이 대체 어디서 지진파를 가져오는지는 풀리지 않는 마법학계의 의문으로 남아있습니다."
    red_dice_list = []
    blue_dice_list = [Dice("blue"), Dice("blue"), Dice("blue"), Dice("blue"), Dice("blue"), Dice("blue")]
    green_dice_list = [Dice("green")]
    blue_roll = True
    red_roll = False
    green_roll = False
    def use(self, hero, monsterlist,myapp):
        self.roll_all_color()
        b_ac = self.avail_count("blue")
        g_ac = self.avail_count("green")
        if b_ac != 6 or g_ac != 1:
            raise Exception("주사위 활성화 오류. 관리자 호출 요망")
        else:
            bd = self.get_dice_num_list("blue")
            super().use_before_calc(hero, monsterlist,myapp)
            self.temp_atk.append(bd[0] + bd[1] + bd[2] + bd[3] + bd[4] + bd[5])
            self.temp_direc.append("hero")
            super().use_after_calc(hero, monsterlist,myapp)

##test##