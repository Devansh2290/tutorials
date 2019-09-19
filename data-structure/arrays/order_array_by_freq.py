from nose.tools import assert_equal
from collections import OrderedDict
import operator

def order_by_freq(arr):
    _dict = OrderedDict()
    for num in arr:
        if num not in _dict:
            _dict[num] = 1
        else:
            _dict[num] += 1
    _dict = sorted(_dict.items(), key=lambda p: p[1])
    return _dict


def frequecy_order(ls):
     r=[]
     s=[]
     ord_d = OrderedDict()
     for i in ls:
        if i not in ord_d:
            ord_d[i]=1
        else:
            ord_d[i] += 1
        r.append(i)
     rs=sorted(ord_d.items(),key=operator.itemgetter(1))
     for rec in rs:
         s.append(rec[0])
     return s


class OrderByFrequency:
    def test(self, sol):
        assert_equal(sol([1, 3, 4, 2, 5, 7, 8, 6, 2, 3, 1]), [4, 5, 7, 8, 1, 3, 2, 2, 3, 1])

obj = OrderByFrequency()
obj.test(frequecy_order)