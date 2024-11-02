import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = 0
def depth(elem, level= 0):
    global maxdepth
    maxdepth = max(maxdepth, level + 1) if [depth(e, level + 1) for e in elem] else max(maxdepth, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
