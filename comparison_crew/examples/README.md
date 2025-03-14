# Example Data Files for ComparisonCrew

This directory contains example data files that can be used with the ComparisonCrew skill comparison system.

## Available Examples

1. **User Profile Example** (`user_profile_example.txt`)
   - A sample user profile detailing skills, education, and experience
   - Use this as a template for creating your own profile

2. **Job Requirements Example** (`job_requirements_example.txt`)
   - A sample job posting with detailed requirements and qualifications
   - Use this as a template for job requirements you want to compare against

## How to Use

You can use these example files with the ComparisonCrew by running:

```bash
python -m comparison_crew.main --profile-file examples/user_profile_example.txt --requirements-file examples/job_requirements_example.txt
```

Or you can use them as references to format your own input data.

## Creating Your Own Files

When creating your own profile or requirements files, follow these guidelines:

### User Profile
- Include name, education, skills with experience level
- List technical and soft skills
- Include work experience and relevant projects
- Be specific about years of experience with technologies

### Job Requirements
- Include job title and company information
- Clearly separate required vs. preferred qualifications
- Be specific about years of experience needed
- Include both technical requirements and soft skills

## Output

The system will generate a `skills_gap_analysis.md` file in the project root directory with the analysis results. 