import os
import sys

def run_logic(env_var_val, arg_val=None):
    """Core logic that we can test."""
    if env_var_val == "Fail":
        return 1, "Error: MY_ENV_VAR is set to 'Fail'!"
    if arg_val == "Fail":
        return 1, "Error: Command line argument is set to 'Fail'!"
    return 0, f"hello word, the env var is: {env_var_val}"

def exit_with_log(code, message=None):
    if message:
        print(message)
    print(f"\n[Process completed with exit code {code}]")
    sys.exit(code)

if __name__ == "__main__":
    # Standard runtime behavior
    env_var = os.getenv("MY_ENV_VAR", "Value not found")
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    
    code, msg = run_logic(env_var, arg)
    exit_with_log(code, msg)
