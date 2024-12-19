import os
from EzyDB.jsonstorage import JStorage
from EzyDB.data_type import TypeValidator as dtype
from EzyDB.cachememory import DatabaseManagement
from EzyDB.query import Query

class JsonDB:
    """
    JsonDB: A file-based JSON database for managing key-value data efficiently.
    """

    def __init__(self, dbname: str = ".db") -> None:
        """
        Initialize the database with a specified directory name.

        Args:
            dbname (str): The name of the directory for storing database files. Default is '.db'.
        """
        self.storage = JStorage(dbname=dbname)
        os.makedirs(dbname, exist_ok=True)

    def usetable(self, tablename: str):
        """
        Set the active table for subsequent operations.

        Args:
            tablename (str): The name of the table to use.
        """
        self.storage.usetable(tablename)

    def insert(self, key: str, value, table: str = None):
        """
        Insert a key-value pair into the table.

        Args:
            key (str): The key for the value being inserted.
            value: The value to be stored.
            table (str): The name of the table. Defaults to the active table.

        Raises:
            TypeError: If the key is not a string.
        """
        dtype.is_string(key)
        self.storage.insert(key, value, table)

    def get(self, key: str, table: str = None):
        """
        Retrieve the value associated with a key.

        Args:
            key (str): The key to retrieve.
            table (str): The name of the table. Defaults to the active table.

        Returns:
            The value associated with the key.

        Raises:
            TypeError: If the key is not a string.
        """
        dtype.is_string(key)
        return self.storage.get(key, table)

    def getall(self, table: str = None):
        """
        Retrieve all key-value pairs from a table.

        Args:
            table (str): The name of the table. Defaults to the active table.

        Returns:
            dict: A dictionary of all key-value pairs in the table.
        """
        return self.storage.getall(table)

    def getnested(self, keyline: str, table: str = None):
        """
        Retrieve a value from nested keys using a dot-separated keyline.

        Args:
            keyline (str): The dot-separated keys (e.g., 'key.subkey').
            table (str): The name of the table. Defaults to the active table.

        Returns:
            The value associated with the nested keys.
        """
        return self.storage.getnested(keyline, table)

    def delete(self, key: str, table: str = None):
        """
        Delete a key-value pair from the table.

        Args:
            key (str): The key to delete.
            table (str): The name of the table. Defaults to the active table.

        Raises:
            TypeError: If the key is not a string.
        """
        dtype.is_string(key)
        self.storage.delete(key, table)

    def drop(self, table: str = None):
        """
        Delete the specified table file from the database.

        Args:
            table (str): The name of the table to drop. Defaults to the active table.
        """
        self.storage.drop(table)

    def getdb(self) -> str:
        """
        Retrieve the name of the database directory.

        Returns:
            str: The name of the database directory.
        """
        return self.storage.dbname

    def update(self, key: str, new_value, table: str = None):
        """
        Update the value associated with a key.

        Args:
            key (str): The key to update.
            new_value: The new value to associate with the key.
            table (str): The name of the table. Defaults to the active table.

        Raises:
            TypeError: If the key is not a string.
        """
        dtype.is_string(key)
        self.storage.update(key, new_value, table)

    def search(self, table: str, query: Query):
        """
        Search for data in the table using a Query object.

        Args:
            table (str): The name of the table to search.
            query (Query): The query object specifying the search criteria.

        Returns:
            list: A list of matching items.
        """
        return self.storage.search(table, query)

    def flush(self, table: str = None):
        """
        Reset the specified table, removing all data.

        Args:
            table (str): The name of the table. Defaults to the active table.
        """
        self.storage.flush(table)

    def archive(self, table: str = None):
        """
        Archive the specified table for backup or storage.

        Args:
            table (str): The name of the table to archive. Defaults to the active table.
        """
        self.storage.archive(table)

    def unarchive(self, table: str = None):
        """
        Restore an archived table.

        Args:
            table (str): The name of the table to restore. Defaults to the active table.
        """
        self.storage.unarchive(table)

    def cache(self, table: str):
        """
        Load the specified table into memory for faster access.

        Args:
            table (str): The name of the table to cache.
        """
        self.cache_memory = DatabaseManagement(self.storage)
        self.cache_memory.cache_memory(table)

    def searchCache(self, table: str, query: Query):
        """
        Search for data in a cached table using a Query object.

        Args:
            table (str): The name of the table to search.
            query (Query): The query object specifying the search criteria.

        Returns:
            list: A list of matching items from the cached table.
        """
        self.cache_memory = DatabaseManagement(self.storage)
        return self.cache_memory.search_cache(table, query)
