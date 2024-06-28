import pytest


@pytest.mark.usefixtures("init_driver", "log_on_failure")
class BaseTest:
    pass
