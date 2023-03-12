from classes_needed import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    family = Family(2, 2, 2)
    family_2 = Family(4, 1, 3)

    activity_1 = Activity(1)
    activity_1.assign_family(family)
    activity_1.assign_family(family_2)

    activity_1.assignment_list()
