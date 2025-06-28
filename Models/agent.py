from Models.enums import Status


class Agent:
    def __init__(self, code_name:str, real_name:str, location:str,
                 status:str = str(Status.ACTIVE), missions_completed:int = 0 ,id:int = 0):
        self.code_name:str = code_name
        self.real_name:str = real_name
        self.location:str = location
        self.status:str = Agent._valid_status(status.lower())
        self.missions_completed:int = missions_completed
        self._id = id
    @staticmethod
    def _valid_status(status:str):
        while not Status.__contains__(status):
            status = input("Status does not exist, please enter again:\n").lower()
        return status

    def __str__(self):
        return (f"Agent(id = {self._id}, code_name = {self.code_name}, real_name = {self.real_name},"
                f" location = {self.location}, status = {self.status}, missions_completed = {self.missions_completed})")





