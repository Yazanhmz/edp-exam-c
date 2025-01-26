from event import ApplicationSentEvent


class Student:
    """Represents a student."""
    def __init__(self, name):
        self.name = name

    def send_application(self, university, queue):
        print(f"{self.name} sent an application to {university.name}.")
        queue.add_event(ApplicationSentEvent({"student": self.name, "university": university.name}))
