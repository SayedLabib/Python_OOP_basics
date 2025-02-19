
# Private Classes and Public classes --------------------------------

#  So actually there is nothing about private or public classes
# in python but we can manually define them or, indicate them as private

class Private:
    def __init__(self,name):
        self.name = name


class Public:

    def __init__(self,name):

        self.name = name
        self.priv = Private(name)

    def _display(self):
        print (self.name)

    def display(self):
        print ('Hi !')                