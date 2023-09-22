class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}  # {class_name: []}
        self.students = {}    # {student_id: class_name}
        self.assignments = {}  # {class_name: [assignment1, assignment2, ...]}

    def add_classroom(self, class_name):
        self.classrooms[class_name] = []
        self.assignments[class_name] = []
        print(f'Classroom "{class_name}" has been created.')

    def list_classrooms(self):
        print('List of Classrooms:')
        for class_name in self.classrooms:
            print(f'- {class_name}')

    def remove_classroom(self, class_name):
        if class_name in self.classrooms:
            del self.classrooms[class_name]
            del self.assignments[class_name]
            print(f'Classroom "{class_name}" has been removed.')
        else:
            print(f'Error: Classroom "{class_name}" does not exist.')

    def add_student(self, student_id, class_name):
        if class_name not in self.classrooms:
            print(f'Error: Classroom "{class_name}" does not exist.')
            return

        self.students[student_id] = class_name
        self.classrooms[class_name].append(student_id)
        print(f'Student "{student_id}" has been enrolled in "{class_name}".')

    def list_students(self, class_name):
        if class_name in self.classrooms:
            print(f'Students enrolled in "{class_name}":')
            for student_id in self.classrooms[class_name]:
                print(f'- {student_id}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist.')

    def schedule_assignment(self, class_name, assignment_details):
        if class_name not in self.classrooms:
            print(f'Error: Classroom "{class_name}" does not exist.')
            return

        self.assignments[class_name].append(assignment_details)
        print(f'Assignment for "{class_name}" has been scheduled.')

    def list_assignments(self, class_name):
        if class_name in self.assignments:
            print(f'Assignments scheduled for "{class_name}":')
            for index, assignment_details in enumerate(self.assignments[class_name]):
                print(f'{index + 1}. {assignment_details}')
        else:
            print(f'Error: Classroom "{class_name}" does not exist or no assignments scheduled.')

    def submit_assignment(self, student_id, class_name, assignment_index):
        if student_id not in self.students or self.students[student_id] != class_name:
            print(f'Error: Student "{student_id}" is not enrolled in "{class_name}".')
            return

        if class_name not in self.assignments or assignment_index >= len(self.assignments[class_name]):
            print(f'Error: Invalid assignment index for "{class_name}".')
            return

        print(f'Assignment submitted by Student "{student_id}" in "{class_name}": {self.assignments[class_name][assignment_index]}')


# Create a VirtualClassroomManager instance
manager = VirtualClassroomManager()

# Define a function to handle user commands
def handle_user_input(command):
    parts = command.split()
    if len(parts) < 1:
        print('Invalid command. Please provide valid input.')
        return

    action = parts[0].lower()

    if action == 'add_classroom':
        if len(parts) < 2:
            print('Invalid command. Please provide valid input.')
            return
        class_name = parts[1]
        manager.add_classroom(class_name)
    elif action == 'list_classrooms':
        manager.list_classrooms()
    elif action == 'remove_classroom':
        if len(parts) < 2:
            print('Invalid command. Please provide valid input.')
            return
        class_name = parts[1]
        manager.remove_classroom(class_name)
    elif action == 'add_student':
        if len(parts) < 3:
            print('Invalid command. Please provide valid input.')
            return
        student_id = parts[1]
        class_name = parts[2]
        manager.add_student(student_id, class_name)
    elif action == 'list_students':
        if len(parts) < 2:
            print('Invalid command. Please provide valid input.')
            return
        class_name = parts[1]
        manager.list_students(class_name)
    elif action == 'schedule_assignment':
        if len(parts) < 3:
            print('Invalid command. Please provide valid input.')
            return
        class_name = parts[1]
        assignment_details = ' '.join(parts[2:])
        manager.schedule_assignment(class_name, assignment_details)
    elif action == 'list_assignments':
        if len(parts) < 2:
            print('Invalid command. Please provide valid input.')
            return
        class_name = parts[1]
        manager.list_assignments(class_name)
    elif action == 'submit_assignment':
        if len(parts) < 4:
            print('Invalid command. Please provide valid input.')
            return
        student_id = parts[1]
        class_name = parts[2]
        assignment_index = int(parts[3]) - 1
        manager.submit_assignment(student_id, class_name, assignment_index)
    else:
        print('Unknown command. Please provide valid input.')


# Run the interactive loop to accept user input
while True:
    user_input = input('Enter a command (or "exit" to quit): ')
    if user_input.lower() == 'exit':
        break
    handle_user_input(user_input)
