namelist = ['a', 'b']
while (1):
    direc = input("공격할 대상의 이름을 선택하여 주세요.")
    if direc in namelist:
        break
    print("잘못된 공격 대상입니다.")
    direc = None
print(direc)