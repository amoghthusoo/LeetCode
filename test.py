import sys
from multiprocessing import Process

def main():
    i = 1
    product = 1
    while(True):
        product *= i
        sys.set_int_max_str_digits(len(str(product)) * 640)
        print(product)
        i += 1

if(__name__ == "__main__"):
    
    while(True):
        Process(target=main).start()