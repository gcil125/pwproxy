import asyncio
from playwright._impl._impl_to_api_mapping import ImplToApiMapping
from playwright.sync_api import Route
from .function import *

import builtins

mapping = ImplToApiMapping()


def stop():
    import nest_asyncio
    nest_asyncio.apply()

    async def inner():
        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        fut.set_result("1")
        await fut
    asyncio.run(inner())


setattr(builtins, "stop", stop)

for func in function.__all__:
    setattr(Route, func, getattr(function, func))
