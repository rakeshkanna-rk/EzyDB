import os
from EzyDB.jsonstorage import JStorage
from EzyDB.data_type import TypeValidator as dtype
from EzyDB.cachememory import DatabaseManagement
from EzyDB.query import Query

class JsonDB:
    
    def __init__(self, dbname:str = ".db") -> None:
        self.storage = JStorage(dbname=dbname)
        
        os.makedirs(dbname, exist_ok=True)

    def usetable(self, tablename):
        """Use a common table"""
        self.storage.usetable(tablename)

    def insert(self, key, value, table:str = None):
        """Insert the value into the table with key-value pair"""
        dtype.is_string(key)
        self.storage.insert(key, value, table)

    def get(self, key, table:str= None):
        """Get the value associated with a key."""
        dtype.is_string(key)
        return self.storage.get(key, table)

    def getall(self, table:str= None):
        """Get a value from nested keys using a keyline like `key.subkey`"""
        return self.storage.getall(table)
    
    def getnested(self, keyline:str, table:str= None):
        """Get all key-value pairs from the table."""
        return self.storage.getnested(keyline, table)
    
    def delete(self, key, table:str= None ):
        """Delete a key-value pair from the table."""
        dtype.is_string(key)
        self.storage.delete(key, table)
    
    def drop(self, table: str = None):
        """Drop (delete) a table file."""
        self.storage.drop(table)

    def getdb(self):
        return self.storage.dbname
    
    def update(self, key, new_value, table: str = None):
        """Update the value associated with a key in the table."""
        dtype.is_string(key)
        self.storage.update(key, new_value, table)

    def search(self, table: str, query: Query):
        """Search in the tables with Query class"""
        return self.storage.search(table, query)

    def flush(self, table:str= None):
        """Reset any table"""
        self.storage.flush(table)

    def archive(self, table:str= None):
        """Archive tables"""
        self.storage.archive(table)

    def unarchive(self, table:str= None):
        """Unarchive tables"""
        self.storage.unarchive(table)

    def cache(self, table):
        """Cache A table from Database"""
        self.cache_memory = DatabaseManagement(self.storage)
        self.cache_memory.cache_memory(table)
    
    def searchCache(self, table: str, query: Query):
        """Search inside Cache faster"""
        self.cache_memory = DatabaseManagement(self.storage)
        return self.cache_memory.search_cache(table, query)

