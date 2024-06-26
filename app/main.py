class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = 0
        for day in range(days):
            if day % 7 == 0:
                weeks += 1

        return weeks

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineCourse":
        return cls(data["name"], data["description"],
                   cls.days_to_weeks(data["days"]))


print(OnlineCourse.days_to_weeks(2))
print(OnlineCourse.days_to_weeks(10))
print(OnlineCourse.days_to_weeks(14))
print(OnlineCourse.days_to_weeks(15))
