from pyren import pyren

def test_disp_res(capfd):
    ren_list = [("foo","bar")]
    pyren.disp_res(ren_list)
    out, _ = capfd.readouterr()
    assert out == "{:30}{:30}".format("foo","bar")