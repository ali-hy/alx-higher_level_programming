#!/usr/bin/python3
'''my rebelious int'''


class MyInt(int):
    '''switched eq and ne'''
    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
