from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

class UserType(ChoiceEnum):
    superadmin = 1
    admin = 2
    simple = 3

class GenderType(ChoiceEnum):
    Male = 1
    Female = 2
