#!/usr/bin/env python
"""
Skills Comparison Script - A simple wrapper for running the ComparisonCrew.

This script makes it easier to run the skills comparison between a user profile
and job requirements without having to remember the full command.
"""

import subprocess
import sys
import os

def main():
    # Get the absolute path of the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Default examples
    default_profile = os.path.join(script_dir, "examples", "user_profile_example.txt")
    default_requirements = os.path.join(script_dir, "examples", "job_requirements_example.txt")
    
    # Parse command line arguments
    profile_path = default_profile
    requirements_path = default_requirements
    
    # Simple argument parsing
    if len(sys.argv) >= 2:
        profile_path = sys.argv[1]
    if len(sys.argv) >= 3:
        requirements_path = sys.argv[2]
    
    # Print information
    print("Running Skills Comparison")
    print(f"User Profile: {profile_path}")
    print(f"Job Requirements: {requirements_path}")
    print("-------------------------------------------")
    
    # Build the command to run
    cmd = [
        "python", "-m", "comparison_crew.main",
        "--profile-file", profile_path,
        "--requirements-file", requirements_path
    ]
    
    # Run the command
    try:
        subprocess.run(cmd, check=True)
        print("\nComparison complete! Check skills_gap_analysis.md for results.")
    except subprocess.CalledProcessError as e:
        print(f"\nError running comparison: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 