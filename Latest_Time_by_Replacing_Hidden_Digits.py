class Solution:
    def maximumTime(self, time: str) -> str:
        
        h1 = time[0]
        h2 = time[1]

        m1 = time[3]
        m2 = time[4]
        
        
        _h1 = None
        _h2 = None

        _m1 = None
        _m2 = None

        if(m1 == '?'):
            _m1 = str(5)
        
        if(m2 == '?'):
            _m2 = str(9)

        if(h1 == '?' and h2 != '?'):

            if(int(h2) <= 3):
                _h1 = str(2)
            else:
                _h1 = str(1)

        if(h2 == '?' and h1 != '?'):

            if(int(h1) <= 1):
                _h2 = str(9)

            else:
                _h2 = str(3)

        if(h1 == h2 == '?'):
            _h1 = str(2)
            _h2 = str(3)

        ans_str = ""

        if(_h1 is not None):
            ans_str += _h1
        else:
            ans_str += h1
        
        if(_h2 is not None):
            ans_str += _h2
        else:
            ans_str += h2

        ans_str += ':'

        if(_m1 is not None):
            ans_str += _m1
        else:
            ans_str += m1

        if(_m2 is not None):
            ans_str += _m2
        else:
            ans_str += m2

        return ans_str        
