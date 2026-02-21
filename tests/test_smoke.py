import importlib


def test_main_exists():
    mod = importlib.import_module("autoprun.cli")
    assert hasattr(mod, "main")
