#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


class Coordinates():  # 극좌표 x,y,z / 그대로 쓰기보다는 시선벡터 내부에서 사용
    coordinateX = 0
    coordinateY = 0
    coordinateZ = 0

    def get_coordinates(self):
        # 나중에 구현
        return np.array([self.coordinateX, self.coordinateY, self.coordinateZ])

