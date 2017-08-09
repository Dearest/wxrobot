import os
import random
class MeiZiTu:
    @staticmethod
    def pics():
        path = '/home/zhou/meizitu/'
        filenames = []
        return [[os.path.join(root, name) for name in files] for root, dirs, files in os.walk(path)]
        # for root, dirs, files in os.walk(path):
        #     for name in files:
        #         filenames.append(os.path.join(root, name))
        # return filenames

    @staticmethod
    def random_pic_path():
        names = list(fliter(lambda x:len(x) > 0, MeiZiTu.pics()))
        return names[random.randint(1, len(names))]