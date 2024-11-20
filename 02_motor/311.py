import pickle

class Motor():
    def __init__(self,status,speed,rotation):
        self.status=status
        self.speed=speed
        self.rotation=rotation
try:
    with open('motorcontroller/motornum1.pkl', 'rb') as file:
        num1 = pickle.load(file)
        print("已成功加载之前的电机状态。")
except (FileNotFoundError, EOFError):
    num1 = Motor("stopped", 0, "无")
    print("未找到之前的电机状态，已创建新的电机对象。")

while True:
        try:
            b=int(input("(请输入下一个指令：0:关闭电机，1:打开电机，2: 修改速度, 3: 显示速度, 4: 修改旋转方向, 5: 显示旋转方向, -1: 退出程序):"))
        except ValueError:
            print("输入无效，请输入一个整数。")
        if b==-1:
            print("已退出程序")
            break
        elif b==0:
            num1.status="stopped"
            num1.speed=0
            num1.rotation="无"
            with open('motorcontroller/motornum1.pkl', 'wb') as file:
                pickle.dump(num1, file)
            print("电机已关闭")
        elif b==1:
            num1.status="running"
            print("电机已开启") 
        elif b==2:
            if num1.status not in ["running"]:
                print("电机未开启")
            else:
                try:
                    num1.speed=float(input("请输入要修改速度的值，单位为rps:"))
                    with open('motorcontroller/motornum1.pkl', 'wb') as file:
                        pickle.dump(num1, file)
                except ValueError:
                    print("输入无效，请输入一个数字。")
        elif b==3:
            if num1.status not in ["running"]:
                print("电机未开启")
            else:
                print("电机的速度为:"+str(num1.speed)+" "+"rps")
        elif b==4:
            if num1.status not in ["running"]:
                print("电机未开启")
            else:
                num1.rotation=input("请输入要修改的旋转方向(顺时针/逆时针)")
                if num1.rotation not in ["顺时针", "逆时针"]:
                    print("输入无效，请输入'顺时针'或'逆时针'。")
                else:
                    with open('motorcontroller/motornum1.pkl', 'wb') as file:
                        pickle.dump(num1, file)
        elif b==5:
            if num1.status not in ["running"]:
                print("电机未开启")
            else:
                print("电机的旋转方向为: "+num1.rotation)
        else :
            print("指令无效，请重试")
