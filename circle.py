
import math

def main():
    r = 10
    my_area = area(r)
    print(my_area)

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    main()
