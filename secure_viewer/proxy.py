class AccessProxy:
    def __init__(self, document, user):
        self._document = document
        self._user = user

    def display(self,title):
        if self._user.role == 'admin' or self._user.role == 'user':
            return self._document.display(title)
        else:
            return "Access Denied: You do not have permission to view this document."
        
    def add(self,title,content):
        if self._user.role == 'admin' or self._user.role == 'user':
            return self._document.add(title,content)
        else:
            return "Access Denied: You do not have permission to add a title with document."
    
    def delete(self,title):
        if self._user.role == 'admin' or self._user.role == 'user':
            return self._document.delete(title)
        else:
            return "Access Denied: You do not have permission to delete a title in document."
