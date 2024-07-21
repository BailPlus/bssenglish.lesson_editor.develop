#Copyright Bail 2021-2023
#bssenglish:libwordclass 单词类模块(阉割版)

class Word:
    '''单词类'''
    def __init__(self,word:str,pronounce:str,trans:str):
        self.word = word
        self.pronounce = pronounce
        self.trans = trans
    def __str__(self)->str:
        return self.word
    def __eq__(self,b):
        if self.word == b.word:
            return True
        else:
            return False
class Lesson:
    '''课程类'''
    def __init__(self,words:tuple,md5:str,progress:list,**info):
        '''课程类初始化
info:课程信息。包括:
- name(str):课程简称（用于显示）
- fullname(str):课程全称
- author(str):课程作者/编写者（推荐附上邮箱，如：Bail <2915289604@qq.com>）
- file_version(int):文件版本
words(tuple):课程中包括的单词。元组中的对象类型为Word
md5(str):课程文件的md5值，作为ID
progress(list):学习进度。长度为3，类型为int，依次为记忆、听写、默写的学习进度'''
        self.name = info['name']
        self.fullname = info['fullname']
        self.author = info['author']
        self.file_version = info['file_version']
        self.words = words
        self.md5 = md5
        self.progress = progress
##    def __iter__(self):
##        return self.words
