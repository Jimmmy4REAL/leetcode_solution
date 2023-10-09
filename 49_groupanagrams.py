import collections
# dictionary {[eelm]:[mlee,elme],} -> dictionary.values()

class Solution:
    def groupAnagrams(strs):
        # input strs 
        # output >> [[strs]]
        record = collections.defaultdict(list)
        for str in strs:
            origin = str
            modified = ''.join(sorted(str))
            record[modified].append(origin)
        return record.values()
    
strs = ['elem','eelm','leem','mm','mml','lml']
print(Solution.groupAnagrams(strs))