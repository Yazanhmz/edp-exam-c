class Event:
    """Base class for all events."""
    def __init__(self, payload):
        self.payload = payload


class ApplicationSentEvent(Event):
    """Event triggered when an application is sent."""
    def __init__(self, payload):
        super().__init__(payload)


class ApplicationRejectedEvent(Event):
    """Event triggered when an application is rejected."""
    def __init__(self, payload):
        super().__init__(payload)


class ApplicationAcceptedEvent(Event):
    """Event triggered when an application is accepted."""
    def __init__(self, payload):
        super().__init__(payload)
