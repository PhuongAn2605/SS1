# Huffman Coding in python

# string = 'BCAADDDCCACACAC'

#char = ['e', 'a', 'i', 'h', 'd', 'c', 'f', 'g', 'b', 'j']
#char_freq = [0.274, 0.171, 0.149, 0.130, 0.092, 0.057, 0.052, 0.042, 0.031, 0.002]
def main():
    input_str = input('Enter a string: ')
    freq = {}
    for c in input_str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(freq)

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        #dict has key and value, key has index 0, value has index 1
        #sort key: key=lamda x : x[0]
        #sort value: key=lamda x : x[1]
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])
    # print(huffmanCode)

    print(' Char | Huffman code ')
    print('----------------------')

    for (char, frequency) in freq:
        compress_char = huffmanCode[char]
        print(' %-4r |%12s' % (char, compress_char))


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
        #print({node: binString})
    print('node',node)
    (l, r) = node.children()
    print('left',l)
    print('right',r)
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '1'))
    d.update(huffman_code_tree(r, False, binString + '0'))
    return d


# Calculating frequency
main()

