import pandas as pd
import os

class DataLoader:
    """
    A class for loading data from various sources including CSV, JSON, Excel, and SQL databases.
    """

    def __init__(self, default_encoding='utf-8', default_sep=','):
        """
        Initialize the DataLoader with default settings.

        Args:
            default_encoding (str): The default encoding to use when reading files.
            default_sep (str): The default separator to use for CSV files.
        """
        self.default_encoding = default_encoding
        self.default_sep = default_sep

    def load_csv(self, file_path, **kwargs):
        """
        Load data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            **kwargs: Additional keyword arguments to pass to pandas.read_csv().

        Returns:
            pandas.DataFrame: The loaded data as a DataFrame.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            Exception: If there's an error while loading the CSV file.
        """
        kwargs.setdefault('encoding', self.default_encoding)
        kwargs.setdefault('sep', self.default_sep)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")
        try:
            df = pd.read_csv(file_path, **kwargs)
            return df
        except Exception as e:
            raise Exception(f"Error loading CSV file: {str(e)}")

    def load_json(self, file_path, **kwargs):
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.
            **kwargs: Additional keyword arguments to pass to pandas.read_json().

        Returns:
            pandas.DataFrame: The loaded data as a DataFrame.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            Exception: If there's an error while loading the JSON file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")
        try:
            df = pd.read_json(file_path, **kwargs)
            return df
        except Exception as e:
            raise Exception(f"Error loading JSON file: {str(e)}")
    
    def load_excel(self, file_path, **kwargs):
        """
        Load data from an Excel file.

        Args:
            file_path (str): The path to the Excel file.
            **kwargs: Additional keyword arguments to pass to pandas.read_excel().

        Returns:
            pandas.DataFrame: The loaded data as a DataFrame.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            Exception: If there's an error while loading the Excel file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")
        try:
            df = pd.read_excel(file_path, **kwargs)
            return df
        except Exception as e:
            raise Exception(f"Error loading Excel file: {str(e)}")
    
    def load_sql(self, query, connection, **kwargs):
        """
        Load data from a SQL database.

        Args:
            query (str): The SQL query to execute.
            connection: A database connection object.
            **kwargs: Additional keyword arguments to pass to pandas.read_sql().

        Returns:
            pandas.DataFrame: The loaded data as a DataFrame.

        Raises:
            Exception: If there's an error while executing the SQL query.
        """
        try:
            df = pd.read_sql(query, connection, **kwargs)
            return df
        except Exception as e:
            raise Exception(f"Error loading SQL: {str(e)}")
    
    def load_data(self, file_path, **kwargs):
        """
        Load data from various file formats based on the file extension.

        Args:
            file_path (str): The path to the file to load.
            **kwargs: Additional keyword arguments to pass to the specific load method.

        Returns:
            pandas.DataFrame: The loaded data as a DataFrame.

        Raises:
            ValueError: If the file format is not supported.
            FileNotFoundError: If the specified file does not exist.
            Exception: If there's an error while loading the file.
        """
        _, extension = os.path.splitext(file_path)
        if extension == ".csv":
            return self.load_csv(file_path, **kwargs)
        elif extension == ".json":
            return self.load_json(file_path, **kwargs)
        elif extension in [".xls", ".xlsx"]:
            return self.load_excel(file_path, **kwargs)
        else:
            raise ValueError(f"Unsupported file format: {extension}")