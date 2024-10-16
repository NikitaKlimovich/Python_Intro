import unittest
from unittest.mock import patch, mock_open
from source_code.arg_parser import ArgParserManager
from source_code.db_manager import DatabaseManager
from source_code.data_writer import DataWriter 
import json

class ArgumentParserManager(unittest.TestCase):
    @patch('sys.argv', ['program', '-r', 'json//rooms.json', '-s', 'json//students.json', '-f', 'xml'])
    def test_parse_arguments(self):
        parser = ArgParserManager()
        args = parser.get_arguments()
        self.assertEqual(args.r, 'json//rooms.json')
        self.assertEqual(args.s, 'json//students.json')
        self.assertEqual(args.f, 'xml')

    @patch('sys.argv', ['program'])
    def test_parse_arguments_no_arguments(self):
        parser = ArgParserManager()
        args = parser.get_arguments()
        self.assertIsNone(args)

    ('sys.argv', ['program', '-r', 'json//rooms.json', '-s', 'json//students.json', '-f', 'xmml'])
    def test_parse_arguments_not_valid_arguments(self):
        parser = ArgParserManager()
        is_valid = parser.validate_arguments()
        self.assertEqual(is_valid,False)



class TestDatabaseManager(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_connection(self, mock_connect):
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Nekito2001',
            'sql_folder': 'sql//'
        } 
        db_manager = DatabaseManager(config)
        mock_connect.assert_called_with(host=config['host'], user=config['user'], password=config['password'])


    def test_read_sql(self):
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Nekito2001',
            'sql_folder': 'sql//'
        } 
        db_manager = DatabaseManager(config)
        sql_queries = db_manager.read_sql('create.sql')
        self.assertIsInstance(sql_queries,list)


    @patch('mysql.connector.connect')
    def test_execute_query(self, mock_connect):
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Nekito2001',
            'sql_folder': 'sql//'
        }  
        mock_connection = mock_connect.return_value
        mock_cursor = mock_connection.cursor.return_value

        db_manager = DatabaseManager(config)
        db_manager.execute_query("SELECT * FROM student")

        mock_cursor.execute.assert_called_with("SELECT * FROM student")
        mock_connection.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_close_connection(self, mock_connect):
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Nekito2001',
            'sql_folder': 'sql//'
        } 
        mock_connection = mock_connect.return_value

        db_manager = DatabaseManager(config)
        db_manager.close_conn()

        mock_connection.close.assert_called_once()













class TestDataWriter(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_write_info(self,mock_file):
        path_to_write = 'res//json//'
        file_name = 'query1.html'
        output_format = 'json'
        data = [{'id': 1, 'name': 'Nikita'}, {'id': 2, 'name': 'Alina'} ]
        writer = DataWriter(path_to_write)
        writer.write_info(file_name,output_format, data)


        mock_file.assert_called_once_with(path_to_write+file_name, 'w', encoding = 'utf-8')
        result = json.dumps(data,indent=4)
        mock_file().write.assert_called_once_with(result)





if __name__ == '__main__':
    unittest.main()
        
