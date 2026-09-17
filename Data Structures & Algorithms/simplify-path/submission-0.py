"""
simplify the path
- assumptin: path is always valid
- consists of english letter, digits, period, slash or '_'

- single period repr curr directory
- double period repr previous/parent directory
- multiple consecutive slashes treated as single slash
- any sequence of periods that don't match above should be treated as a valid directory or file name

- directories with path must be seperated by exactly one slash
- path must not end with slash unless it is the root dir
- path must not have/..//"$0 any single or double points used to denote curr or parent dir

e.g.
path = "/neetcode/practice//...///../courses"
output = "/neetcode/practice/courses"

approach: 
- split by ("/")
- go in order from there

e.g. 
path = "/..//"
output = "/"

approach:
- split by ("/")
- check in order to check next valid path
- append next valid path to res

e.g. 
path = "/..//_home/a/b/..///"
output = "/_home/a"

res = []
path.split("/")

"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path_string = path.split('/')

        for string in path_string:
            if string == "" or string == ".":
                continue
            elif string == "..":
                if res:
                    res.pop()
            else:
                res.append(string)
        return "/" + "/".join(res)
