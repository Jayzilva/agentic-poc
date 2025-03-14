# User Data Gathering Crew

Welcome to the User Data Gathering Crew project, powered by [crewAI](https://crewai.com). This project is designed to help you collect, organize, and analyze user information from various sources including direct input, social media profiles, and resume documents.

## Overview

This crew consists of four specialized AI agents that work together to create a comprehensive user profile:

1. **Data Gathering Agent** - Collects basic user information such as name, education, institute, and a brief description.
2. **Social Media Agent** - Analyzes LinkedIn and X.com (Twitter) profiles to extract professional details and interests.
3. **Resume Parser Agent** - Extracts information from resume documents (PDF or DOCX) stored in the data folder.
4. **Data Fine-Tuning Agent** - Combines all gathered information, removes duplications, and creates a comprehensive user profile.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuration

**Add your `OPENAI_API_KEY` into the `.env` file**

## Preparing Your Data

1. Place your resume file (PDF or DOCX format) in the `data/` folder at the root of the project.
2. Have your LinkedIn and X.com (Twitter) profile URLs ready.

## Running the Project

To start the data gathering process, run this command from the root folder of your project:

```bash
$ crewai run
```

This command will:
1. Prompt you for basic user information (name, education, etc.)
2. Ask for your social media profile URLs
3. Display available resume files in the data folder for you to select
4. Process all the information through the AI agents
5. Generate a comprehensive user profile saved as `user_profile.json`

## Understanding the Workflow

1. The **Data Gathering Agent** collects your basic information.
2. The **Social Media Agent** analyzes your LinkedIn and X.com profiles to extract professional details and interests.
3. The **Resume Parser Agent** uses specialized tools to extract information from your resume document.
4. The **Data Fine-Tuning Agent** combines all the gathered information, removes duplications, and creates a comprehensive profile.

## Customizing

- Modify `src/datagathering_crew/config/agents.yaml` to adjust agent behaviors and capabilities
- Modify `src/datagathering_crew/config/tasks.yaml` to change task objectives or outputs
- Modify `src/datagathering_crew/crew.py` to add your own logic, tools, or specific arguments
- Modify `src/datagathering_crew/main.py` to customize user input collection

## Support

For support, questions, or feedback regarding this project or crewAI:
- Visit the [crewAI documentation](https://docs.crewai.com)
- Reach out through the [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join the crewAI Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with the crewAI docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
