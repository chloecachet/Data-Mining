import unittest
import os
from scraper.spiders.coursespider import CourseRunParser
from util.scrapy_testutils import fake_response_from_file
from scraper.spiders.tests import __file__ as test_directory
from scraper.items import CourseItem
from scraper.spiders.page_counter import PageCounter
from scraper.spiders.coursespider import CourseSpider

def data_dir():
    return os.path.join(os.path.dirname(test_directory), 'data')

class CourseRunParserTest(unittest.TestCase):

    def setUp(self):
        self.course_run_parser = CourseRunParser(log = CourseSpider().log)
        self.course_27002_course_run_page = os.path.join(data_dir(), '27002_course_run_summer_2010.html')

    def test_parse_grade_dist_page(self):
        response = fake_response_from_file(self.course_27002_course_run_page)
        response.meta['course'] = CourseItem(course_runs = [], code = '27002')
        response.meta['counter'] = PageCounter(1, 0)
        course_item = self.course_run_parser.parse_grade_dist_page(response)
        course_run = course_item['course_runs'][0]

        self.assertEqual(u'2010', course_run['year'])
        self.assertEqual(u'Summer', course_run['semester'])
        self.assertEqual(u'74', course_run['students_registered'])
        self.assertEqual(u'61', course_run['students_attended'])
        self.assertEqual(u'45', course_run['students_passed'])
        #self.assertEqual(u'4.7', course_run['exam_average'])
        self.assertEqual(u'2', course_run['grade_12'])
        self.assertEqual(u'10', course_run['grade_10'])
        self.assertEqual(u'21', course_run['grade_7'])
        self.assertEqual(u'7', course_run['grade_4'])
        self.assertEqual(u'5', course_run['grade_02'])
        self.assertEqual(u'8', course_run['grade_00'])
        self.assertEqual(u'8', course_run['grade_minus_3'])
        self.assertEqual(u'2', course_run['sick'])
        self.assertEqual(u'11', course_run['not_shown'])