# **EzyDB**  
EzyDB is a lightweight, file-based NoSQL database system designed for Python developers.
  
> [!WARNING]  
> This tool is in **BETA** / **DEVELOPMENT** stage. Please use latest version.   
  
## **Installation**
```bash
pip install EzyDB
```

# JsonDB Class Documentation

The `JsonDB` class provides an interface to interact with a file-based JSON database. It allows inserting, updating, retrieving, and querying data in a structured and efficient manner.

---

## **Methods**

**`__init__(dbname: str = ".db")`**
**Description**:  
Initializes the database with the specified directory name.

**Parameters**:  
- `dbname` (*str*, optional): The name of the directory where the database files will be stored. Default is `.db`.

**Returns**:  
None

---

**`usetable(tablename)`**
**Description**:  
Sets the active table for subsequent database operations.

**Parameters**:  
- `tablename` (*str*): The name of the table to use.

**Returns**:  
None

---

**`insert(key, value, table: str = None)`**
**Description**:  
Inserts a key-value pair into the specified table.

**Parameters**:  
- `key` (*str*): The key for the value being inserted.  
- `value` (*any*): The value to insert.  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
None

**Raises**:  
- `TypeError`: If `key` is not a string.

---

**`get(key, table: str = None)`**
**Description**:  
Retrieves the value associated with a key.

**Parameters**:  
- `key` (*str*): The key to search for.  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
- The value associated with the key.

**Raises**:  
- `TypeError`: If `key` is not a string.

---

**`getall(table: str = None)`**
**Description**:  
Retrieves all key-value pairs from the specified table.

**Parameters**:  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
- A dictionary containing all key-value pairs from the table.

---

**`getnested(keyline: str, table: str = None)`**
**Description**:  
Retrieves a value from a nested key structure using a dot-separated keyline.

**Parameters**:  
- `keyline` (*str*): A dot-separated string indicating the nested keys (e.g., `key.subkey`).  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
- The value associated with the nested keys.

---

**`delete(key, table: str = None)`**
**Description**:  
Deletes a key-value pair from the specified table.

**Parameters**:  
- `key` (*str*): The key to delete.  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
None

**Raises**:  
- `TypeError`: If `key` is not a string.

---

**`drop(table: str = None)`**
**Description**:  
Deletes the specified table file from the database.

**Parameters**:  
- `table` (*str*, optional): The name of the table to drop. If not specified, the currently active table is dropped.

**Returns**:  
None

---

**`getdb()`**
**Description**:  
Retrieves the name of the database directory.

**Returns**:  
- The name of the database directory as a string.

---

**`update(key, new_value, table: str = None)`**
**Description**:  
Updates the value associated with a key in the specified table.

**Parameters**:  
- `key` (*str*): The key to update.  
- `new_value` (*any*): The new value to assign to the key.  
- `table` (*str*, optional): The name of the table. If not specified, the currently active table is used.

**Returns**:  
None

**Raises**:  
- `TypeError`: If `key` is not a string.

---

**`search(table: str, query: Query)`**
**Description**:  
Searches for data in the specified table using a `Query` object.

**Parameters**:  
- `table` (*str*): The name of the table to search.  
- `query` (*Query*): The query object specifying the search criteria.

**Returns**:  
- A list of matching items.

---

**`flush(table: str = None)`**
**Description**:  
Resets the specified table, removing all its data.

**Parameters**:  
- `table` (*str*, optional): The name of the table to reset. If not specified, the currently active table is reset.

**Returns**:  
None

---

**`archive(table: str = None)`**
**Description**:  
Archives the specified table for backup or storage purposes.

**Parameters**:  
- `table` (*str*, optional): The name of the table to archive. If not specified, the currently active table is archived.

**Returns**:  
None

---

**`unarchive(table: str = None)`**
**Description**:  
Restores an archived table.

**Parameters**:  
- `table` (*str*, optional): The name of the archived table to restore. If not specified, the currently active table is restored.

**Returns**:  
None

---

**`cache(table)`**
**Description**:  
Loads the specified table into memory for faster access.

**Parameters**:  
- `table` (*str*): The name of the table to cache.

**Returns**:  
None

---

**`searchCache(table: str, query: Query)`**
**Description**:  
Searches for data in a cached table using a `Query` object for faster performance.

**Parameters**:  
- `table` (*str*): The name of the table to search.  
- `query` (*Query*): The query object specifying the search criteria.

**Returns**:  
- A list of matching items from the cached table.

--- 

## **Example Usage**
```python
from EzyDB.jsonstorage import JsonDB
from EzyDB.query import Query

# Initialize database
db = JsonDB()

# Insert data
db.insert("001", {"name": "Alice", "age": 25}, table="users.json")

# Query data
query = Query().key("age") > 20
results = db.search("users.json", query)
print(results)
```

## **Contributing**
We welcome contributions! Feel free to fork the repository, submit issues, or create pull requests to help us improve. Let's build something amazing together! 🚀 
[Open a Fork](https://github.com/EzyCode-org/EzyDB/fork)
[Open an Issue](https://github.com/EzyCode-org/EzyDB/issues)  
[Open a Pull Request](https://github.com/EzyCode-org/EzyDB/pulls)

## **Package Detials**
**Name** : EzyDB  
**Version** : 1.0.1  
**Author** : Rakesh Kanna  
**Mail** : [**rakeshkanna0108@gmail.com**](mailto:rakeshkanna0108@gmail.com)  
**GitHub** : **https://github.com/EzyDB-org/EzyDB/**  
**PyPI** : **https://pypi.org/project/EzyDB/**  