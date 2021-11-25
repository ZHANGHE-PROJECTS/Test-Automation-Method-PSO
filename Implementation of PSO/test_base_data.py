#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhang He
# @File    : test_base_data.py
# @Contact : 2110194@tongji.edu.cn
# @From    : Tongji University

import pandas as pd
import numpy as np

class testBaseData:
    def __init__(self,path,name=['vs','dif_speed','dis']):
        self.data = pd.read_csv(path)
        self.name = name
        print(self.data.shape)
    def test(self,sample):
        sample_frame = pd.DataFrame(sample)
        sample_frame.columns = self.name #变成dataframe格式
        sample_frame = sample_frame.merge(self.data,how='left')#left 左连接， 左侧取全部信息，右侧没有的变为NAN”
        return np.array(sample_frame['result'])

if __name__ == "__main__":
    sut = testBaseData("Testing_Results.csv")
    res = sut.test([[0,10,5],[3,-15,7]])
    print(res)