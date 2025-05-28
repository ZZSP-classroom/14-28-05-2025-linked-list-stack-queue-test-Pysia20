import unittest
from playlist_menager import *

class tests(unittest.TestCase):
    def test_add(self):
        manager = LinkedList()
        self.assertAlmostEqual(manager.sizeOfLL(),0)
        manager.add_song("test","tester")
        self.assertEqual(manager.sizeOfLL(),1)
    def test_add_multiple(self):
        manager = LinkedList()
        self.assertAlmostEqual(manager.sizeOfLL(),0)
        manager.add_song("test","tester")
        self.assertEqual(manager.sizeOfLL(),1)
        manager.add_song("test2","testerr")
        manager.add_song("test3","testerrr")
        manager.add_song("test3","testerrr")
        self.assertEqual(manager.sizeOfLL(),4)
    def test_remove(self):
        manager = LinkedList()
        manager.add_song("test2","testerr")
        manager.add_song("test3","testerrr")
        manager.add_song("test4","testerrrr")
        manager.remove_song("test3")
        self.assertEqual(manager.returnLL()[1].title,"test4")
    def test_get_next(self):
        manager = LinkedList()
        manager.add_song("test2","testerr")
        manager.add_song("test3","testerrr")
        manager.add_song("test4","testerrrr")
        self.assertEqual(manager.get_next_song("test3").title, "test4")
    def test_get_next_none(self):
        manager = LinkedList()
        manager.add_song("test2","testerr")
        manager.add_song("test3","testerrr")
        manager.add_song("test4","testerrrr")
        self.assertEqual(manager.get_next_song("test4"), "")
    def test_get_next_none2(self):
        manager = LinkedList()
        manager.add_song("test2","testerr")
        manager.add_song("test3","testerrr")
        manager.add_song("test4","testerrrr")
        self.assertEqual(manager.get_next_song("test5"), "")
        

if __name__ == '__main__':
    unittest.main()