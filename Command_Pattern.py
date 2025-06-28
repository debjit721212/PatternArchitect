from abc import ABC,abstractmethod
import time

class Base(ABC):
    
    @abstractmethod
    def on(self):
        pass
    
    @abstractmethod
    def off(self):
        pass
    


class SwitchCommand(Base):
    def __init__(self,receiver):
        self.receiver = receiver
    
    def on(self):
        self.receiver.perform_on()
    
    def off(self):
        self.receiver.perform_off()

class Receiver:
    def __init__(self):
        self.history = []
        
    def perform_on(self):
        print("Turn on the switch ")
        self.history.append(True)
    
    def perform_off(self):
        print("Trun off the switch")
        self.history.pop()
        
class Invoker:
    def command(self,cmd):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.on()
        time.sleep(5)
        self.cmd.off()

if __name__ == "__main__":
    receiver = Receiver()
    cmd = SwitchCommand(receiver=receiver)
    invoker = Invoker()
    invoker.command(cmd=cmd)
    invoker.execute()