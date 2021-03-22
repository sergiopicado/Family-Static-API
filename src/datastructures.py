
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id": self._generateId(), "Name": "John Jackson", "Age": 33,
             "Lucky Numbers": [7, 13, 22]},
            {"id": self._generateId(), "Name": "Jane Jackson", "Age": 33,
             "Lucky Numbers": [10, 14, 3]},
            {"id": self._generateId(), "Name": "Jimmy Jackson",
             "Age": 5, "Lucky Numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_memberDataStr(self, member):
        member["id"] = self._generateId()
        print(member)
        self._members.append(member)

    def delete_memberDataStr(self, id):
        self._members.pop(member)

    def get_member(self, id):
        json_text = jsonify(self._members)
        return json_text

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
