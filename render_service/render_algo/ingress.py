from node import Node
import json
import sys

# Takes as input: key (a string) and lw-graph (Can load with Node.parse)

# Returns: Render tree as json string
def simple_render(graph, key):
    return json.dumps(Node.parse(graph).render(key))

def render(graph, *keys):
    root = Node.parse(graph)
    for key in keys:
        yield json.dumps(root.render(key))

if __name__ == "__main__":
    print(simple_render(sys.argv[2], sys.argv[1]))
    sys.stdout.flush()
