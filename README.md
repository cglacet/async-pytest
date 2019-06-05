# Investigating synchronous tests using pytest

The goal is to run several tests concurrently using asyncio (/curio/trio/...) together with pytest.

Comments suggested to use [pytest-xdist][pytest-xdist] (a thread based solution) but I was curious
about the other alternative that was suggested:
 [pytest-subtests][pytest-subtests].

 I implemented a short test suite to investigate how good a solution
 usin [`pytest-subtests` + `asyncio`](asyncio_test.py) (resp. [`pytest-subtests` + `trio`](trio_test.py)) would be.

 Here is what the output of `pytest -v` looks like:

 ```
================================================= test session starts ==================================================
platform darwin -- Python 3.7.0, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- /Users/cglacet/test/async-tests/.venv/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/cglacet/test/async-tests
plugins: asyncio-0.10.0, trio-0.5.2, subtests-0.2.1
collected 2 items

asyncio_test.py::tests PASSED                                                                                    [ 50%]
asyncio_test.py::tests PASSED                                                                                    [ 50%]
asyncio_test.py::tests PASSED                                                                                    [ 50%]
asyncio_test.py::tests PASSED                                                                                    [ 50%]
asyncio_test.py::tests PASSED                                                                                    [ 50%]
trio_test.py::tests PASSED                                                                                       [100%]
trio_test.py::tests PASSED                                                                                       [100%]
trio_test.py::tests PASSED                                                                                       [100%]
trio_test.py::tests PASSED                                                                                       [100%]
trio_test.py::tests PASSED                                                                                       [100%]

=============================================== 2 passed in 8.06 seconds ===============================================
 ```

 Goals:
  - Have a cleaner output with subtests names and more accurate progression percentage.
  - Try more complex examples.

[pytest-xdist]: https://pypi.org/project/pytest-xdist/
[pytest-subtests]: https://pypi.org/project/pytest-subtests/
