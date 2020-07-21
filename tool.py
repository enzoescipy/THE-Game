
import time
import copy
import random

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
class TTsig(QThread):
    inputsig = pyqtSignal(str)


def cut(int):
    if int >= 0:
        return int
    else:
        return 0

class UpgradedVar:
    def __init__(self, name, value):
        self.name = name #이름짓는 규칙. 1: 변수의 영어이름을 그대로 타이핑한다. 2: 클래스의 파라미터일 경우에 다른 파라미터의 값을 참조하여 쓸 수 있는데, 이때는 서로를 .으로 구분한다.ex)골렘.hp
        self.value = value

        self.old_value = None
        self.valuelog = []

        self.observer = []  # [[name,mother,[[temp1],[temp2],[temp3]]]] 즉슨, [[이름,모체,[[1순위],[2순위],[3순위]]]] 형식. "분류형 2차원 스택"
        self.always_observer =[]

    def initialize(self):
        self.valuelog = []
        self.observer = []
        self.always_observer = []

    def change(self, new_value):
        # 새로운 값 저장 및 이전 값 저장
        self.old_value = self.value
        self.valuelog.append(self.old_value)
        self.value = new_value

        # 우선순위가 "항상" 인 옵저버들을 전부 실행 및 예외처리 위해 우선순위가 항상인 옵저버가 1개라도 있는지 체크
        always_obs_true = False
        if len(self.always_observer) != 0:
            always_obs_true = True
        for i in range(len(self.always_observer)):
            if self.always_observer[i][2](self.old_value, new_value,self.valuelog) == True:
                self.always_observer[i][0](*self.always_observer[i][4])

        # 빈 스택 리스트 제거
        for i in range(len(self.observer)):
            if self.observer[i][1] == []:
                self.observer.pop(i)

        # 옵저버가 비게 되었다면 옵저버센터에서 제거. 단, 우선순위 항상인 옵저버가 있다면 패스.
        if self.observer == [] and always_obs_true == False:
            ObserverCenter.observing_center_pop(self.name)
            return

        # 모든 스택 내의 옵저버들을 1씩 실행
        for i in range(len(self.observer)):
            for j in range(len(self.observer[i][1][0])):
                if self.observer[i][1][0][j][2](self.old_value, new_value,self.valuelog) == True:
                    self.observer[i][1][0][j][0](*self.observer[i][1][0][j][4])
                    self.observer[i][1][0].pop(j)
            if self.observer[i][1][0] == []:
                self.observer[i][1].pop(0)

        # 실행되고 난 후, 모든 스택이 비어있다면 옵저버 초기화 후 옵저버 센터에서 제거. 단,  우선순위 항상인 옵저버가 있으면 옵저버센터 제거는 패스.
        empty = True
        for list in self.observer:
            if list[1] != []:
                empty = False
        if empty == True:
            self.observer = []
            if always_obs_true == False:
                ObserverCenter.observing_center_pop(self.name)
            return


    def observer_add(self, show_bool, show_func, priority, observer, obs_name, obs_brain, obs_mother, *obs_para): #priority 스택 우선순위, observer 실행할 함수 obsmother 함수의 모체 객체(ex: buff.use면 buff) obsbrain 조건식 함수 obspara 실행할 함수의 파라미터

        if type(priority) == type(1):
            temp = [observer, obs_name, obs_brain, obs_mother, obs_para, show_bool, show_func]
            obsfirsttag = []
            for i in range(len(self.observer)):
                obsfirsttag.append(self.observer[i][0])
            if obs_name in obsfirsttag:
                index = obsfirsttag.index(obs_name)

                if priority < len(self.observer[index][1]):
                    self.observer[index][1][priority].append(temp)

                elif priority >= len(self.observer[index][1]):
                    delta = priority - len(self.observer[index][1]) + 1
                    if delta < 0:
                        return "Error!"
                    for i in range(delta):
                        self.observer[index][1].append([])
                    self.observer[index][1][priority].append(temp)

            else:
                tempstack = []
                for i in range(priority):
                    tempstack.append([])
                tempstack.append([temp])
                tempnamestack = [obs_name, tempstack]
                self.observer.append(tempnamestack)

        elif priority == "ALL":
            temp = [observer, obs_name, obs_brain, obs_mother, obs_para, show_bool, show_func]
            self.always_observer.append(temp)





class ObserverCenter:
    observing_list = []

    @classmethod
    def observing_center_add(cls, var):
        for i in range(len(cls.observing_list)):
            if cls.observing_list[i].name == var.name:
                return "Error!"
        cls.observing_list.append(var)

    @classmethod
    def observing_center_pop(cls, varname):
        for i in range(len(cls.observing_list)):
            if cls.observing_list[i].name == varname:
                cls.observing_list.pop(i)
    @classmethod
    def observing_center_search(cls, varname):
        for i in range(len(cls.observing_list)):
            if cls.observing_list[i].name == varname:
                return cls.observing_list[i]
        return None




##test##