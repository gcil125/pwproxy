import asyncio

from playwright._impl._impl_to_api_mapping import ImplToApiMapping
from playwright.sync_api import Page
import pytest


@pytest.fixture(autouse=True)
def reset_stop():
    mapping = ImplToApiMapping()

    def stop(self):
        async def pause() -> None:
            async def a():
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
