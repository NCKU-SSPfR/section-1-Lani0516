from horrible_fizzbuzz import fizzBuzz
import time

failed_count: int = 0
passed_count: int = 0
total_time: float = 0

def exec_test(func):
    """
    calculate execute time
    and determine whether it is passed or failed
    """
    def wrapper(*args, **kwargs):
        global failed_count
        global passed_count
        global total_time

        res: any = 0

        # count time
        start_time: float = time.time()
        # determine passed or failed
        try:
            res = func(*args, *kwargs)
            passed_count += 1
        except AssertionError:
            failed_count += 1
        end_time: float = time.time()
        total_time += end_time - start_time
        return res
    return wrapper

@exec_test
def test_3():
    assert fizzBuzz(3) == "Fizz"

@exec_test
def test_5():
    assert fizzBuzz(5) == "Buzz"

@exec_test
def test_15():
    assert fizzBuzz(15) == "Fizz" + "Buzz"

@exec_test
def test_2():
    assert fizzBuzz(2) == "2"


# execute unittests
test_3()
test_5()
test_15()
test_2()

# result
print(f"{failed_count} failed, {passed_count} passed in {total_time:.8f}s")