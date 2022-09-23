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

    def __call__(self, br1 = None, br2 = None):
        if br1 is None or br2 is None: 
            border1, border2 = self.border1, self.border2
        else:
            border1, border2 = br1, br2
        return random.random() * (border2 - border1) + border1


class ReportManager:

    def __init__(self) -> None:
        self.tests = []

    def register(self, *tests: any) -> None:
        self.tests = tests

    def get_report(self) -> str:
        report = []
        for test in self.tests:
            report.append([test(), test.__name__])

        report.sort(reverse=True)

        report_str = '\n'
        for data in report:
            report_str += f'{data[1]}{"."*(60-len(data[1]))}{data[0]}\n'

        return report_str







