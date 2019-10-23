from nose.tools import assert_equal

def compress(s):
    length = len(s)
    index = 1
    count = 1
    result = ''
    if length == 0:
        return ''
    if length == 1:
        return f'{s}1'

    while index < length:
        if s[index] != s[index - 1]:
            result += f"{s[index - 1]}{count}"
            count = 1
        else:
            count += 1
        index += 1
    result += f"{s[index - 1]}{count}"

    return result


class TestCompress:
    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print("ALL TEST CASES PASSED.")


obj = TestCompress()
obj.test(compress)