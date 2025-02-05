from abc import ABC, abstractmethod
class Demo(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
class Demo2(Demo):
    def disp2(self):
        print('Inside disp2')
    def disp1(self):
        print('Inside disp1')
d2 = Demo2()
d2.disp1()
d2.disp2()