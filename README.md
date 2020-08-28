# Weather Pi
A raspberry Pi that takes periodic environmental data and publishes to a database.

## weatherpi

weatherpi is a module that handles the following

- database creation
- database read/writes
- taking sensor readings

---
note: If the path in database.py is not absolute the service will be unable to write to the database.
