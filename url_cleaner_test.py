import unittest
import stripper


class TestStripperMethods(unittest.TestCase):
    def test_simple(self):
        url = 'http://deakin.edu.au/?utm_mkt=simple'
        expected = 'http://deakin.edu.au/'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_utm_and_mkt(self):
        url = 'http://deakin.edu.au/?utm_mkt=utttm&mkt_name=mkttttm'
        expected = 'http://deakin.edu.au/'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_mixed(self):
        url = 'http://deakin.edu.au/?utm_mkt=utmmkt&page=1'
        expected = 'http://deakin.edu.au/?page=1'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_mixed_doubles(self):
        url = 'http://deakin.edu.au/?utm_mkt=utmmkt&page=1&page=2'
        expected = 'http://deakin.edu.au/?page=1&page=2'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_query_with_special_chars(self):
        url = 'http://www.deakin.edu.au/searchpage?q=query[0]=hello&query[1]=goodbye&utm_medium=EDM'
        expected = 'http://www.deakin.edu.au/searchpage?q=query[0]=hello&query[1]=goodbye'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_find_a_course(self):
        url = 'http://www.deakin.edu.au/courses/find-a-course/results?q=&dkncoursestudent=Domestic&dkncoursequal=under_bachelor_degree&dkncourseatar=0..70&dkncourseintakes=Trimester+1&dkncourselocations=Burwood&dknpagetagia=ia-Information+Technology&dknpagetype=Course'
        expected = 'http://www.deakin.edu.au/courses/find-a-course/results?q=&dkncoursestudent=Domestic&dkncoursequal=under_bachelor_degree&dkncourseatar=0..70&dkncourseintakes=Trimester+1&dkncourselocations=Burwood&dknpagetagia=ia-Information+Technology&dknpagetype=Course'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )

    def test_courses_by_atar(self):
        url = 'http://www.deakin.edu.au/courses/courses-by-atar/?utm_source=Marketo&utm_medium=EDM&utm_campaign=generic&mkt_tok=eyJpIjoiTXpBMU5HWTRPRE5pTlRVNCIsInQiOiJ2eFdoaXBRQnZ3K0FiNFc5cUl1ZDIxUXpSMWlsRld4VVAxXC9lNzZER21ONktrb3p4WENZb21xZWYrSFdcL2NRXC92V3o2SjR3ODNhZDg2SUV6UHNYYlp0Nm5NTlJCcTlvVmxPMmtKMTAwazNwS2lXSkpkVDJtcXJuUjlDSkIwTWRzeCJ9'
        expected = 'http://www.deakin.edu.au/courses/courses-by-atar/'
        self.assertEqual(
            expected, stripper.removeBlackListedParameters(url)
        )


if __name__ == '__main__':
    unittest.main()
