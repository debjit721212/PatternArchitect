from abc import ABC, abstractmethod


class FileSystemEntity(ABC):
    @abstractmethod
    def show(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass


class File(FileSystemEntity):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("  " * indent + f"📄 {self.name}")

    def delete(self):
        print(f"🗑️ Deleting file: {self.name}")
    
    
    

class Folder(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print("  " * indent + f"📁 {self.name}")
        for child in self.children:
            child.show(indent + 1)

    def delete(self):
        print(f"🗑️ Deleting folder: {self.name}")
        for child in self.children:
            child.delete()
            
root = Folder("Root")
docs = Folder("Documents")
img = Folder("Images")

file1 = File("resume.pdf")
file2 = File("profile.jpg")
file3 = File("notes.txt")

docs.add(file1)
img.add(file2)
docs.add(file3)

root.add(docs)
root.add(img)

root.show()



"""
root.show(indent=0)
│
├── print "📁 Root"
│
├── loop: child = docs
│   └── docs.show(indent=1)
│       ├── print "  📁 Documents"
│       ├── child = file1 → file1.show(indent=2)
│       │   └── print "    📄 resume.pdf"
│       ├── child = file3 → file3.show(indent=2)
│       │   └── print "    📄 notes.txt"
│
├── next child = img
│   └── img.show(indent=1)
│       ├── print "  📁 Images"
│       ├── child = file2 → file2.show(indent=2)
│       │   └── print "    📄 profile.jpg"

"""