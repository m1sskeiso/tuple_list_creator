class TupleListCreator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def create_tuples(self):
        return [(self.list1[i], self.list2[i]) for i in range(min(len(self.list1), len(self.list2)))]

# Sample usage
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

tuple_creator = TupleListCreator(list1, list2)
result = tuple_creator.create_tuples()

print(result)  # Output: [(1, "mark"), (2, "alice"), (3, "john")]
