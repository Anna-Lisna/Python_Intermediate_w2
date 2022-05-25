class ReverseIter:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.start = len(self.list) - 1
        return self

    def __next__(self):
        if self.start >= 0:
            element = self.list[self.start]
            self.start -= 1
            return element
        else:
            raise StopIteration


my_list = [1, 2, 3, 4, 5]
iteration = ReverseIter(my_list)

for i in iteration:
    print(i)


