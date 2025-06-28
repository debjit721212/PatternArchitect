class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # guest, user, admin
        self.name_to_role_dict = {}
        self.name_to_role_dict[name]= self.role
    
    def add(self,name,role):
        if name not in self.name_to_role_dict:
            self.name_to_role_dict[name]= role
        else:
            print("The name is already exits go for a edit the name ")
    
    def edit(self,name,role):
        if name in self.name_to_role_dict:
            self.name_to_role_dict[name]= role
        else:
            print("The name is not exits so add the name with role")
    
    def delete(self,name):
        if name in self.name_to_role_dict:
            del self.name_to_role_dict[name]
        else:
            print("The name you want to delete it's not exits ")
