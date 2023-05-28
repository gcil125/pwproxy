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
        await loop.create_future()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(inner())


setattr(builtins, "stop", stop)

for func in function.__all__:
    setattr(Route, func, getattr(function, func))
