from collections import deque

class CommunicationQueue:
    """Handles communication between students and universities via events."""
    def __init__(self):
        self.events = deque()

    def add_event(self, event):
        self.events.append(event)

    def process_event(self):
        if self.events:
            event = self.events.popleft()
            print(f"Processing event: {type(event).__name__} with payload: {event.payload}")
            return True
        return False
