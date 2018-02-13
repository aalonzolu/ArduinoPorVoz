import importlib

# plugins = ["spotify","arduino","hora"]
plugins = ["hora","spotify"]



class Analyzer:
    def __init__(self):
        print("Inicializando analizado")
        self.modules = self.import_plugins()
        print(self.modules)

    def analize(self, data):
        for m in self.modules:
            action = m.getAction()
            if data['action'] in action:
                return m.analizar(data)
        return False

    def import_plugins(self):
        res = []
        for p in plugins:
            mod = importlib.import_module("modules." + p)
            class_name = dir(mod)[0]
            class_ = getattr(mod, class_name)
            instance = class_()
            res.append(instance)
        return res

