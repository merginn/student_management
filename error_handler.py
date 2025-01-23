class StudentError(Exception):
    pass

class FileError(StudentError):
    def __init__(self, message="Error handling file."):
        self.message = message
        super().__init__(self.message)
