# crew/crew_runner.py

from crewai import Crew
from crew.agent_content_adaptor import create_content_agent
from crew.tasks import create_tasks

def create_crew():
    agent = create_content_agent()
    tasks = create_tasks(agent)

    crew = Crew(
        agents=[agent],
        tasks=tasks,
        verbose=True
    )

    return crew
