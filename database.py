class TodoItem():
    def __init__(self, text):
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
        self.todos = []
        self.docs = []
    def addTodo(self, todo:TodoItem) -> None:
        self.todos.append(todo)
    def addDoc(self, doc):
        self.docs.append(doc)
    def getTodos(self):
        return [dict(done=td.done,
                     text=td.text)
                for td in self.todos]
    def getDocs(self):
        return self.docs