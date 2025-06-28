""" This code is for adapter method python """


import datetime
from abc import ABC,abstractmethod
import threading

def singletone(cls):
    _instance = {}
    _lock = threading.Lock()
    def wraper(*args,**kwargs):
        with _lock:
            if cls not in _instance:
                _instance[cls] = cls(*args,**kwargs)
            return _instance[cls]
    return wraper

@singletone
class Logger:
    def __init__(self):
        self.message_dict = {}
    
    
    def log(self,message,level="info"):
        if level not in self.message_dict:
            self.message_dict[level] = []
        
        self.message_dict[level].append(f"timestamp: {datetime.datetime.now()}  message: {message}")
        return True
    def show_logs(self,level="info",is_filter_log=False):
        if is_filter_log:
            print(f"log type is ---> {level}")
            messages = self.filter_logs(level=level)
            for message in messages:
                print(f"The message is ----> {message}")
        else:
            for log_type,messages in self.message_dict.items():
                print(f"log type is ---> {log_type}")
                for message in messages:
                    print(f"The message is ----> {message}")
    
    def filter_logs(self,level="info"):
        return self.message_dict[level]
    def clear_logs(self,level):
        if level in self.message_dict:
            self.message_dict[level] = []
    
    def write_logs_to_file(self,filename):
       with open(filename, "w") as f:
            for log_type,messages in self.message_dict.items():
                for message in messages:
                    f.write(f"loglevel -> {log_type}  the message is ----> {message} \n")
            



class EmailSender:
    def send_email(self,message,logger):
        logger.log(message,level = "email")
        print(f"Hey ! Humba {message}")

class SMSSender:
    def send_SMS(self,message,logger):
        logger.log(message,level = "SMS")
        print(f"Hey ! Humba {message}")

class SlackNotifier:
    def send_slack_message(self,message,logger):
        logger.log(message,level = "slack")
        print(f"Hey ! Humba {message}")

class Messagereciver(ABC):
    @abstractmethod
    def notify(self,message):
        raise 
    
class NotificationAdapter(Messagereciver):
    def __init__(self,message_reciver):
        super().__init__()
        self.message_reciver =message_reciver
        self.logger = Logger()
    
    def notify(self, message):
        if hasattr(self.message_reciver,"send_email"):
            self.message_reciver.send_email(message,self.logger)
        elif hasattr(self.message_reciver,"send_SMS"):
            self.message_reciver.send_SMS(message,self.logger)
        elif hasattr(self.message_reciver,"send_slack_message"):
            self.message_reciver.send_slack_message(message,self.logger)
    def show_all_notification(self):
        self.logger.show_logs()
        

def load_and_send_messages(filename):
    services = {
        "email": EmailSender(),
        "sms": SMSSender(),
        "slack": SlackNotifier()
    }

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            method, message = line.split("::", 1)
            service = services.get(method.lower())
            if service:
                adapter = NotificationAdapter(service)
                adapter.notify(message)

    # View all notifications
    NotificationAdapter(services["email"]).show_all_notification()


if __name__ == "__main__":
    load_and_send_messages("/home/debjit/Pictures/Humba/notification_builder_message_input.txt")