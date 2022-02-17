class GoodKangaroo:

    def __init__(self, name) -> None:
        
        self.name = name
        self.pouch_contents = []
    
    def __str__(self) -> str:
        return f"I'm the Kangaroo {self.name} and have the following in my pouch: \n{self.pouch_contents}."

    def put_in_pouch(self, other) -> None:
        """Adds a new item to the pouch contents.
        
        item: object to be added
        """
        self.pouch_contents.append(other)


class BadKangaroo:
    """A Kangaroo is a marsupial.
    
    
    WARNING: this class contains a NASTY bug.  I put
    it there on purpose as a debugging exercise, but
    you DO NOT want to emulate this example!
    """
    
    def __init__(self, name, contents=[]):  # The bug is this keyword argument: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
                                            # You can also see and explanation here https://github.com/AllenDowney/ThinkPython2/blob/master/code/GoodKangaroo.py
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


if __name__ == '__main__':
    
    kanga = GoodKangaroo('Kanga')
    roo = GoodKangaroo('Roo')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
