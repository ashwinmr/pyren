from pyren import pyren

def test_disp_res(capfd):
    """ Test disp_res functions
    """
    ren_list = [("./foo","./bar")]
    pyren.disp_res(ren_list)

    # Read console output
    out, _ = capfd.readouterr()
    assert out == "{:30}{:30}\n".format("foo","bar")

def test_prompt_no(monkeypatch):
    """ Test that the prompt works for n
    """
    # monkeypatch the "input" function, so that it returns "n".
    monkeypatch.setattr('builtins.input', lambda x: "n")

    assert pyren.prompt() == False

def test_prompt_yes(monkeypatch):
    """ Test that the prompt works for y
    """
    # monkeypatch the "input" function, so that it returns "n".
    monkeypatch.setattr('builtins.input', lambda x: "y")

    assert pyren.prompt() == True

