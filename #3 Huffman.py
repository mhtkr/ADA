import time

string = 'BACAADDBDCCACCACACDCB'

class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return f'{self.left}_{self.right}'

def huffman_code_tree(node, left=True, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, bin_string + '0'))
    d.update(huffman_code_tree(r, False, bin_string + '1'))
    return d

# Calculate frequency of each character
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# Build Huffman Code Tree
start = time.time()
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = [(key, count) for (key, count) in freq]

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffman_code = huffman_code_tree(nodes[0][0])

# Display Huffman Codes
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(f' {char:<4} |{huffman_code[char]:>12}')

end = time.time()
print("Execution Time for Huffman Code:", (end - start) * 1000, "Milliseconds")
