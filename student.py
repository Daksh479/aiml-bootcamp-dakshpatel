"""Provide student management and marks calculation utilities."""


def calculate_average(marks: list[int]) -> float:
    """Return the average of the given marks.

    Args:
        marks (list[int]): A list of student marks.

    Returns:
        float: The average of the marks.
            Returns 0.0 if the list is empty.
    """
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


def highest_mark(marks: list[int]) -> int | None:
    """Return the highest mark from the given list.

    Args:
        marks (list[int]): A list of student marks.

    Returns:
        Optional[int]: The highest mark, or None if the list is empty.
    """
    if not marks:
        return None

    return max(marks)


def lowest_mark(marks: list[int]) -> int | None:
    """Return the lowest mark from the given list.

    Args:
        marks (list[int]): A list of student marks.

    Returns:
        Optional[int]: The lowest mark, or None if the list is empty.
    """
    if not marks:
        return None

    return min(marks)


class Student:
    """Represent a student and manage their academic marks."""

    def __init__(self, name: str, roll_no: int, marks: list[int] | None = None) -> None:
        """Initialize a student with personal details and optional marks.

        Args:
            name (str): The student's name.
            roll_no (int): The student's roll number.
            marks (Optional[list[int]]): Initial marks. Defaults to None,
                which creates an empty marks list.

        Returns:
            None: Initializes the student object.
        """
        self.name = name
        self.roll_no = roll_no
        self.marks = list(marks) if marks is not None else []

    def add_mark(self, score: int) -> None:
        """Add a new mark to the student's marks list.

        Args:
            score (int): The mark to add.

        Returns:
            None: Updates the student's marks list.
        """
        self.marks.append(score)

    def average(self) -> float:
        """Return the average of the student's marks.

        Args:
            None.

        Returns:
            float: The average mark, or 0.0 if there are no marks.
        """
        return calculate_average(self.marks)

    def highest(self) -> int | None:
        """Return the highest mark obtained by the student.

        Args:
            None.

        Returns:
            Optional[int]: The highest mark, or None if there are no marks.
        """
        return highest_mark(self.marks)

    def lowest(self) -> int | None:
        """Return the lowest mark obtained by the student.

        Args:
            None.

        Returns:
            Optional[int]: The lowest mark, or None if there are no marks.
        """
        return lowest_mark(self.marks)

    def __str__(self) -> str:
        """Return a readable representation of the student.

        Args:
            None.

        Returns:
            str: Student name, roll number, and marks.
        """
        return (
            f"Student Name: {self.name}, "
            f"Roll No: {self.roll_no}, "
            f"Marks: {self.marks}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the student.

        Args:
            None.

        Returns:
            str: A representation that shows the student's attributes.
        """
        return (
            f"Student(name={self.name!r}, "
            f"roll_no={self.roll_no}, "
            f"marks={self.marks!r})"
        )
