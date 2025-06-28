from pprint import pprint

from DB.my_sql_data import MySqlData
from Models.agent import Agent


class AgentDAL:
    @staticmethod
    def insert_agent(agent:Agent):
        query = f"INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, {agent.missions_completed})"
        values = (agent.code_name, agent.real_name, agent.location, agent.status)
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor() as cmd:
                    cmd.execute(query,values)
                    conn.commit()
                    print("The insertion was successful.")
            else:
                print("Failed to connect to the database, insertion failed.")

    @staticmethod
    def update_agent_by_id(agent:Agent,id:int):
        query = f"UPDATE agents SET location = %s, status = %s, missionsCompleted = {agent.missions_completed} WHERE id = {id}"
        values = (agent.location, agent.status)
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor() as cmd:
                    cmd.execute(query, values)
                    conn.commit()
                    print("The update was successful.")
            else:
                print("Failed to connect to the database, update failed.")
    @staticmethod
    def get_agent_by_id(id:int):
        query = f"SELECT * FROM agents WHERE id = {id}"
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor(dictionary=True) as cmd:
                    cmd.execute(query)
                    dict_agent = cmd.fetchall()[0]
                    return Agent(dict_agent["codeName"],dict_agent["realName"],dict_agent["location"],
                                 dict_agent["status"],dict_agent["missionsCompleted"],dict_agent["id"])
            else:
                print("Failed to connect to the database.")

    @staticmethod
    def delete_agent_by_id(id:int):
        query = f"DELETE FROM agents WHERE id = {id}"
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor() as cmd:
                    cmd.execute(query)
                    conn.commit()
                    print("The deletion was successful.")
            else:
                print("Failed to connect to the database.")

    @staticmethod
    def get_agents():
        query = "SELECT * FROM agents"
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor(dictionary=True) as cmd:
                    cmd.execute(query)
                    dict_agents = cmd.fetchall()
                    list_agents = list()
                    for agent in dict_agents:
                        list_agents.append(Agent(agent["codeName"], agent["realName"], agent["location"],
                          agent["status"], agent["missionsCompleted"], agent["id"]))
                    return list_agents

            else:
                print("Failed to connect to the database.")


    @staticmethod
    def get_agent_by_code_name(code_name:str):
        query = f"SELECT * FROM agents WHERE codeName = '{code_name}'"
        with MySqlData.get_connection() as conn:
            if conn and conn.is_connected():
                with conn.cursor(dictionary=True) as cmd:
                    cmd.execute(query)
                    dict_agents = cmd.fetchall()
                    list_agents = list()
                    for agent in dict_agents:
                        list_agents.append(str(Agent(agent["codeName"], agent["realName"], agent["location"],
                                                 agent["status"], agent["missionsCompleted"], agent["id"])))
                    return list_agents




