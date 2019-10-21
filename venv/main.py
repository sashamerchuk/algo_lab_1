from file import read_file
from algorithm_1 import selection_sort
from algorithm_1 import mergeSort

def main():
    list_restaurants = read_file('c:/Users/User/Desktop/algorithm_1/venv/restauranFile.TXT')
    selection_sort(list_restaurants)
    mergeSort(list_restaurants)

if __name__ == '__main__':
    main()
