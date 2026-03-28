'''
Created on 1 May 2020

@author: shree
'''


class book:
    '''
    classdocs
    '''

    def __init__(self, id=None, title=None):
        '''
        Constructor
        '''
        self.id = id
        self.title = title


    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

