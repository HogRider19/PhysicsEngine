from functools import wraps
import random
import time


def operations_per_second(inner_fun):
    
    @wraps(inner_fun)
    def dec_fun():

        first_time = time.time()
        result = []

        while time.time() - first_time < 1:
            result.append(inner_fun(ValueGenerator(-30, 30)))

        return round(len(result)/1000)

    return dec_fun


class ValueGenerator:

    def __init__(self, border1: float, border2: float) -> None:
        self.border1 = border1
        self.border2 = border2

    def __call__(self):
        return random.random() * (self.border2 - self.border1) + self.border1


class ReportManager:

    def __init__(self) -> None:
        self.tests = []

    def register(self, *tests: any) -> None:
        self.tests = tests

    def get_report(self) -> str:
        report = '\n'
        for test in self.tests:
            report += f'{test.__name__}: {test()}\n'
        
        return report







