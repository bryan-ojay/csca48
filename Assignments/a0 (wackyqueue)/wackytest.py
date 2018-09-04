from wackyqueue import *
import unittest


class TestWackyQueue(unittest.TestCase):

    def test_queue_no_elements(self):
        '''Testing that queue shows as empty after inserting and extracting
        an element.'''
        queue = WackyQueue()
        result = queue.getoddlist() is None and queue.getevenlist() is None
        expected = True
        self.assertEqual(result, expected, "The lists did not show as empty.")

    def test_queue_one_element(self):
        '''Testing that one inserted item shows in oddlist'''
        queue = WackyQueue()
        queue.insert('a', 1)
        result1 = queue.getoddlist().get_item() == 'a'
        result2 = queue.getoddlist().get_priority() == 1
        result3 = queue.getevenlist() is None
        result = result1 and result2 and result3
        expected = True
        self.assertEqual(result, expected,
                        "The item was not properly inserted into the queue.")

    def test_queue_odd_elements_forward(self):
        '''Testing for three elements inserted from highest to lowest
        priority'''
        queue = WackyQueue()
        queue.insert('a', 3)
        queue.insert('b', 2)
        queue.insert('c', 1)

        result1 = queue.getoddlist().get_item() == 'a'
        result2 = queue.getoddlist().get_next().get_item() == 'c'
        result3 = queue.getevenlist().get_item() == 'b'

        result = result1 and result2 and result3
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order")

    def test_queue_odd_elements_lowest(self):
        '''Testing for five elements inserted from lowest to highest priority
        '''
        queue = WackyQueue()
        queue.insert('a', 1)
        queue.insert('b', 2)
        queue.insert('c', 3)
        queue.insert('d', 4)
        queue.insert('e', 5)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3 = (even1.get_next(),
                        even1.get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('e', 'c', 'a', None)
        result2 = (even1._item, even2._item, even3) == ('d', 'b', None)
        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")

    def test_queue_odd_elements_random(self):
        '''Testing for five elements inserted in the queue in random order.
        '''
        queue = WackyQueue()
        queue.insert('c', 3)
        queue.insert('e', 5)
        queue.insert('b', 2)
        queue.insert('a', 1)
        queue.insert('d', 4)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3 = (even1.get_next(),
                        even1.get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('e', 'c', 'a', None)
        result2 = (even1._item, even2._item, even3) == ('d', 'b', None)
        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")


    def test_queue_odd_elements_same_priority(self):
        '''Testing for five elements with the same priority inserted into
        the queue'''
        queue = WackyQueue()
        queue.insert('a', 3)
        queue.insert('b', 3)
        queue.insert('c', 3)
        queue.insert('d', 3)
        queue.insert('e', 3)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3 = (even1.get_next(),
                        even1.get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('a', 'c', 'e', None)
        result2 = (even1._item, even2._item, even3) == ('b', 'd', None)
        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")

    def test_queue_even_elements_forward(self):
        '''Testing for four elements inserted from highest to lowest
        priority'''
        queue = WackyQueue()
        queue.insert('a', 4)
        queue.insert('b', 3)
        queue.insert('c', 2)
        queue.insert('d', 1)

        result1 = queue.getoddlist().get_item() == 'a'
        result2 = queue.getoddlist().get_next().get_item() == 'c'
        result3 = queue.getevenlist().get_item() == 'b'
        result4 = queue.getevenlist().get_next().get_item() == 'd'

        result = result1 and result2 and result3 and result4
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order")

    def test_queue_even_elements_lowest(self):
        '''Testing for six elements inserted from lowest to highest priority
        '''
        queue = WackyQueue()
        queue.insert('a', 1)
        queue.insert('b', 2)
        queue.insert('c', 3)
        queue.insert('d', 4)
        queue.insert('e', 5)
        queue.insert('f', 6)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3, even4 = (even1.get_next(),
                               even1.get_next().get_next(),
                               even1.get_next().get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('f', 'd', 'b', None)
        result2 = (even1._item, even2._item,
                   even3._item, even4) == ('e', 'c', 'a', None)

        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")

    def test_queue_even_elements_random(self):
        '''Testing for six elements inserted in the queue in random order.
        '''
        queue = WackyQueue()
        queue.insert('c', 3)
        queue.insert('e', 5)
        queue.insert('b', 2)
        queue.insert('f', 6)
        queue.insert('a', 1)
        queue.insert('d', 4)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3, even4 = (even1.get_next(),
                               even1.get_next().get_next(),
                               even1.get_next().get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('f', 'd', 'b', None)
        result2 = (even1._item, even2._item,
                   even3._item, even4) == ('e', 'c', 'a', None)

        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")


    def test_queue_even_elements_same_priority(self):
        '''Testing for six elements with the same priority inserted into
        the queue'''
        queue = WackyQueue()
        queue.insert('a', 3)
        queue.insert('b', 3)
        queue.insert('c', 3)
        queue.insert('d', 3)
        queue.insert('e', 3)
        queue.insert('f', 3)

        odd1 = queue.getoddlist()
        odd2, odd3, odd4 = (odd1.get_next(),
                            odd1.get_next().get_next(),
                            odd1.get_next().get_next().get_next())

        even1 = queue.getevenlist()
        even2, even3, even4 = (even1.get_next(),
                               even1.get_next().get_next(),
                               even1.get_next().get_next().get_next())

        result1 = (odd1._item, odd2._item,
                   odd3._item, odd4) == ('a', 'c', 'e', None)
        result2 = (even1._item, even2._item,
                   even3._item, even4) == ('b', 'd', 'f', None)

        result = result1 and result2
        expected = True
        self.assertEqual(result, expected,
                        "The items were not inserted in the right order.")


if(__name__ == "__main__"):
    unittest.main(exit=False)
