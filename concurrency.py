from typing import List, Union

"""
Concurrency vs Parallelism

Concurrency, parallelism, and multi-threading are three terms that areoften mistaken for
one another. Actually, differentiating between them can be a bit confusing.

However, it's quite easy to differentite and I'll try to do that as follows:

--> Multithreading is the ability of a system to excute multiple tasks in simultaneously.
    That is, the system is able to do another task while also currently doing one.

---> Concurrency is the ability of a system to excute multiple tasks in an overlapping mannner.
    That is, while doing one task, it can start doing another one while waiting for the first.
    This typically happens on a single processor. Hence, the processor starts working on a new
    task while the current one is waiting using some other system resources.
    It doesn't necessarily mean the multiple tasks will be running at the same time.

---> Parallelism is the ability of a system to excute multiple tasks at the same time on
    multiple processors.

---> Concurrency and Parallelism are both types of Multithreading

---> Concurrency is asynchronous. That is, non-sequental.
---> Parallelism is synchronous. That is, sequential.

---> Concurrency uses a non-deterministic control flow.
---> Parallelism uses a deterministic control flow.

TL;DR

** Concurrency is ideal for I/O-boud tasks
** Parallelism is ideal for CPU-bound tasks


Async X FastAPI


FastAPI relies on concurrency using the async-await syntax. This makes it ideal for web APIs,
particularly those associated with data science/ML systems.
You can also achieve parallelism in FastAPI.



Async - Await

async-await is Python's (and JS's) way of abstracting the complexities of implementing concurrent code.

---> An Asynchronously function must be defined with `async def`
---> Every async function can only be called by preceding it with the await keyword.
        `await my_async_func()`
---> An async function can only be called from inside an async function


Coroutines

Coroutines collectively refers to the functionalities provided by the async-await syntax but
particularly refers to the returned value of an aynchronous function.

"""


async def process_users(name: Union[List[str], None]) -> List[str]:
    # doing some cool asynchronous stuff like db query, api call and all
    return name

async def get_user(name: List[str]) -> str:
    # Get a single user from the processed ones
    users = await process_users(None)
    return "User!"