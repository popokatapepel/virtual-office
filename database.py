class TodoItem():
    def __init(self, text):
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
    def addTodo(self, todo):
        self.todos.append(todo)
    def addDoc(self, doc):
        self.docs.append(doc)
    def getTodos(self):
        return self.todos
    def getDocs(self):
        return self.docs