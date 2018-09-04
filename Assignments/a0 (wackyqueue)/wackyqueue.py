"""
# Copyright Nick Cheng, 2018
# Copyright Bryan Oladeji, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


class WackyQueue:
    '''A class representing a wacky queue'''

    def __init__(self):
        '''(WackyQueue) -> NoneType
        Initializes an empty WackyQueue.
        '''
        # Representation Invariant:
        # WackyQueue is made up of 2 linked lists:
        # if not (self.isempty()):
        #     _oddhead is a dummy WackyNode that points to the first entered
        #     node and every alternate node entered after iT
        #     _evenhead is a dummy WackyNode that points to the second entered
        #     node and every alternate node entered after it
        # else:
        #     _oddhead points to None
        #     _evenhead points to None
        self._oddhead = WackyNode(None, 0)
        self._evenhead = WackyNode(None, 0)

    def insert(self, obj, pri):
        '''(WackyQueue, obj, int) -> NoneType
        Inserts the object into the wacky queue with the given priority.
        Identical objects with the same priority are allowed.
        '''
        # Create node for object
        obj_node = WackyNode(obj, pri)

        # Start traversing from the first item in each list
        odd_prev, odd_cur = self._oddhead, self._oddhead.get_next()
        even_prev, even_cur = self._evenhead, self._evenhead.get_next()

        # Create flag to check if object is not inserted
        not_inserted = True

        # Traverse through both lists until the end is reached or until the
        # object is inserted
        while not_inserted and not (odd_cur is None or even_cur is None):
            # If object has a higher priority than the next biggest object
            # in the oddlist, insert object into oddlist
            if pri > odd_cur.get_priority():
                # All nodes with lower priority in evenlist shift to oddlist
                # All nodes with lower priority in oddlist shift to evenlist
                odd_prev.set_next(obj_node)
                obj_node.set_next(even_cur)
                even_prev.set_next(odd_cur)
                not_inserted = False

            # Else if object's has a higher priority than the next biggest
            # in the evenlist, insert object into evenlist
            elif pri > even_cur.get_priority():
                # All nodes with lower priority in oddlist shift to evenlist
                # All nodes with lower priority in evenlist shift to oddlist
                even_prev.set_next(obj_node)
                obj_node.set_next(odd_cur.get_next())
                odd_cur.set_next(even_cur)
                not_inserted = False

            # Continue traversing through both lists
            odd_prev, odd_cur = odd_cur, odd_cur.get_next()
            even_prev, even_cur = even_cur, even_cur.get_next()

        # if end of queue is reached (a.k.a object priority is the smallest),
        # check if it should be inserted in the odd list or even list:

        # Check if there are an odd number of items in the queue and the object
        # has the 2nd smallest priority
        if (not_inserted and odd_cur is not None and
           pri > odd_cur.get_priority()):
            # Insert the object into the oddlist
            # Shift the smaller items in the oddlist to the even list
            odd_prev.set_next(obj_node)
            even_prev.set_next(odd_cur)

        # Or if there are an even number of items in the queue and the
        # object has the smallest priority
        elif not_inserted and odd_cur is None and even_cur is None:
            # Insert the object into the oddlist
            odd_prev.set_next(obj_node)

        # Or if there are an odd number of items in the queue and the
        # object has the smallest priority
        elif not_inserted and even_cur is None:
            # Insert the object into the evenlist
            even_prev.set_next(obj_node)

    def extracthigh(self):
        '''(WackyQueue) -> obj
        Removes and returns the first item in the wacky queue.
        REQ: self.isempty() == False
        '''
        # Assign variables for the first items in the odd and even lists
        first_odd = self.getoddlist()
        first_even = self.getevenlist()

        # Shift the evenlist items to the oddlist
        # Shift all oddlist items after the oddlist head to the even list
        # Unlink the old oddlist head from the oddlist
        self._oddhead.set_next(first_even)
        self._evenhead.set_next(first_odd.get_next())
        first_odd.set_next(None)

        return first_odd.get_item()

    def isempty(self):
        '''(WackyQueue) -> bool
        Indicates if there are no items in the wacky queue.
        '''
        # Check if there are no heads for both lists
        return ((self.getoddlist() is None) and (self.getevenlist() is None))

    def changepriority(self, obj, pri):
        '''(WackyQueue, obj, int) -> NoneType
        Changes the priority of the first instance of the specified object
        to the given priority. The object will be inserted as a new object
        given the priority changes. If the object does not exist in the wacky
        queue or the object already has the given priority, no changes will be
        made.
        '''
        # Start traversing from the first item in the list
        odd_prev, odd_cur = self._oddhead, self._oddhead.get_next()
        even_prev, even_cur = self._evenhead, self._evenhead.get_next()

        # Create flag to check if the old object was removed from the list
        not_found = True

        # Traverse through both lists until the end is reached or until the
        # object has been found
        while not_found and (odd_cur is not None and even_cur is not None):

            # Check if there is a matching object in the oddlist
            if (obj == odd_cur.get_item()):
                # Mark object as found
                not_found = False
                # Check if the object has a different priority
                if pri != odd_cur.get_priority():
                    # Shift all odd items after the obj up to the evenlist
                    # Shift all even items after the obj up to the oddlist
                    # Unlink the object from the oddlist
                    # Re-insert it with the new priority
                    odd_prev.set_next(even_cur)
                    even_prev.set_next(odd_cur.get_next())
                    odd_cur.set_next(None)
                    self.insert(obj, pri)

            # Else check if there is a matching object in the evenlist
            elif (obj == even_cur.get_item()):
                # Mark object as found
                not_found = False
                # Check if the object has a different priority
                if pri != even_cur.get_priority():
                    # Shift all even items after the obj up to the oddlist
                    # Shift all odd items after the obj up tothe evenlist
                    # Unlink the object from the evenlist
                    # Re-insert it with the new priority
                    even_prev.set_next(odd_cur.get_next())
                    odd_cur.set_next(even_cur.get_next())
                    even_cur.set_next(None)
                    self.insert(obj, pri)

            # Continue traversing through both lists
            odd_prev, odd_cur = odd_cur, odd_cur.get_next()
            even_prev, even_cur = even_cur, even_cur.get_next()

        # Check if there is an odd number of items and the last object in
        # the list is a matching object with a different priority
        if not_found and odd_cur is not None:
            if obj == odd_cur.get_item() and pri != odd_cur.get_priority():
                # Unlink the object from the list and re-insert with the new
                # priority
                odd_prev.set_next(None)
                self.insert(obj, pri)

    def negateall(self):
        '''(WackyQueue) -> NoneType
        Negates the priority of all objects in the wacky queue, and reverses
        the insertion order of the objects in the wacky queue.
        '''
        # If there are no items in the queue, do nothing
        if self.isempty():
            pass

        # Or if there's only one item in the queue, negate the priority of
        # that object
        elif self.getevenlist() is None:
            self.getoddlist().set_priority(-self.getoddlist().get_priority())

        # If there are 2 or more items in the queue, traverse through the
        # whole queue
        else:
            # Start from the first and second items in each list
            odd_cur, odd_next = (self.getoddlist(),
                                 self.getoddlist().get_next())
            even_cur, even_next = (self.getevenlist(),
                                   self.getevenlist().get_next())

            # Negate the priority and reverse the insertion order
            # for the first items in each list
            odd_cur.set_priority(-odd_cur.get_priority())
            even_cur.set_priority(-even_cur.get_priority())
            odd_cur.set_next(None)
            even_cur.set_next(None)

            # Traverse through the rest of the queue
            while (odd_next is not None) and (even_next is not None):
                # Advance through both lists
                (odd_prev, odd_cur, odd_next) = (odd_cur, odd_next,
                                                 odd_next.get_next())
                (even_prev, even_cur, even_next) = (even_cur, even_next,
                                                    even_next.get_next())

                # Negate the priority and reverse the insertion order of the
                # currently traversed items in the queue
                odd_cur.set_priority(-odd_cur.get_priority())
                even_cur.set_priority(-even_cur.get_priority())
                odd_cur.set_next(odd_prev)
                even_cur.set_next(even_prev)

            # If there are an odd number of items in the queue, negate the
            # priority of the last item and reverse its insertion order
            if odd_next is not None:
                odd_next.set_priority(-odd_next.get_priority())
                odd_next.set_next(odd_cur)
                # Set the head of the oddlist as the new first oddlist item
                # Set the head of the evenlist as the new first evenlist item
                self._oddhead.set_next(odd_next)
                self._evenhead.set_next(even_cur)

            # Or if there are an even number of elements, flip the oddlist head
            # and the evenlist head
            else:
                self._oddhead.set_next(even_cur)
                self._evenhead.set_next(odd_cur)

    def getoddlist(self):
        '''(WackyQueue) -> WackyNode or NoneType
        Returns a pointer linked to the first node entered into the wackyqueue
        along with every alternate node entered after it.
        Returns None if there are no items in the queue.
        '''
        return self._oddhead.get_next()

    def getevenlist(self):
        '''(WackyQueue) -> WackyNode or NoneType
        Returns a pointer linked to the first node entered into the wackyqueue
        along with every alternate node entered after it.
        Returns None if there are no items in the queue.
        '''
        return self._evenhead.get_next()

    def __str__(self):
        '''(WackyQueue) -> str
        Returns the oddlist and evenlist of the wackyqueue as a string
        '''
        return str(self.getoddlist()) + '\n' +  str(self.getevenlist())
