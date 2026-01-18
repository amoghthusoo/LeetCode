from threading import Semaphore
class Foo:
    def __init__(self):
        self.s2 = Semaphore(0)
        self.s3 = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s2.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.s2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.s3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()