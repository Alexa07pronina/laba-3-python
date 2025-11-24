import pytest
from src.sorting import *
from src.generators import rand_int_array,reverse_sorted,rand_float_array,nearly_sorted,many_duplicates
from src.math_func import fibo,fibo_recursive,factorial_recursive,factorial
from src.data_structures import Stack,Queue
def test_bubble_sort():
    with pytest.raises(TypeError):
        bubble_sort([1,3,4,'a','dfg'])

def test_quick_sort():
    mas = rand_int_array(10, 2, 20)
    sorted_by_quick = quick_sort(mas)
    sorted_by_python = sorted(mas)
    assert sorted_by_quick == sorted_by_python

def test_countinf_sort():
    mas = rand_int_array(15, 3, 50)
    sorted_by_quick = counting_sort(mas)
    sorted_by_python = sorted(mas)
    assert sorted_by_quick == sorted_by_python

def test_radix_sort():
    mas = rand_int_array(7, 3, 50)
    sorted_by_quick = radix_sort(mas,5)
    sorted_by_python = sorted(mas)
    assert sorted_by_quick == sorted_by_python

def test_bucket_sort():
    mas = rand_int_array(7, 3, 50)
    sorted_by_quick = bucket_sort(mas)
    sorted_by_python = sorted(mas)
    assert sorted_by_quick == sorted_by_python

def test_heap_sort():
    mas = rand_float_array(10, 2.0, 5.0)
    sorted_by_quick = heap_sort(mas)
    sorted_by_python = sorted(mas)
    assert sorted_by_quick == sorted_by_python

def test_fibo():
    with pytest.raises(Exception):
        fibo('s')

def test_fibo_rec():
    assert fibo_recursive(20) == 6765

def test_fact():
    assert factorial(5)==120

def test_stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    assert stack.__len__() == 2
    assert stack.pop() == 2
    assert stack.min() == 1

def test_stack_error():
    stack=Stack()
    with pytest.raises(IndexError):
        stack.peek()

def test_queue():
    queue=Queue()
    queue.enqueue(3)
    queue.enqueue('a')
    assert queue.__len__() == 2
    assert queue.front() == 3
    assert queue.dequeue() == 3
    assert queue.is_empty() == False

def test_queue_error():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.front()

def test_generators():
    res = rand_int_array(10,3,100,False,123)
    assert rand_int_array(10,3,100,False,123) == res

def test_many_duplicates():
    res = many_duplicates(10,4,12)
    assert many_duplicates(10,4,12) == res
