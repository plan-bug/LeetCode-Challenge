class Foo(object):
    
    first_executed = False
    second_executed = False
    
    def __init__(self):
        pass

    def first(self, printFirst):
        printFirst()
        self.first_executed = True


    def second(self, printSecond):
        while not self.first_executed:
            continue
        printSecond()
        self.second_executed = True
            
            
    def third(self, printThird):
        while not self.second_executed:
            continue
        printThird()
