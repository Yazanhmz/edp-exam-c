from student import Student
from university import University
from queue import CommunicationQueue

if __name__ == "__main__":

    queue = CommunicationQueue()


    student = Student("Alice")
    university = University("Tech University")

    student.send_application(university, queue)

    university.respond_to_application(queue, "accepted", student.name)

    print("\n--- Event Loop Started ---")
    while queue.process_event():
        pass
    print("--- Event Loop Ended ---")

git add .