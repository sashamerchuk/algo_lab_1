from restauran import Restauran

def read_file(restauran):
    with open(restauran,'r') as file_path:
        list_restaurants=[]
        for line in file_path:
            line=line.strip('\n').split(",")
            list_restaurants.append(Restauran(line[0],line[1],line[2],line[3]))
    return list_restaurants
