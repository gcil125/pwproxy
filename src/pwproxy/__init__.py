import asyncio
from playwright._impl._impl_to_api_mapping import ImplToApiMapping
from playwright.sync_api import Route, Page
from .function import *


mapping = ImplToApiMapping()


# def stop():
#     import nest_asyncio
#     nest_asyncio.apply()
#
#     async def inner():
#         loop = asyncio.get_running_loop()
#         await loop.create_future()
#
#     asyncio.run(inner())

def stop(self):
    async def pause() -> None:
        async def a():
            while True:
                await asyncio.sleep(1)

        await asyncio.wait(
            [
                asyncio.create_task(a()),
                self._impl_obj._closed_or_crashed_future,
            ],
            return_when=asyncio.FIRST_COMPLETED,
        )

    return mapping.from_maybe_impl(self._sync(pause()))


setattr(Page, "stop", stop)

for func in function.__all__:
    setattr(Route, func, getattr(function, func))
