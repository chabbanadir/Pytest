from hello import run_logic

def test_success():
    code, msg = run_logic("Success")
    assert code == 0
    assert "Success" in msg

def test_fail_env():
    code, msg = run_logic("Fail")
    assert code == 1
    assert "MY_ENV_VAR" in msg

def test_fail_arg():
    code, msg = run_logic("Success", "Fail")
    assert code == 1
    assert "Command line argument" in msg
