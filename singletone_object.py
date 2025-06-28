import datetime

def singletone(cls):
    _instance = {}
    def wraper(*args,**kwargs):
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
            



logger = Logger()

# Logging different types
logger.log("Starting application...", level="INFO")
logger.log("User not found!", level="ERROR")
logger.log("Debugging step 1", level="DEBUG")
logger.log("Disk space running low", level="WARNING")

# Show all logs
print("\n🔍 All Logs")
logger.show_logs()

# Show only ERROR logs
print("\n❗ Filtered ERROR Logs")
logger.show_logs(level="ERROR", is_filter_log=True)

# Clear DEBUG logs
print("\n🧹 Clearing DEBUG Logs...")
logger.clear_logs("DEBUG")

# Show again to confirm
print("\n🔁 After Clearing DEBUG Logs")
logger.show_logs()

# Write logs to a file
print("\n💾 Writing Logs to File 'logs.txt'")
logger.write_logs_to_file("logs.txt")
