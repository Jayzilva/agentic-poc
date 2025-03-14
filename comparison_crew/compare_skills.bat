@echo off
REM Skills Comparison Batch Script
REM This script makes it easy to run the skills comparison tool

echo Running Skills Comparison Tool...

if "%~1"=="" (
    set PROFILE=examples\user_profile_example.txt
) else (
    set PROFILE=%~1
)

if "%~2"=="" (
    set REQUIREMENTS=examples\job_requirements_example.txt
) else (
    set REQUIREMENTS=%~2
)

echo User Profile: %PROFILE%
echo Job Requirements: %REQUIREMENTS%
echo -----------------------------------------

python -m comparison_crew.main --profile-file "%PROFILE%" --requirements-file "%REQUIREMENTS%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Comparison complete! Check skills_gap_analysis.md for results.
) else (
    echo.
    echo Error running comparison.
)

pause 