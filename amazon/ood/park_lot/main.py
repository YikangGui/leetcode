import re
from setting_Car import Car
from setting_Manage import ParkManage


def check_car_number(car_number):    #判断车牌号是否合法
    pattern = re.compile(u'[\u4e00-\u9fa5]?')
    pattern1 = re.compile(u'[A-Z]+')
    pattern2 = re.compile(u'[0-9]+')

    match = pattern.search(car_number)
    match1 = pattern1.search(car_number)
    match2 = pattern2.search(car_number)
    if match and match1 and match2:
        return True
    else:
        return False

def check_contact_way(contact_way):   #判断手机号是否合法
    pattern = re.compile(u'1[3|4|5|6|7|8|9]\d{9}$')

    match = pattern.search(contact_way)
    if match:
        return True
    else:
        return False


def main():
    parkmanage=ParkManage()
    while True:
        parkmanage.info()
        choice=input("请输入你要的功能:")
        if choice=='1':
            check_error_list=[]
            car_number=input("请输入车牌号:")
            if check_car_number(car_number):
                car_owner=input("请输入车主姓名:")
                contact_way=input("请输入车主联系方式:")
                if check_contact_way(contact_way):
                    car_color=input("请输入车颜色:")
                    car_model=input("请输入车型(小汽车:0,小卡：1，中卡：2，大卡：3):")
                    check_error_list=[car_number,car_owner,contact_way,car_color,car_model]
                    for info in check_error_list:    #判断输入信息的完整性
                        if info=='':
                            print("输入信息不全")
                            break
                    else:
                        car = Car(car_number, car_owner, contact_way, car_color, car_model)
                        parkmanage.add_car(car)
                else:
                    print("手机号无效")
            else:
                print("车牌号不合法")

        elif choice=='2':
            parkmanage.searchCar()
        elif choice =='3':
            parkmanage.display()
        elif choice=='4':
            parkmanage.change_Carinfo()
        elif choice=='5':
            car_number = input("输入您要删除的车辆的车牌号：")
            for car in parkmanage.car_list:
                if car.car_number == car_number:
                    parkmanage.delete_car(car)
                    break
            else:
                print("未找到车牌号为%s的车辆" % (car_number))

        elif choice=='6':
            parkmanage.statistics()
        elif choice=='7':
            print("欢迎下次使用！！！")
            exit()
        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()

