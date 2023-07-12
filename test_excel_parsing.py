import unittest
from app import excel_parser

class ExcelParsingTestCase(unittest.TestCase):
    def test_excel_parser(self):
        # Define the sample Excel data as a string
        excel_data = """
        Period    Date        Transaction             Tax  Remarks                                           Exclusive  Tax Amount  Inclusive
        Tenant    (Staff) Lindiwe Mweli    Code    2897    Main Unit No    245    Property    The Museum Tower - Middle Block (51)    General Contact    Lindiwe Mweli (Staff)    Telephone        Lease Starts    01/12/2020    Ends    31/12/2020    Vacate
        202101    01/01/2021            Balance B/f            0.00
        202102    01/02/2021            Balance B/f            0.00
        """

        # Call the parse_excel_data function to parse the data
        parsed_data = excel_parser(excel_data)

        # Perform assertions to verify the correctness of the parsed data
        self.assertEqual(len(parsed_data), 2)  # Assuming two rows of data
        self.assertEqual(parsed_data[0]['Period'], '202101')
        self.assertEqual(parsed_data[0]['Date'], '01/01/2021')
        self.assertEqual(parsed_data[0]['Transaction'], '')
        self.assertEqual(parsed_data[0]['Tax'], '')
        self.assertEqual(parsed_data[0]['Remarks'], 'Balance B/f')
        self.assertEqual(parsed_data[0]['Exclusive'], '0.00')
        self.assertEqual(parsed_data[0]['Tax Amount'], '')
        self.assertEqual(parsed_data[0]['Inclusive'], '')

        self.assertEqual(parsed_data[1]['Period'], '202102')
        self.assertEqual(parsed_data[1]['Date'], '01/02/2021')
        self.assertEqual(parsed_data[1]['Transaction'], '')
        self.assertEqual(parsed_data[1]['Tax'], '')
        self.assertEqual(parsed_data[1]['Remarks'], 'Balance B/f')
        self.assertEqual(parsed_data[1]['Exclusive'], '0.00')
        self.assertEqual(parsed_data[1]['Tax Amount'], '')
        self.assertEqual(parsed_data[1]['Inclusive'], '')

if __name__ == '__main__':
    unittest.main()
