from functools import wraps
from progress.bar import ChargingBar
import random
import time
import datetime


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

    def __call__(self, br1=None, br2=None):
        if br1 is None or br2 is None: 
            border1, border2 = self.border1, self.border2
        else:
            border1, border2 = br1, br2
        return random.random() * (border2 - border1) + border1


class ReportManager:

    def __init__(self, logger=None) -> None:
        self.tests = []
        self._logger = logger

    def register(self, *tests: any) -> None:
        self.tests = tests

    def show_report(self) -> None:
        report = []
        bar = ChargingBar('Modeling', max=len(self.tests))
        for test in self.tests:
            report.append([test(), test.__name__.replace('_test', '')])
            bar.next()

        bar.finish()

        report.sort(reverse=True)

        if self._logger is not None:
            self._logger.info('\ndate: %s\n', datetime.datetime.now())

        report_str = '\n'
        for data in report:
            report_str += f'{data[1]}{"."*(65-len(data[1]))}{data[0]}\n'
            if self._logger is not None:
                self._logger.info(f'{data[1]}{"."*(65-len(data[1]))}{data[0]}')
            
        if self._logger is None:
            print(report_str)







