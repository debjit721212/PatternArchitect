class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.content_dict = {}
        self.content_dict[self.title]=self.content

    def display(self,title):
        return f"Document: {title}\nContent: {self.content_dict.get(title,'This title has no content ')}"
    
    def add(self,title,content):
        if title not in self.content_dict:
            self.content_dict[title]=content
        else:
            print("Title already exits so create a new title")
    
    def delete(self,title):
        if title in self.content_dict:
            del self.content_dict[title]
        else:
            print("Title is not exits please share me a proper title")
    
    
