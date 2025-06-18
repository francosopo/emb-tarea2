class DataController():

    def __init__(self, model):

        self.model = model

    def add_data(self, d):
        self.model.add_data(d)

    def show_data(self):
        return self.model.retrieve_data()