import numpy as np


# 本次设计第二部分，数据构造器部分，部分代码不太合理，想到哪里整到哪里
# 定义一些常量，这些常量不仅在本模组会用到，在其他模组也会用到


# 常量，基坑支护类型

# 支护结构共11种
LATERAL_EARTH_SUPPORT_STRUCTURE = np.array(['放坡开挖', '土钉墙', '水泥土重力式挡墙', '排桩', '地连墙','SMW', '钢板桩', '混凝土支撑', '钢支撑', '锚杆', '逆作法']) 

# 结构框架数组：（2，5）
FRAME_STRUCTURE = np.array([['支护单元', '支护类型', '支护长度/m', '基坑深度', '标识ID'], ['', '', '', '', ''] ])

class LateralEarthSupport(object):
    """基坑支护结构类"""

    def __init__(self, project_name = '', structure_type = LATERAL_EARTH_SUPPORT_STRUCTURE[0], structure_length = 0.0, excavation_depth = 0.0, sc_range = FRAME_STRUCTURE.copy()):


        # 初始化默认值
        # 支护类型默认为'放坡开挖'
        # 支护长度默认为0m
        # 开挖深度默认为0m
        super.__init__()
        self._project_name = project_name
        self._structure_type = structure_type
        self._structure_length = structure_length
        self._excavation_depth = excavation_depth

        self._struct_range = sc_range.copy()
        self._struct_range[1, 0] = self._project_name
        self._struct_range[1, 1] = self._structure_type
        self._struct_range[1, 2] = self._structure_length
        self._struct_range[1, 3] = self._excavation_depth
        self._struct_range[1, 4] = self._project_name + self._structure_type
    @property
    def project_name(self):
        """"项目名称"""
        return self._project_name

    @project_name.setter
    def project_name(self,proj_name_value):
        self._project_name = str(proj_name_value)


    @property
    def structure_type(self):
        """支护结构类型"""
        return self._structure_type
    
    @structure_type.setter
    def structure_type(self, strucuture_type_value):
        if strucuture_type_value in LATERAL_EARTH_SUPPORT_STRUCTURE:
            self._structure_type = strucuture_type_value
        elif strucuture_type_value not in LATERAL_EARTH_SUPPORT_STRUCTURE:
            raise ValueError('不属于指定类型')

    @property
    def structure_length(self):
        """支护长度"""
        return self._structure_length
    
    @structure_length.setter
    def structure_length(self, structure_length_value):
        if not isinstance(structure_length_value, float):
            raise TypeError('长度必须是数字')
        elif structure_length_value < 0 or structure_length_value > 10000:
            raise ValueError('支护长度范围0~10000m')
        else:
            self._structure_length = structure_length_value

    @property
    def excavation_depth(self):
        """基坑深度"""
        return self._excavation_depth
    
    @excavation_depth.setter
    def excavation_depth(self, excav_depth_value):

        if not isinstance(excav_depth_value, float):
            raise TypeError('excavation depth must be float or integer!')
        elif excav_depth_value < 0 or excav_depth_value > 100:
            raise ValueError('excavation depth must between 0~100m')
        else:
            self._excavation_depth = excav_depth_value
    """
    @property
    def sturct_range(self):
        arrange = self.__struct_range.copy()
        return arrange
    """


class FrameStructure(np.ndarray, ):
    

    def __init__(self, )
def test():
    dem01 = LateralEarthSupport
    dem01.project_name = '1-1'
    dem01.structure_type = LATERAL_EARTH_SUPPORT_STRUCTURE[2]
    dem01.structure_length = 100
    dem01.excavation_depth = 6.0
    arr = dem01._struct_range
    for i in arr.flat:
        print(i)

test()