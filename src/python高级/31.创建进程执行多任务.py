import time
from multiprocessing import Process


class EatProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self)->None:
        for i in range(10):
            print(f'{self.name} 正在吃饭 == {i}')
            time.sleep(0.1)

class WorkProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self)->None:
        for i in range(10):
            print(f'{self.name} 正在写作业 == {i}')
            time.sleep(0.1)


if __name__ == '__main__':
    EatProcess('process-1').start()
    WorkProcess('process-2').start()