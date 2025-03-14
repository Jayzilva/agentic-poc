#!/usr/bin/env python
import sys
import warnings
import argparse
from datetime import datetime

from comparison_crew.crew import ComparisonCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def parse_arguments():
    """Parse command line arguments for the script."""
    parser = argparse.ArgumentParser(description='Run a skills comparison between user profile and job requirements.')
    parser.add_argument('--profile', '-p', help='User profile information (name, skills, expertise)', required=False)
    parser.add_argument('--requirements', '-r', help='Project or job requirements', required=False)
    parser.add_argument('--profile-file', '-pf', help='File containing user profile information', required=False)
    parser.add_argument('--requirements-file', '-rf', help='File containing project or job requirements', required=False)
    
    return parser.parse_args()

def get_input_content(input_text, input_file):
    """Get content from either direct input or a file."""
    if input_text:
        return input_text
    elif input_file:
        try:
            with open(input_file, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file {input_file}: {e}")
            return None
    return None

def run():
    """
    Run the crew with user profile and job requirements.
    """
    args = parse_arguments()
    
    user_profile = get_input_content(args.profile, args.profile_file)
    job_requirements = get_input_content(args.requirements, args.requirements_file)
    
    # Use sample inputs if none provided
    if not user_profile:
        user_profile = """
        Name: Alex Johnson
        Skills: Python (5 years), Data Analysis (3 years), Machine Learning (2 years), SQL (4 years)
        Education: MS in Computer Science
        Previous roles: Data Analyst (2 years), Junior Developer (3 years)
        """
    
    if not job_requirements:
        job_requirements = """
        Senior Data Scientist position
        Requirements:
        - 5+ years Python experience
        - Advanced knowledge of machine learning algorithms
        - Experience with big data technologies (Spark, Hadoop)
        - Strong SQL skills
        - PhD or MS in Computer Science, Statistics or related field
        - Experience with cloud platforms (AWS/Azure)
        """
    
    inputs = {
        'user_profile': user_profile,
        'job_requirements': job_requirements,
        'current_year': str(datetime.now().year),
        'topic': 'Career Development'
    }
    
    try:
        ComparisonCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Sample inputs for training
    inputs = {
        "user_profile": """
        Name: Taylor Smith
        Skills: JavaScript (3 years), React (2 years), HTML/CSS (4 years), Node.js (1 year)
        Education: BS in Web Development
        Previous roles: Frontend Developer (2 years)
        """,
        "job_requirements": """
        Senior Frontend Developer
        Requirements:
        - 5+ years JavaScript experience
        - 3+ years React experience
        - Experience with TypeScript
        - Knowledge of UI/UX principles
        - Experience with state management (Redux)
        """,
        "topic": "Career Development"
    }
    try:
        ComparisonCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ComparisonCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Sample inputs for testing
    inputs = {
        "user_profile": """
        Name: Jordan Lee
        Skills: Java (7 years), Spring (5 years), Docker (3 years), Kubernetes (1 year)
        Education: BS in Computer Engineering
        Previous roles: Backend Developer (4 years), DevOps Engineer (2 years)
        """,
        "job_requirements": """
        Senior Backend Developer position
        Requirements:
        - 5+ years Java experience
        - Experience with microservices architecture
        - Experience with containerization (Docker, Kubernetes)
        - Knowledge of cloud platforms
        - Experience with database design and optimization
        """,
        "topic": "Career Development"
    }
    try:
        ComparisonCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "train":
            train()
        elif sys.argv[1] == "replay":
            replay()
        elif sys.argv[1] == "test":
            test()
    else:
        run()
