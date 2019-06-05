import pytest
import sys
import asyncio
import inspect
import re
import time


pytestmark = pytest.mark.asyncio
io_test_pattern = re.compile("io_.*")


async def tests(subtests):

    def find_io_tests(subtests, ignored_names):
        functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
        for (f_name, function) in functions:
            if f_name in ignored_names:
                continue
            if re.search(io_test_pattern, f_name):
                yield run(subtests, f_name, function)

    async def run(subtests, test_name, test_function):
        with subtests.test(msg=test_name):
            await test_function()

    self_name = inspect.currentframe().f_code.co_name
    return await asyncio.gather(*find_io_tests(subtests, {self_name}))




async def io_test_1():
    await assert_sleep_duration_ok(1)

async def io_test_2():
    await assert_sleep_duration_ok(2)

async def io_test_3():
    await assert_sleep_duration_ok(3)

async def io_test_4():
    await assert_sleep_duration_ok(4, fail=True)

MAX_ERROR = 0.1

async def assert_sleep_duration_ok(duration, fail=False):
    start = time.time()
    await asyncio.sleep(duration)
    actual_duration = time.time() - start
    assert abs(actual_duration - duration) < MAX_ERROR
    assert not fail