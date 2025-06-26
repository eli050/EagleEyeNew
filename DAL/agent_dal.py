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


    def update_agent(self):
        pass
    def get_agent_by_code_name(self):
        pass
    def delete_agent(self):
        pass

