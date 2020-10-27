class Tools:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name !r}, {self.weight})'

    tools = [
        Tools('Leveller', 3.5),
        Tools('Hammer', 3),
        Tools('Screwdriver', 2)
    ]

    # Tools.sort will not work
    print('Unsorted', repr(tools))
    tools.sort(key=lambda x:x.name)
