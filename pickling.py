import pickle

class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": "2", "third": [1, 2, 3]}
    a_turple = (22, 23)
my_object = example_class()

my_pickled_object = pickle.dumps(my_object)
print(f"This is my pickled object:\n{my_pickled_object}\n")
                                  
my_object.a_dict = None

