class Vehicle:
    def __init__(self,is_engine_running):
        self.is_engine_running=is_engine_running
    def engine_status(self):
        if self.is_engine_running==True:
            print('engine is running')
        elif self.is_engine_running==False:
            print('engine is off')
        else:
            print('wrong value inserted')
class privatecar(Vehicle):
    def __init__(self,is_engine_running):
        self.is_engine_running= is_engine_running
        super().__init__(is_engine_running)#super passes the variable through parent class 

ford_focus= privatecar(True)
ford_focus.engine_status()