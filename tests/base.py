import inspect
import signal
import os
import sys
from subprocess import call, PIPE, Popen
import requests

class BaseTest(object):
    def get_methods(self, starting_with, reverse=False):
        methods = []
        members = inspect.getmembers(self, predicate=inspect.ismethod)
        members = sorted(members, key=lambda m: m[0], reverse=reverse)
        for m in members:
            name, method = m
            if name.startswith(starting_with):
                methods.append(method)
        return methods

    def setup_method(self, method):
        for meth in self.get_methods("set_up"):
            meth(method)

    def teardown_method(self, method):
        for meth in self.get_methods("tear_down", reverse=True):
            meth(method)

    def _check_link_request_code(self, url):
        if url is None:
            return True
        try:
            return requests.get(url, timeout=5).status_code == 200
        except Exception as e:
            print(str(e))




def terminate(process):
    if process.poll() is None:
        call(r'taskkill /F /T /PID ' + str(process.pid))


ffmpeg_command = os.environ['ffmpeg_command']
video_base_path = os.environ['video_base_path']


class BaseRecordTest(BaseTest):
    def set_up_00(self, method):

        # video save path should be "base path" + "test case module path" + "test case class" + "test case name"
        module_name = self.__module__
        if module_name == '__main__':
            filename = sys.modules[self.__module__].__file__
            module_name = os.path.splitext(os.path.basename(filename))[0]
        module_path = module_name.replace('.', '\\')
        dir_name = video_base_path + module_path
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        video_path = dir_name + '\{}-{}.avi'.format(self.__class__.__name__, method.__name__)

        if os.path.exists(video_path):
            os.remove(video_path)

        process = Popen(
            "{} {}".format(ffmpeg_command, video_path),
            shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        self.__process = process

    def tear_down_99(self, method):
        # self.__process.terminate()
        # os.killpg(self.__process.pid, signal.CTRL_C_EVENT)
        # os.kill(self.__process.pid, signal.CTRL_C_EVENT)
        # terminate(self.__process)

        self.__process.stdin.write(b'q')
        # self.__process.stdin.flush()
