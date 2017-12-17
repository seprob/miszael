# Miszael

## Synopsis

Use this software if you want to delete all documents from all databases in MongoDB except data in "admin" database.

## Usage

You should use Python 2 to run this application.

```
python miszael.py -u user -p password -db database -a address
```
where:
- "user" (optional) is a database user name,
- "password" is a database password,
- "database" is a authentication database,
- "address" (optional) is a database host address.