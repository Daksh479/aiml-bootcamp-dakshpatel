"""Test student management and marks calculation functionality."""

from student import (
    Student,
    calculate_average,
    highest_mark,
    lowest_mark,
)


def test_calculate_average() -> None:
    """Test average calculation with multiple marks."""
    assert calculate_average([80, 90, 100]) == 90.0


def test_calculate_average_empty() -> None:
    """Test average calculation with an empty list."""
    assert calculate_average([]) == 0.0


def test_highest_mark() -> None:
    """Test finding the highest mark."""
    assert highest_mark([80, 95, 70]) == 95


def test_highest_mark_empty() -> None:
    """Test highest mark with an empty list."""
    assert highest_mark([]) is None


def test_lowest_mark() -> None:
    """Test finding the lowest mark."""
    assert lowest_mark([80, 95, 70]) == 70


def test_lowest_mark_empty() -> None:
    """Test lowest mark with an empty list."""
    assert lowest_mark([]) is None


def test_student_creation() -> None:
    """Test creating a student with initial marks."""
    student = Student("Rahul", 101, [85, 90])

    assert student.name == "Rahul"
    assert student.roll_no == 101
    assert student.marks == [85, 90]


def test_student_without_marks() -> None:
    """Test creating a student without initial marks."""
    student = Student("Amit", 102)

    assert student.marks == []
    assert student.average() == 0.0
    assert student.highest() is None
    assert student.lowest() is None


def test_add_mark() -> None:
    """Test adding a mark to a student's marks list."""
    student = Student("Rahul", 101)

    student.add_mark(85)
    student.add_mark(95)

    assert student.marks == [85, 95]


def test_student_average() -> None:
    """Test calculating a student's average."""
    student = Student("Priya", 102, [80, 90, 100])

    assert student.average() == 90.0


def test_student_highest() -> None:
    """Test retrieving a student's highest mark."""
    student = Student("Priya", 102, [80, 95, 70])

    assert student.highest() == 95


def test_student_lowest() -> None:
    """Test retrieving a student's lowest mark."""
    student = Student("Priya", 102, [80, 95, 70])

    assert student.lowest() == 70


def test_single_mark() -> None:
    """Test average, highest, and lowest with one mark."""
    student = Student("Rahul", 101, [85])

    assert student.average() == 85.0
    assert student.highest() == 85
    assert student.lowest() == 85


def test_str_representation() -> None:
    """Test the readable string representation of a student."""
    student = Student("Rahul", 101, [85])

    assert str(student) == ("Student Name: Rahul, Roll No: 101, Marks: [85]")


def test_repr_representation() -> None:
    """Test the developer representation of a student."""
    student = Student("Rahul", 101, [85])

    assert repr(student) == ("Student(name='Rahul', roll_no=101, marks=[85])")


def test_student_list_representation() -> None:
    """Test representation of student objects inside a list."""
    students = [
        Student("Rahul", 101, [85]),
        Student("Priya", 102, [92]),
    ]

    assert repr(students) == (
        "[Student(name='Rahul', roll_no=101, marks=[85]), "
        "Student(name='Priya', roll_no=102, marks=[92])]"
    )


def test_marks_list_is_copied() -> None:
    """Test that the original marks list is not shared."""
    marks = [85, 90]
    student = Student("Rahul", 101, marks)

    marks.append(100)

    assert student.marks == [85, 90]
