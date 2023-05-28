import asyncio
import builtins

import pytest


@pytest.fixture(autouse=True)
def reset_stop():
    def _stop():
        import nest_asyncio
        nest_asyncio.apply()

        async def inner():
            loop = asyncio.get_running_loop()
            fut = loop.create_future()
            fut.set_result("1")
            await fut

        asyncio.run(inner())

    setattr(builtins, "stop", _stop)
