# ComparisonCrew Crew

Welcome to the ComparisonCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Skills Comparison Feature

This project has been enhanced with a skills comparison system that allows you to:

1. **Analyze a user's skills profile** - Extract and categorize skills, education, and experience
2. **Analyze job requirements** - Break down job requirements by importance and categories
3. **Compare profiles against requirements** - Identify skill gaps and recommend improvements

This is perfect for job seekers looking to understand how their skills match up against specific job postings, or for anyone wanting to identify areas for professional development.

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
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/comparison_crew/config/agents.yaml` to define your agents
- Modify `src/comparison_crew/config/tasks.yaml` to define your tasks
- Modify `src/comparison_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/comparison_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Basic Research Crew

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the comparison-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

### Skills Comparison

To run the skills comparison feature, use one of these methods:

#### Using the batch file (Windows):
```
comparison_crew\compare_skills.bat [user_profile_file] [job_requirements_file]
```

#### Using Python directly:
```
python -m comparison_crew.main --profile-file [user_profile_file] --requirements-file [job_requirements_file]
```

#### Example files:
The project includes example files in the `examples` directory that you can use to test the feature:
```
python -m comparison_crew.main --profile-file examples/user_profile_example.txt --requirements-file examples/job_requirements_example.txt
```

The comparison results will be saved in a `skills_gap_analysis.md` file in the project root.

## Understanding Your Crew

The comparison-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ComparisonCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
