from event import ApplicationAcceptedEvent, ApplicationRejectedEvent


class University:
    """Represents a university."""
    def __init__(self, name):
        self.name = name

    def respond_to_application(self, queue, response, student_name):
        if response == "accepted":
            print(f"{self.name} accepted the application of {student_name}.")
            queue.add_event(ApplicationAcceptedEvent({"student": student_name, "university": self.name}))
        elif response == "rejected":
            print(f"{self.name} rejected the application of {student_name}.")
            queue.add_event(ApplicationRejectedEvent({"student": student_name, "university": self.name}))
