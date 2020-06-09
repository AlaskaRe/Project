# -*- coding: UTF-8 -*-
import numpy as np


# 本次设计第二部分，数据构造器部分，部分代码不太合理，想到哪里整到哪里
# 定义一些常量，这些常量不仅在本模组会用到，在其他模组也会用到


# 常量， 一些基础设置
# 浮点数精度
ACCURACY_FLOAT = 4
# 常量，基坑支护类型

# 支护结构共11种

LATERAL_EARTH_SUPPORT_STRUCTURE = np.array(['放坡开挖', '土钉墙', '水泥土重力式挡墙', '排桩', '地连墙','SMW', '钢板桩', '混凝土支撑', '钢支撑', '锚杆', '逆作法'], dtype= object) 

# 结构框架数组：（2，5）
FRAME_STRUCTURE = np.array([['支护单元', '支护类型', '支护长度/m', '基坑深度', '标识ID'], ['', '', '', '', '']],dtype= object)

# 钢筋
STEEL_CLASS = np.array(['HPB300', 'HRB335', 'HRBF335', 'HRB400', 'HRBF400', 'RRB400', 'HRB500', 'HRBF500'], dtype = object)

FRAME_STEEL = np.array([['用途', '钢筋强度', '直径/mm', '参数', '总长度/m', '总重量/kg'], ['', '', '', '', '', '']], dtype= object)


class LateralEarthSupport(object):
    """基坑支护结构类"""

    def __init__(self, project_name = '', structure_type = LATERAL_EARTH_SUPPORT_STRUCTURE[0], structure_length = 0.0, excavation_depth = 0.0):


        # 初始化默认值
        # 支护类型默认为'放坡开挖'
        # 支护长度默认为0m
        # 开挖深度默认为0m
        super.__init__()
        self._project_name = project_name
        self._structure_type = structure_type
        self._structure_length = structure_length
        self._excavation_depth = excavation_depth

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

    def create_range_struct(self):

        struct_range = FRAME_STRUCTURE.copy()
        struct_range[1,0] = self.project_name
        struct_range[1,1] = self.structure_type
        struct_range[1,2] = self.structure_length
        struct_range[1,3] = self.excavation_depth
        struct_range[1,4] = self.project_name + self.structure_type

        return struct_range

class Steel(object):

    """钢筋对象"""

    def __init__(self, steel_usage = '钢筋', strength_type = STEEL_CLASS[0], steel_diameter = 0, total_length = 0.0, total_weight = 0.0):
        
        self._steel_usage = steel_usage
        self._strength_class = strength_type
        self._steel_diameter = steel_diameter
        self._total_length = total_length
        self._total_weight = total_weight

    @property
    def steel_usage(self):
        return self._steel_usage

    @property
    def total_length(self):
        """钢筋总长度"""

        return self._total_length

    @total_length.setter
    def total_length(self, length_value):

        if not isinstance(length_value, float):
            raise TypeError("长度必须是数字")
        elif length_value <0 :
            raise ValueError('长度必须是大于零的数字')
        else:
            self._total_length = length_value
    
    @property
    def strength_type(self):
        """钢筋强度"""

        return self._strength_class
    
    @strength_type.setter
    def strength_type(self, strength_type_value):
        
        if strength_type_value  in STEEL_CLASS:
            self._strength_class = strength_type_value
        elif strength_type_value not in STEEL_CLASS:
            rasie ValueError("不属于指定类型")
    
    @property
    def steel_diameter(self):

        """钢筋直径"""
        return self._steel_diameter
    
    @steel_diameter.setter
    def steel_diameter(self, diameter_value):
        if not isinstance(diameter_value, float):

            raise TypeError("钢筋直径必须是数字")
        elif diameter_value <0:

            raise ValueError("钢筋直径必须是大于零的数字")
        elif isinstance(diameter_value, float) and diameter_value >= 0:

            self._steel_diameter = diameter_value
    
    @property
    def total_weight(self):
        
        self._total_weight = round(self.total_length * self.steel_diameter * self.steel_diameter * 0.00617, ACCURACY_FLOAT)
        
        return self._total_weight

    def create_range_steel(self):
        
        range_steel = FRAME_STEEL.copy()
        range_steel[1,0] = self._steel_usage
        range_steel[1,1] = self._strength_class
        range_steel[1,2] = self._steel_diameter
        range_steel[1,3] = self._steel_usage + self._strength_class + self._steel_diameter
        range_steel[1,4] = self._total_length
        range_steel[1,5] = self._total_weight

class SlopeRatio(LateralEarthSupport):

    """基坑支护——放坡开挖"""
    def __init__(self, slope_grade = 1, slope_shoulder = 0.0):

        LateralEarthSupport.__init__(self, project_name = '', structure_type = LATERAL_EARTH_SUPPORT_STRUCTURE[0], structure_length = 0.0, excavation_depth = 0.0)
        self._slope_grade = slope_grade
        self._slope_shoulder = slope_shoulder
    
    @property
    def slope_grade(self):

        """放坡级数"""
        return self._slope_grade
    
    @slope_grade.setter
    def slope_grade(self, slp_grade_value):

        if not isinstance(slp_grade_value, int):
            raise TypeError("坡级数必须整数")
        elif slp_grade_value <1:
            raise ValueError("坡级数至少是1")
        elif isinstance(slp_grade_value, int) and slp_grade_value >= 0:

            self._slope_grade = slp_grade_value

    @property
    def sloper_shoulder(self):

        return self._slope_shoulder
    
    @sloper_shoulder.setter
    def sloper_shoulder(self, slp_shder_value):
        
        if not isinstance(slp_shder_value, float):
            raise TypeError("坡肩长度必须是数字")
        elif slp_shder_value <0 :
            raise ValueError("坡肩长度必须是大于零的数字")
        elif isinstance(slp_shder_value, float) and slp_shder_value >= 0:
            self._slope_shoulder = slp_shder_value



def test():

    dem01 = LateralEarthSupport
    dem01.project_name = '1-1'
    dem01.structure_type = LATERAL_EARTH_SUPPORT_STRUCTURE[2]
    dem01.structure_length = 100
    dem01.excavation_depth = 6.0
    arr = dem01.create_range_struct(dem01)
    for i in arr.flat:
        print(i)


test()