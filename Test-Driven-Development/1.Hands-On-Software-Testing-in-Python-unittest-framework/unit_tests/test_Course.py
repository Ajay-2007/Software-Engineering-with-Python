import unittest
from Ex_4_OOP_SC.Course import Course
from unittest import mock
"""
What can we unit test ?
- course information exists --> hard-coded --> Done
- Can create an object --> Done
- search student
"""
# integration test --> coupling
# dependency why not just import it? --> integration
# ======================== unit test for Course --> decoupling dependencies

class TestCourse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.course = Course()
        cls.mockedStudentObj = mock.Mock()

        # cls.studentObj = Student()

    def test_canCreateObj(self):
        # sad path test
        with self.assertRaises(TypeError):
            Course("Dummy")

    def test_InfoExists(self):
        self.assertIsNotNone(self.course.course_info)


    def test_searchStudentReturnsVal(self):
        self.mockedStudentObj.name = "Ahmed"
        student = self.course.search_student(self.mockedStudentObj)
        # breakpoint()
        self.assertIsNotNone(student)

    def test_searchStudentReturnsNone(self):
        # sand path testing
        self.mockedStudentObj.name = "dafadsf"
        student = self.course.search_student(self.mockedStudentObj)
        # breakpoint()
        self.assertIsNone(student)

    def test_calcAvgReturnsVal(self):
        self.mockedStudentObj.name = "Ahmed"
        avg = self.course.calc_avg(self.mockedStudentObj)
        self.assertIsNotNone(avg)

    def test_calcAvgReturnsNone(self):
        self.mockedStudentObj.name = "dsafsd"
        with self.assertRaises(KeyError):
            avg = self.course.calc_avg(self.mockedStudentObj)