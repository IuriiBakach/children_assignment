import math


class Family:
    def __init__(self, family_id, num_child, num_adult):
        self.family_id = family_id
        self.num_child = num_child
        self.num_adult = num_adult

    def __str__(self):
        return "Family number {} has {} children and {} adults".format(self.family_id,
                                                                       self.num_child,
                                                                       self.num_adult)


class Activity:
    """
    Add more stuff if such a need arises
    """

    def __init__(self, activity_id, start_time, end_time, capacity_used=0, family_assigned=None, capacity_left=math.inf,
                 location='default'):
        if family_assigned is None:
            family_assigned = []
        self.family_assigned = family_assigned
        self.activity_id = activity_id
        self.capacity_used = capacity_used
        self.capacity_left = capacity_left
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def gen_info(self):
        """
        Just a basic output view -> to be updated later
        :return:
            string: info about the Activity
        """
        return "Activity number {} has {} capacity used and {} capacity left".format(self.activity_id,
                                                                                     self.capacity_used,
                                                                                     self.capacity_left)

    def assign_family(self, family):
        self.family_assigned.append(family)
        # also update used and left capacity

    def assignment_list(self):
        for element in self.family_assigned:
            print(element.family_id)
