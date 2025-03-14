#!/usr/bin/env python
import sys
import warnings
import os
import glob
import json

from datetime import datetime

from datagathering_crew.crew import DatagatheringCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_user_input():
    """
    Get user inputs for the data gathering crew.
    """
    print("Welcome to the Data Gathering Crew!")
    print("Please provide the following information:")
    
    name = input("Full Name: ").strip()
    education = input("Education (e.g., BS Computer Science): ").strip()
    institute = input("Institute: ").strip()
    description = input("Brief Professional Description: ").strip()
    linkedin_url = input("LinkedIn Profile URL: ").strip()
    twitter_url = input("X.com (Twitter) Profile URL: ").strip()
    
    # Resume file handling - automatic detection
    resume_file = None
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data')
    
    # Make sure data directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        print(f"\nCreated data directory at: {data_dir}")
        print("Place your resume files there if you want them to be processed.")
    
    # Look for PDF files first, then DOCX files
    pdf_files = glob.glob(os.path.join(data_dir, '*.pdf'))
    docx_files = glob.glob(os.path.join(data_dir, '*.docx'))
    
    # Automatically select the first PDF file if available
    if pdf_files:
        resume_file = pdf_files[0]
        print(f"\nFound PDF resume: {os.path.basename(resume_file)}")
    # Otherwise, try to use the first DOCX file
    elif docx_files:
        resume_file = docx_files[0]
        print(f"\nFound DOCX resume: {os.path.basename(resume_file)}")
    else:
        print("\nNo resume files found in the data directory.")
        print(f"Place your resume (PDF or DOCX) in the '{data_dir}' folder if you want it to be processed.")
    
    # Create inputs dictionary
    inputs = {
        'name': name,
        'education': education,
        'institute': institute,
        'description': description,
        'linkedin_url': linkedin_url,
        'twitter_url': twitter_url,
        'resume_file': resume_file if resume_file else "No resume file provided"
    }
    
    # Validate inputs
    print("\nInput summary:")
    for key, value in inputs.items():
        print(f"{key}: {value}")
    
    print("\nProceeding with these inputs. If anything is incorrect, please restart the application.")
    
    return inputs

def run():
    """
    Run the crew.
    """
    inputs = get_user_input()
    
    # Save inputs for reference
    try:
        with open("user_inputs.json", "w") as f:
            json.dump(inputs, f, indent=2)
        print("Input data saved to user_inputs.json for reference")
    except Exception as e:
        print(f"Warning: Could not save input data for reference: {e}")
    
    print("\nStarting data processing with CrewAI agents...")
    try:
        result = DatagatheringCrew().crew().kickoff(inputs=inputs)
        print("\nProcess completed successfully!")
        print("Your user profile has been saved as 'user_profile.json'")
        return result
    except Exception as e:
        error_msg = f"An error occurred while running the crew: {e}"
        print(f"ERROR: {error_msg}")
        raise Exception(error_msg)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = get_user_input()
    try:
        DatagatheringCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DatagatheringCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = get_user_input()
    try:
        DatagatheringCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
