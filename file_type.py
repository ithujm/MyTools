# -*- coding = utf-8 -*-
# @Time: 2023/1/30 20:55
# @Author:hjm
# @File：file_type.py
# @Software: PyCharm

import os
import shutil

BASE_DIR = os.path.dirname(__file__)


class FileTypeTool(object):
    def __init__(self):
        self.apps_dir = r"D:/apps"
        self.app_suffix_lst = [".zip", ".gz", ".exe", ".tar"]
        self.ignore_suffix_lst = [".git", ".idea"]
        self.pre_dir_name = "all_"

    def file_job(self, file):

        suffix = os.path.splitext(file)[-1]
        file = os.path.abspath(file)
        suffix_dir = os.path.join(BASE_DIR, "{}{}".format(self.pre_dir_name, suffix))
        if suffix in self.ignore_suffix_lst or file == __file__:
            return
        if not os.path.isdir(suffix_dir):
            os.mkdir(suffix_dir)
        try:
            if suffix in self.app_suffix_lst:
                shutil.copy(file, self.apps_dir)
            shutil.move(file, suffix_dir)
        except FileExistsError:
            pass

    def run(self):
        for _f in os.listdir(BASE_DIR):
            f_path = os.path.join(BASE_DIR, _f)
            if os.path.isfile(f_path):
                self.file_job(f_path)


if __name__ == '__main__':
    case = FileTypeTool()
    case.run()
