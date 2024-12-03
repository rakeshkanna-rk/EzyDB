import os
import json
from EzyDB.query import Query
from EzyDB.logmsg import Logger

log = Logger()
log.config(add_time=True, print_able=True)

class JStorage:
    def __init__(self, dbname:str ='.db'):
        self.dbname = dbname
        self.data = {}

        if not os.path.exists(self.dbname):
            os.makedirs(self.dbname, exist_ok=True)
            log.info(f"Created {self.dbname}, as Database not exist")
    
    def save(self, table:str):
        """Save current data to the given table."""

        with open(table, 'w') as f:
            json.dump(self.data, f, indent=4)

        self.data = {}

    def load(self, table: str) -> dict:
        """Load data from the given table."""
        table = os.path.join(self.dbname, table)

        if os.path.exists(table):
            with open(table, 'r') as f:
                return json.load(f)
        
        else:
            log.warn(f"{table} does not exist, returning {{}}")
            return {}

    def usetable(self, tablename):
        """Use a common table name for all"""
        self.table = tablename
        log.info(f"Using {self.table} as default table")

    def insert(self, key, value, table:str= None):
        """Insert the value into the table with key-value pair"""

        if not table:
            table = self.table

        table = os.path.join(self.dbname, table)

        # Load existing data before adding a new key-value
        if os.path.exists(table):
            with open(table, 'r') as f:
                self.data = json.load(f)
        else:
            # Create an empty file if the table doesn't exist
            with open(table, 'w') as f:
                f.write("{}")
                log.info(f"Created {table} as it does not exist")
        
        # Add the new key-value pair and save the data
        self.data[key] = value
        self.save(table)
        self.data = {}
        log.done(f"Inserted {key} sucessfully")

    def get(self, key, table:str= None):
        """Get the value associated with a key."""
        if not table:
            table = self.table

        load = self.load(table)
        return load.get(key)
    
    def getnested(self, keyline:str, table:str= None):
        """Get a value from nested keys using a keyline like `key.subkey`"""
        if not table:
            table = self.table

        load:dict = self.load(table)
        keys = keyline.split(".")
        value: dict = load
        for key in keys:
            value = value.get(key)
            if value is None:
                return None
        
        return value

    def getall(self, table:str= None) -> dict:
        """Get all key-value pairs from the table."""
        if not table:
            table = self.table
            
        load = self.load(table)
        return load

    def delete(self, key, table:str= None ):
        """Delete a key-value pair from the table."""
        if not table:
            table = self.table
        
        load = self.load(table)  
        table = os.path.join(self.dbname, table)

        if key in load:
            del load[key]
            self.data = load
            self.save(table)
            log.done(f"{key} deleted from {table}")
        else:
            log.error(f"{key} not found in {table}")

    def drop(self, table: str = None):
        """Drop (delete) a table file."""
        if not table:
            table = self.table
            
        table = os.path.join(self.dbname, table)
        if os.path.exists(table):
            os.remove(table)
            log.done(f"{table} Droped")
        else:
            log.error("Table not found")

    def update(self, key, new_value, table: str = None):
        """Update the value associated with a key in the table."""
        if not table:
            table = self.table
        savetable = os.path.join(self.dbname, table)

        # Load existing data and check if the key exists
        self.data = self.load(table)
        if key in self.data:
            self.data[key] = new_value  # Update the value
            self.save(savetable)
            log.done("Updated Value")
        else:
            log.error(f"{key} not found in {table}")
    

    def search(self, table: str, query: Query):
        data = self.load(table)
        results = []
        for item in data.values():
            if query.matches(item):
                results.append(item)
        return results
    
    def flush(self, table:str= None):

        if not table:
            table = self.table

        table = os.path.join(self.dbname, table)
        with open(table, 'w') as f:
            f.write("{}")
            log.done(f"{table} reset to empty")

    def archive(self, table:str= None):
        if not table:
            table = self.table
        
        table_path = os.path.join(self.dbname, table)
        if not os.path.exists(table_path):
            log.error(f"Table '{table}' not found")
            exit()
        
        os.makedirs(os.path.join(self.dbname, ".archive"), exist_ok=True)
        transfer_path = os.path.join(self.dbname, ".archive", table)
        if os.path.exists(transfer_path):
            log.error(f"{table} already exist")
            exit()
        os.rename(table_path, transfer_path)
        log.done(f"{table} archived")
        
    def unarchive(self, table):
        if not table:
            table = self.table
        
        table_path = os.path.join(self.dbname, ".archive", table)

        if not os.path.exists(table_path):
            log.error(f"Table '{table}' not found")
            exit()
        
        transfer_path = os.path.join(self.dbname, table)
        if os.path.exists(transfer_path):
            log.error(f"{table} already exist")
            exit()
        
        os.rename(table_path, transfer_path)
        log.done(f"{table} unarchived")
    
