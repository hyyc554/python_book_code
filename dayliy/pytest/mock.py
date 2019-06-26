from unittest.mock import MagicMock, patch

m = MagicMock()
# mock test 函数，返回值 1
m.test = MagicMock(return_value=1)
# 调用 test 函数
m.test()
# 输出：1
class MyObj(object):
    value = 'old_value'

my = MyObj()
with patch.object(my, 'value', 'new_value'):
    print(my.value)