class Restauran:
    def __init__(self,name,num_of_dishes,adress,num_of_tables):
        self.name=name
        self.num_of_dishes = num_of_dishes
        self.adress = adress
        self.num_of_tables = num_of_tables
    def str(self):
        return self.name + " "\
    + self.num_of_dishes + " "\
    + self.adress + " "\
    + self.num_of_tables


