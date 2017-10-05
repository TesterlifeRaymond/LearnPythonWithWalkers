""" pass """
import os
import time
import unittest
import BSTestRunner


CASE_PATH = os.path.abspath('case')
REPORT_PATH = 'report/report.html'


def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in all files named
    ``test_*.py`` in ./src/app/
    """
    suite = unittest.defaultTestLoader.discover(CASE_PATH, pattern='test_*.py')
    with open(REPORT_PATH, 'wb') as files:
        runner = BSTestRunner.BSTestRunner(
            files,
            title='TestReport_{0}'.format(int(time.time())),
            description=u'\Automation-TestReport'
        )
        runner.run(suite)


if __name__ == '__main__':
    try:
        unittest.main()
    except (AttributeError, TypeError):
        pass
