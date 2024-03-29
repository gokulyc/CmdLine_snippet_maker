from sqlalchemy import create_engine, MetaData, Table, inspect, Column, Integer, String
dbPath = 'Dal/DB.db'
db_uri = 'sqlite:///{}'.format(dbPath)
engine = create_engine(db_uri)

# census = db.Table('census', metadata, autoload=True, autoload_with=engine)
# Create MetaData instance
connection = engine.connect()
metadata = MetaData()
tblCommands = Table('Commands', metadata, autoload=True, autoload_with=engine)
# print(repr(metadata.tables['Commands']))
# print(metadata.tables)


# inspector = inspect(engine)

# # Get table information
# print(inspector.get_table_names())

# # Get column information
# print(inspector.get_columns('Commands'))

# # Get Table
# ex_table = metadata.tables['Commands']
# print(ex_table)

# DBAPI - PEP249
# create table
# engine.execute('CREATE TABLE "EX1" ('
#                'id INTEGER NOT NULL,'
#                'name VARCHAR, '
#                'PRIMARY KEY (id));')
# table = Table('Commands',metadata,autoload=True)

def InsertCmd(Name, Ctext):
    """
    Requires Name of command and Command Text
    """
    query = '''Insert into "Commands" (Name,Ctext) Values('{}','{}')'''.format(
        Name, Ctext)
    #  print(query)
    engine.execute(query)

# InsertCmd('ipconfig','ipconfig')


# select *
def get_cmd(cid=0):
    """
    Optional Cid value in int format to get the record, use 0 for all records in list type
    ex :  for _r in get_cmd(0):
             print(_r)
    """
    # print("Cid :",cid)

    if(cid == 0):
        result = engine.execute('SELECT * FROM '+'"Commands"')
    else:
        result = engine.execute(
            ('SELECT * FROM '+'"Commands" where Cid={}').format(cid))
    return result


def delete(cid):
    """
    need command id (cid) to remove the record
    ex: delete(4)
    """
    query = 'delete from Commands where Cid={}'.format(cid)
    #  print(query)
    engine.execute(query)

# for _r in get_cmd(0):
#     print(_r)
