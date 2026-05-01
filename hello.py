import os
import sys

def exit_with_log(code, message=None):
    if message:
        print(message)
    print(f"\n[Process completed with exit code {code}]")
    sys.exit(code)

# Check for "fail" in environment variable
env_var = os.getenv("MY_ENV_VAR", "Value not found")
if env_var == "Fail":
    exit_with_log(1, "Error: MY_ENV_VAR is set to 'Fail'!")

# Check for "fail" in command line arguments
if len(sys.argv) > 1 and sys.argv[1] == "Fail":
    exit_with_log(1, "Error: Command line argument is set to 'Fail'!")

print(f"hello word, the env var is: {env_var}")

exit_with_log(0)

