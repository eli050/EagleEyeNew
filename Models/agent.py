from Models.enums import Status


class Agent:
    def __init__(self, code_name:str, real_name:str, location:str,
                 status:str = Status.ACTIVE, missions_completed:int = 0 ):
        self.code_name:str = code_name
        self.real_name:str = real_name
        self.location:str = location
        self.status:str = status.lower()
        self._valid_status()
        self.missions_completed:int = missions_completed
    def _valid_status(self):
        while not Status.__contains__(self.status):
            self.status = input("Status does not exist, please enter again:\n").lower()

    def __str__(self):
        return (f"Agent(code_name = {self.code_name}, real_name = {self.real_name},"
                f" location = {self.location}, status = {self.status}, missions_completed = {self.missions_completed})")




