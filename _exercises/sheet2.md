---
layout: default
mathjax: true
title:  Sheet 2
date:   2022-11-01 09:33:19 +0100
categories: exercises 
---

## Sheet 2


Continue the exercises from Sheet 1 on Python programming and use the
instructor to clarify your doubts on this topic. In particular, focus
on the Tasks 13-24 on Numpy. As you should learn from the benchmarks
in Assignment 1, you should always use Numpy to carry out linear
algebra calculations.

You could benchmark your alternative implementations via `list` in
Assignment 1 using the following code:

```python
import time

class Timer(object):  # this is a special class: context manager
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, ty, val, tb):
        end = time.time()
        self.elapsed = end - self.start
        return False


def our_timer(repeats, loops):
    #repeats = 5
    #loops = 1000
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = [0]*repeats
            for i in range(repeats):
                with Timer() as t1:
                    for _ in range(loops):
                        func(*args, **kwargs)
                times[i] = t1.elapsed
                #print(func.__name__, times[i])
            print("best of", str(repeats), "times",str(loops),"executions for", func.__name__, str(min(times
)))
        return wrapper
    return decorator
```
