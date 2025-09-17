import unittest
import HtmlTestRunner

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests')  # Looks for all test_*.py in tests/

    runner = HtmlTestRunner.HTMLTestRunner(
        output='test-results',
        report_title='Unit Test Report',
        report_name='pytest-report',
        combine_reports=True
    )
    runner.run(suite)