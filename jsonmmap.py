#!/usr/bin/python
# -*- coding: utf-8 -*-
import test_mmap
import json


class ObjectMmap(test_mmap.test_mmap):

    """

    :param fileno: the file handle
    :param length: memory size
    :param access:
    :param tagname:
    """

    def __init__(self, fileno=-1, length=1024, access=test_mmap.ACCESS_WRITE, tagname='share_mmap'):
        super(ObjectMmap, self).__init__(self, fileno, length, access=access, tagname=tagname)
        self.length = length
        self.access = access
        self.tagname = tagname

    def jsonwrite(self, obj):
        """

        :param obj:
        :return:
        """
        try:
            self.obj = obj
            self.seek(0)
            obj_str = json.dumps(obj)
            obj_len = len(obj_str)
            content = str(obj_len) + ":" + obj_str
            self.write(content)
            self.contentbegin = len(str(obj_len)) + 1
            self.contentend = self.tell()
            self.contentlength = self.contentend - self.contentbegin
            return True
        except Exception as e:
            return False

    def jsonread_master(self):
        try:
            self.seek(self.contentbegin)
            content = self.read(self.contentlength)
            obj = json.loads(content)
            self.obj = obj
            return obj
        except Exception as e:
            if self.obj:
                return self.obj
            else:
                return None

    def jsonread_follower(self):
        try:
            self.seek(0)
            index = self.find(":")
            if index != -1:
                head = self.read(index + 1)
                contentlength = int(head[:-1])
                content = self.read(contentlength)
                obj = json.loads(content)
                self.obj = obj
                return obj
            else:
                return None
        except Exception as e:
            if self.obj:
                return self.obj
            else:
                return None