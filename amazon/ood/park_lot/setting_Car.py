import time
from setting_Manage import ParkManage

class Car(ParkManage):
    """一个关于车的类"""
    def __init__(self,car_number,car_owner,contact_way,car_color,car_model):
        super(Car, self).__init__()
        self.car_number=car_number
        self.car_owner=car_owner
        self.contact_way=contact_way
        self.car_color=car_color
        self.car_model=car_model
        self.balance=200
        self.entrance_time = 0
        self.exit_time = 0

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def slot_card(self):
        """根据时间计费"""
        park_time=time.mktime(time.strptime(self.exit_time)) - time.mktime(
            time.strptime(self.entrance_time))
        h=park_time//3600
        m=(park_time-h*3600)//60
        s=park_time-h*3600-m*60
        P_time="%.0f时%.0f分%.0f秒"%(h,m,s)
        consumption = ((park_time) / 3600) * 5
        self.balance -= consumption
        print("车牌号为:%s\n停车时长:%s\n本次消费:%.2f元\n卡里余额:%.2f元\n" % (self.car_number,P_time, consumption, self.balance))

    def __str__(self):
        if self.car_model=='0':
            self.car_model="小汽车"
        elif self.car_model=='1':
            self.car_model="小卡"
        elif self.car_model=='2':
            self.car_model="中卡"
        elif self.car_model=='3':
            self.car_model="大卡"
        return "%s %s %s %s %s %s" %(self.car_number,self.car_owner,self.contact_way,
                                     self.car_color,self.car_model,self.entrance_time)


