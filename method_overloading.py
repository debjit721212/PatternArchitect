class Perent:
    def display(self):
        print("HEY I AM IN PERENT ----> ")

class Chile(Perent):
    def show(self):
        print("CAME INSIDE CHILE CLASS ")

class bothclass(Chile):
    def show(self):
        print("CAME IN BOTHCLASS -----> ")


a = bothclass()
print(a.show())
print(a.display())