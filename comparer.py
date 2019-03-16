import lib.diff_match_patch as dmp_module

class Comparer:
    """ This is the core module for string comparison """
    def __init__(self, resolver):
        # Dependency Injection
        self.resolver = resolver
    def compare_and_resolve(self, a, b):
        diffs = self.__generateDiff(a,b)
        # convert result from list to dictionary
        result = {0 : [], 1 : [], -1 : []}
        for diff in diffs:
            result[diff[0]].append(diff[1])
        return self.resolver.resolve(result)

    def __generateDiff(self, a,b):
        dmp = dmp_module.diff_match_patch()
        diff = dmp.diff_main(a, b)
        dmp.diff_cleanupSemantic(diff)
        return diff