#!/usr/bin/env python
import sys

from youtube_idea_generator_crew.crew import YoutubeIdeaGeneratorCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Define the inputs for the crew. This is a dictionary containing comments data.
    inputs = {
        "comments": '[{"video_title":"I Automated My YouTube Channel With CrewAI [Free Source Code Included]","comment":"The BEST video really inspired me a lot and I can&#39;t wait to get started using crewAI to make some interesting work","video_id":"95ab3e25-12bd-4611-b09a-4fea29846c3d","comment_id":"8013f709-93af-4a06-b14a-612c988b504f"}, ... ]'
    }
    # Create an instance of YoutubeIdeaGeneratorCrew and start the crew with the given inputs.
    YoutubeIdeaGeneratorCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    # Define the inputs for training. Here, the topic is set to "AI LLMs".
    inputs = {"topic": "AI LLMs"}
    try:
        # Train the crew with the number of iterations and filename provided via command line arguments.
        YoutubeIdeaGeneratorCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        # Catch any exceptions during training and raise a new exception with a descriptive message.
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        # Replay the crew execution starting from a specific task ID provided via command line arguments.
        YoutubeIdeaGeneratorCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        # Catch any exceptions during replay and raise a new exception with a descriptive message.
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Define the inputs for testing. Here, the topic is set to "AI LLMs".
    inputs = {"topic": "AI LLMs"}
    try:
        # Test the crew with the number of iterations and OpenAI model name provided via command line arguments.
        YoutubeIdeaGeneratorCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        # Catch any exceptions during testing and raise a new exception with a descriptive message.
        raise Exception(f"An error occurred while replaying the crew: {e}")