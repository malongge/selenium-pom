import pytest


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group._addoption(
        '--once', action="store",
        default='no',
        metavar="method", choices=['yes', 'no'],
        help="跳过一次运行的任务")
    group._addoption(
        '-1', action="store_const", const="yes", dest="once",
        help="shortcut for --once=yes")


def pytest_runtest_setup(item):
    if 'once' in item.name and item.config.getoption("--once") == 'no':
        pytest.skip("need --once=yes option to run")
