class TodoItem():
    def __init__(self, text, id):
        self.id=id
        self.text = text
        self.done = False
    def setText(self, text):
        self.text = text
    def getText(self):
        return self.text
    def setDone(self, done):
        self.done = done
    def getDone(self):
        return self.done

class Database():
    def __init__(self):
        self.todocounter=-1
        self.todos = []
        self.docs = []
    def addTodo(self, todo_text:str) -> None:
        self.todocounter+=1
        self.todos.append(TodoItem(todo_text,
                                   self.todocounter))
    def addDoc(self, doc):
        self.docs.append(doc)
    def getTodos(self):
        return [dict(id=td.id,
                     done=td.done,
                     text=td.text)
                for td in self.todos]
    def getDocs(self):
        return self.docs