from collections import Counter, OrderedDict

if __name__ == '__main__':

    class OrderedCounter(Counter, OrderedDict):
        pass
      
    letters = OrderedCounter(sorted(input())).most_common(3)
    
    [print(*letter) for letter in letters]
