from heapq import heappush, heappop


class Node:
    def __init__(self, ch, frequency, left, right):
        self.ch = ch
        self.frequency = frequency
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
    

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding( text ):

    # get frequency of elements

    frequencies = { c: text.count(c) for c in text}

    # create list of Nodes N
    nodes = []
    for k,v in frequencies.items():
        node = Node(k, v, left=None, right=None)
        heappush(nodes, node)
    # pop lowest 2 frequency. Sum and create a new node. push it to the list N

    while len(nodes) != 1: # so we can pop 2 at the same time. 

        left = heappop(nodes)
        right = heappop(nodes)

        total = left.frequency + right.frequency
        node = Node("", total, left, right)
        heappush(nodes, node) 


    # the last element in the nodes is the root
    root = nodes[0]


    # create a schema
    encoding_schema = create_encode_schema( root)

    # encode 

    encoded_text = "".join([ encoding_schema[c] for c in text ])

    print( "encoded text is:", encoded_text)

    # decode

    decoded_text = decoding(encoded_text, root)

    print("decoded text is:", decoded_text)

    print("original text is:", text)

    assert decoded_text == text

    print("encoding schema is:",encoding_schema)


def create_encode_schema( root):
    
    nodes = [ ( root, "")]
    encoding = {}

    while nodes:
        node, character = nodes.pop()

        if node.is_leaf():
            encoding[node.ch] = character        
        else:
            if node.left:  nodes.append( (node.left, character + "0"))
            if node.right: nodes.append( (node.right, character + "1"))

    return encoding



def decoding( code, root):
    result = ""
    cursor = root 
    for c in code:
        if c == "0":
            cursor = cursor.left
        else:
            cursor = cursor.right
        if cursor.is_leaf():
            result += cursor.ch
            cursor = root
    return result     



def test():

    text = "aaaabbbccd"
    huffman_encoding(text)

test()