# !/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import time

def timer(func):
    """ 
    Print the runtime of the decorated function
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # the time just before the func starts running
        value = func(*args, **kwargs)
        end_time = time.perf_counter()   # the time just before the func finishes running
        run_time = end_time - start_time # time intervals
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(999)
"""
If you want to do more precise
measurements of code, you should instead consider the timeit
module in the standard library. It temporarily disables garbage
collection and runs multiple trials to strip out noise from quick
function calls.
"""

# Debugging Code

import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        """The f-string formats each
            argument as key=value where the !r specifier means that repr()
            is used to represent the value."""
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age = None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Ranke")
make_greeting(["ranke","tao"], 20)

import math

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    """
    get an approximation to the true value e = 2.718281828
    """
    return sum(1/ math.factorial(n) for n in range(terms))

approximate_e(5)

import functools
import time

def slow_down(func):
    """ Sleep 1 second before calling the function """
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def CountDown(from_number):
    if from_number < 1:
        print("Lift off!")
    else:
        print(from_number)
        CountDown(from_number - 1)

CountDown(5)

# Decorators don’t have to wrap the function they’re decorating.
import random
PLUGINS = dict() # global PLUGINS dict.

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name), type(greeter), type(greeter_func)

randomly_greet("Lucy")

from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(func):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

# Decorating classes 
# (1)decorate the methods of a class

# from decorators import debug, timer  此文件中已有debug， timer，所以无需导入

class TimeWaster:
    @debug
    def __init__(self, max_num):
            self.max_num = max_num
    
    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

tw = TimeWaster(1000)
tw.waste_time(999)

# (2)decorate the whole class

@timer # only measures the time it takes to instantiate the class
class TimeWaster:
    def __init__(self, max_num):
            self.max_num = max_num
    
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

tw = TimeWaster(1000)
tw.waste_time(999)

# Nesting Decorators
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("NaNa")

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")

greet("NaNa")

#Decorator with arguments
def repeat(_func = None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat #定义默认为2次
def say_whee():
    print("Whee!")
@repeat(num_times = 4)
def greet(name):
    print(f"Hello {name}")

say_whee()
greet("NaNa")

#stateful decorator
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

say_whee()
say_whee.num_calls

# Classes as decorators

class Counter:
    def __init__(self, start = 0):
            self.count = start
    def __call__(self):
        self.count +=1
        print(f"Current count is {self.count}")

counter = Counter()
counter()
counter.count

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self,func)
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")

say_whee()
say_whee.num_calls

# Slowing Down code
import functools
import time

def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down
    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)

@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Lift off!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)
#Creating Singleton

import functools

def singleton(cls): # using cls instead of func as the parameter name to indicate that it is meant to be a class decorator.
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

first_instance = TheOne()
second_instane = TheOne()
id(first_instance)
id(second_instane)
first_instance is second_instane

#Caching Return Values

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)

fibonacci(10) # needs a whopping 177 calculations

#simple caching of the calculations reduce times of function callls
import functools

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args +tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10) # call 11 time fibonacci func
fibonacci(8) 
"""no new calculations were needed, since the eighth Fibonacci number had already been
 calculated for fibonacci(10)."""

# use @functools.lru_cache instead of writing your own cache decorator
import functools
@functools.lru_cache(maxsize=4) # 只存储最近的4个运算结果
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(4)
fibonacci(8)
fibonacci(3)
fibonacci(10)
# Adding Information About Units
# Validating JSON