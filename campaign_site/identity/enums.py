from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)


class UserType(ChoiceEnum):
    admin = 1
    simple = 2


class GenderType(ChoiceEnum):
    Male = 1
    Female = 2
