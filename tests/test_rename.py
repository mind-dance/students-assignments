import os
import unittest

from client.rename import get_all_file


class Test_rename(unittest.TestCase):
    def test_get_file(self):
        # 可以优化一下，开始之前创建temp文件夹，用完之后直接删了。



        current_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = os.path.join(current_path, 'temp')
        os.chdir(temp_path)
        # 批量创建文件和文件夹
        folders = ["folder1","folder2","folder3"]
        files = ["file1.txt", "file2.txt", "file3.txt"]
        # folders = ["Don't panic", "42", "The answer of everything"]
        # files = ["The Hitchhiker's Guide to the Galaxy.txt", "The Restaurant at the End of the Universe.mobi", "Life, the Universe and Everything.azw3", "So Long, and Thanks for All the Fish.epub", "Mostly Harmless.pdf"]
        for item in folders:
            os.makedirs(item, exist_ok=True)
        for item in files:
            with open(item, 'w') as f:
                f.write('This is a test file.')
        # 测试函数
        get_file = get_all_file(temp_path)
        self.assertEqual(get_file, files)
        # 清理缓存
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            if os.path.isdir(item_path):  # 如果是文件夹
                os.rmdir(item_path)
            elif os.path.isfile(item_path):  # 如果是文件
                os.remove(item_path)




