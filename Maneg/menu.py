from pprint import pprint

from DAL.agent_dal import AgentDAL
from Models.agent import Agent


class Menu:
    @staticmethod
    def start():
        to_exit = False
        while not to_exit:
            choose = Menu._print_menu()
            match choose:
                case "1":
                    pprint(AgentDAL.get_agents())
                case "2":
                    print("Enter a code name: ")
                    code_name = Menu._valid_str_input()
                    print("Enter a real name: ")
                    real_name = Menu._valid_str_input()
                    print("Enter a location: ")
                    location = Menu._valid_str_input()
                    AgentDAL.insert_agent(Agent(code_name,real_name,location))


                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    to_exit = True
                case _:
                    pass

    @staticmethod
    def _print_menu():
        return input("Welcome to the Agents menu, please select an option:\n"
                    "1. Print all agents\n"
                    "2. Insert agent\n"
                    "3. Print agent by ID\n"
                    "4. Delete agent by ID\n"
                    "5. Print agent by code name\n"
                    "6. Exit\n")
    @staticmethod
    def _valid_int_input():
        num = input()
        while not num.isdigit():
            num = input(f"The character {num} is invalid (not a number). Please enter it again.")
        return num
    @staticmethod
    def _valid_str_input():
        string = input()
        while len(string) < 1:
            string = input(f"The character {string} is invalid (Its length is less than one). Please enter it again.")
        return string

Menu.start()