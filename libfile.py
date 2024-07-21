# Copyright Bail 2021-2023
# bssenglish:libfile 文件处理模块(阉割版)

import libclass
import json
import csv

LESSON_FILE_HEADER = 'bssenglish lesson file\n' # 课程文件头

def readfile(fn: str) -> libclass.Lesson:
    '''读取课程文件
    fn(str):文件名
    返回值:课程对象(libclass.Lesson)'''
    # 读取课程信息
    with open(fn, encoding='utf-8') as file:
        file.readline()
        lesson_info = json.loads(file.readline())
    # 读取课程内容
    words = tuple(libclass.Word(*i) for i in readfromcsv(fn, 2))
    md5 = 0
    progress_file_name = ''
    progress = [0,0,0]
    lesson = libclass.Lesson(**lesson_info, words=words, md5=md5, progress=progress)  # 使用`words=words`是为了避免参数传乱出现bug
    return lesson

def readfromcsv(fn: str = None, jump_lines: int = 1) -> list:
    '''从csv读取内容
    fn(str):文件名。若不指定则呼出文件选择窗口手动选择
    jump_lines(int):跳过行数。若不指定则跳过第一行
    返回值:二维列表，第一维为每一行，第二维为这一行的每一列(list)'''
    lst = []
    with open(fn, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for index, items in enumerate(reader):
            if index in range(jump_lines):  # 跳过指定行
                continue
            lst.append(items)
    return lst

