import os
import unittest
import shutil

from client.rename import get_all_file


class Test_rename(unittest.TestCase):
    def setUp(self):
        # 创建测试文件夹
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.mkdir("temp")

    def tearDown(self):
        # 删除测试文件夹
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        shutil.rmtree("temp")

    def test_get_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = os.path.join(current_path, 'temp')
        os.chdir(temp_path)
        # 批量创建文件和文件夹
        folders = ["folder1", "folder2", "folder3"]
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



