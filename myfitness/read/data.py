class readdata:
    def __init__(self, file, name):
        self.file = file
        self.name = name

    def data(self):
        import pandas as pd
        self.data = pd.read_csv(self.file)
        return self.data

    def getname(self):
        return self.name
