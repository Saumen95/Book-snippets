class Tool:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('Leveller', 3.5),
    Tool('Hammer', 2.5),
    Tool('Screwdriver', 1)
]

print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nsorted: ', tools)

tools.sort(key=lambda x: x.weight)
print('\nBy weight', tools)

