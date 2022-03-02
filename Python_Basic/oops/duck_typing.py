# Attributes having same name are
# considered as duck typing

class pycharm:

    def execute(self):
        print("compiling")
        print("running")

class myeditor:

    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class laptop:

    def code(self,ide):
        ide.execute()

ide=myeditor()
lap1= laptop()
lap1.code(ide)
