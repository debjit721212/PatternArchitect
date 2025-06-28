# class Singletone:
#     _inisialized = False
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __init__(self,name):
#         if not self._inisialized:
#             self.name = name
#             Singletone._inisialized = True

# c1 = Singletone("Humba")
# # c2 = Singletone("Hola")


class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):  # ✅ Accept extra args
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not self._initialized:
            self.name = name
            Singleton._initialized = True

# Test
a = Singleton("Humba")
b = Singleton("Another")

print(a.name)  # Humba
print(b.name)  # Humba ✅ Still the same instance


#### Singletone as a wrapper 

def singletone(cls):
    instance = {}
    def wraper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return wraper
    
@singletone
class Configuration:
    def __init__(self):
        print("Loading config ...... .")

c1 = Configuration()
c2 = Configuration()
print(c1 , c2)


            