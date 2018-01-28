class Subject(object):
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
    def allStudents(self):
        self.temp_students = self.students[:]
        self.temp_students.sort()
        for s in self.temp_students:
            yield s
    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'
