from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.document_tools import DOCXSearchTool, PDFSearchTool
import os
import json

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class DatagatheringCrew():
	"""DatagatheringCrew for collecting and processing user information"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# Helper to validate file existence
	def _validate_file_path(self, file_path):
		if not file_path or file_path == "No resume file provided" or not isinstance(file_path, str):
			return False
		return os.path.exists(file_path)
	
	@agent
	def data_gathering_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_gathering_agent'],
			verbose=True
		)

	@agent
	def social_media_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['social_media_agent'],
			verbose=True
		)

	@agent
	def resume_parser_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_parser_agent'],
			tools=[DOCXSearchTool(), PDFSearchTool()],
			verbose=True
		)

	@agent
	def data_fine_tuner_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_fine_tuner_agent'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def user_data_collection_task(self) -> Task:
		return Task(
			config=self.tasks_config['user_data_collection_task'],
		)

	@task
	def social_media_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['social_media_analysis_task'],
		)

	@task
	def resume_parsing_task(self) -> Task:
		def resume_parsing_callback(context):
			# Validate the resume file before passing to the task
			resume_file = context.get('resume_file', "No resume file provided")
			is_valid = self._validate_file_path(resume_file)
			context['resume_file_valid'] = is_valid
			
			if not is_valid:
				print(f"\nWARNING: Resume file not found or invalid: {resume_file}")
				context['resume_file'] = "File not found or invalid: " + str(resume_file)
				
				# Create a placeholder result to prevent task failure
				try:
					# Create a placeholder file to prevent errors in downstream tasks
					with open("resume_parsing_result.json", "w") as f:
						result = {
							"status": "no_resume",
							"message": f"No valid resume file was processed: {resume_file}",
							"resume_data": {}
						}
						json.dump(result, f, indent=2)
						
					print("Created placeholder resume parsing result")
				except Exception as e:
					print(f"Warning: Could not create placeholder result: {e}")
			
			return context
		
		def resume_parsing_error_callback(context, exception):
			# This gets called if the task fails
			print(f"\nWARNING: Resume parsing task failed: {str(exception)}")
			
			# Create a placeholder result to allow the workflow to continue
			try:
				with open("resume_parsing_result.json", "w") as f:
					result = {
						"status": "error",
						"message": f"Resume parsing failed: {str(exception)}",
						"resume_data": {}
					}
					json.dump(result, f, indent=2)
					
				print("Created error placeholder for resume parsing result")
				return {"resume_data": {}, "status": "error", "message": str(exception)}
			except Exception as e:
				print(f"Warning: Could not create error placeholder: {e}")
				return {"resume_data": {}, "status": "error"}
			
		return Task(
			config=self.tasks_config['resume_parsing_task'],
			callback=resume_parsing_callback,
			error_callback=resume_parsing_error_callback,
			output_file="resume_parsing_result.json"
		)

	@task
	def data_fine_tuning_task(self) -> Task:
		def data_fine_tuning_callback(context):
			# Ensure we have all the required inputs, with fallbacks if tasks failed
			try:
				# Try to load resume parsing results if they exist
				resume_data = {}
				if os.path.exists("resume_parsing_result.json"):
					try:
						with open("resume_parsing_result.json", "r") as f:
							resume_result = json.load(f)
							resume_data = resume_result.get("resume_data", {})
					except Exception as e:
						print(f"Warning: Could not load resume parsing result: {e}")
				
				# Add resume data status to context
				context['has_resume_data'] = bool(resume_data)
				if not context.get('has_resume_data'):
					print("No resume data available. Proceeding with other data sources only.")
				
				return context
			except Exception as e:
				print(f"Warning in data fine tuning callback: {e}")
				return context
		
		return Task(
			config=self.tasks_config['data_fine_tuning_task'],
			callback=data_fine_tuning_callback,
			output_file='user_profile.json'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the DatagatheringCrew crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
