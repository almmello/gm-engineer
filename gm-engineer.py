# gm-engineer.py
from dotenv import load_dotenv
import os
import subprocess
import sys

# Load .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Set the API key as an environment variable for the current process
os.environ['OPENAI_API_KEY'] = api_key

# Check for correct command line arguments
if len(sys.argv) < 2:
    print("Usage: python3 gm-engineer.py [--feedback] projects/project_name")
    sys.exit(1)

# Get feedback flag and project name from command line arguments
use_feedback = False
project_name = sys.argv[-1]

if "--feedback" in sys.argv:
    use_feedback = True

# Call gpt-engineer with the subprocess module
if use_feedback:
    subprocess.run(["gpt-engineer", "--steps", "use_feedback", project_name])
else:
    subprocess.run(["gpt-engineer", project_name])
