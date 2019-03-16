import sys
sys.path.append('../')
from comparer import Comparer

class TestComparer():
    def test(self):
        first = "This is an Apple.\nThat is a Banana."
        second = "No.\nThis is a Banana.\nTHAT is an Apple."
        class resolver():
            def resolve(self, diffs):
                return diffs
        diffs = Comparer(resolver()).compare_and_resolve(first, second)
        assert (len(diffs[-1]) == 1 and diffs[-1][0] == "n Apple.\nThat is a Banana") and \
               (len(diffs[1]) == 2 and "No.\n" in diffs[1] and " Banana.\nTHAT is an Apple" in diffs[1])


if __name__ == "__main__":
    TestComparer().test()