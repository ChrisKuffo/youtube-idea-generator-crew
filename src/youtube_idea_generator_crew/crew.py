from typing import List

# Import necessary classes and decorators from the crewai library
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

# Import a custom tool for searching YouTube videos
from youtube_idea_generator_crew.tools.SearchYouTubeTool import (
    YoutubeVideoSearchAndDetailsTool,
)

# Define a data model for research items using Pydantic
class ResearchItem(BaseModel):
    title: str
    url: str
    view_count: int

# Define a data model for video ideas using Pydantic
class VideoIdea(BaseModel):
    score: int
    video_title: str
    description: str
    video_id: str
    comment_id: str
    research: List[ResearchItem]

# Define a data model for a list of video ideas using Pydantic
class VideoIdeasList(BaseModel):
    video_ideas: List[VideoIdea]

# Define the main class for the YouTube idea generator crew
@CrewBase
class YoutubeIdeaGeneratorCrew:
    """YoutubeIdeaGeneratorCrew"""

    # Define an agent for filtering comments
    @agent
    def comment_filter_agent(self) -> Agent:
        return Agent(config=self.agents_config["comment_filter_agent"], verbose=True)

    # Define an agent for generating video ideas
    @agent
    def video_idea_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["video_idea_generator_agent"], verbose=True
        )

    # Define an agent for researching video ideas
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            tools=[YoutubeVideoSearchAndDetailsTool()],  # Use the custom YouTube search tool
            verbose=True,
        )

    # Define an agent for scoring video ideas
    @agent
    def scoring_agent(self) -> Agent:
        return Agent(config=self.agents_config["scoring_agent"], verbose=True)

    # Define a task for filtering comments
    @task
    def filter_comments_task(self) -> Task:
        return Task(
            config=self.tasks_config["filter_comments_task"],
        )

    # Define a task for generating video ideas
    @task
    def generate_video_ideas_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_video_ideas_task"],
        )

    # Define a task for researching video ideas
    @task
    def research_video_ideas_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_video_ideas_task"],
        )

    # Define a task for scoring video ideas
    @task
    def score_video_ideas_task(self) -> Task:
        return Task(
            config=self.tasks_config["score_video_ideas_task"],
            output_pydantic=VideoIdeasList,  # Specify the output format using Pydantic
        )

    # Define the crew, which orchestrates the agents and tasks
    @crew
    def crew(self) -> Crew:
        """Creates the YoutubeIdeaGenerator crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Define the process as sequential
            verbose=True,
            # process=Process.hierarchical, # Optionally use a hierarchical process
        )