"""
用于 selenium 执行中可以增加录制视频的条件， 以便回放错误， 解决问题

"""
from __future__ import with_statement

import os
import signal
from subprocess import Popen, PIPE

import py
import pytest

unicode = py.builtin.text

VIDEO_SAVE_PATH = "VIDEO_SAVE_PATH"
FFMPEG_COMMAND = "FFMPEG_COMMAND"


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group._addoption(
        '--record', action="store",
        default="single",
        metavar="method", choices=['single', 'all'],
        help="ffmpeg record video of desktop")
    group._addoption(
        '-R', action="store_const", const="single", dest="record",
        help="shortcut for --record=single.")
    parser.addini(VIDEO_SAVE_PATH, 'record desktop video save path')
    parser.addini(FFMPEG_COMMAND, 'use ffmpeg to record video, need the ffmpeg command')



def pytest_configure(config):
    if config.option.__dict__.get('record', None):
        base_path = config.getini(VIDEO_SAVE_PATH)

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        path = os.path.join(base_path, 'test.avi')
        print(path)
        if os.path.exists(path):
            os.remove(path)
        command = config.getini(FFMPEG_COMMAND)
        full_command = "{} {}".format(command, path)
        print(full_command)
        process = Popen(
            full_command,
            shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        config.option.__dict__['__process'] = process


@pytest.mark.trylast
def pytest_unconfigure(config):
    process = config.option.__dict__.get('__process', None)
    if process:
        # out, error = process.communicate()
        # print(out, error)
        # os.kill(process.pid, signal.CTRL_C_EVENT)
        # print(process.pid)
        process.stdin.write(b'q')
        process.stdin.flush()


class Recording:
    def __init__(self, command, path, option):
        self.command = command
        self.path = path
        self.option = option

    def record(self, path):
        process = Popen(
            "{} {}".format(self.command, path),
            shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        self.__process = process

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_setup(self, item):
        if self.option == 'single':
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            path = os.path.join(self.path, item.__name__ + '.avi')
            if os.path.exists(path):
                os.remove(path)
            self.record(path)
        yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_teardown(self, item):
        yield
        if self.option == 'single':
            if getattr(self, '__process', None):

                os.kill(self.__process.pid, signal.CTRL_C_EVENT)
