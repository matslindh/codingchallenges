import os.path


def rs(path):
    base = os.path.dirname(__file__)
    return open(f"{base}/input/{path}").read().splitlines()
