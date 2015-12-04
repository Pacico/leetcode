import MySQLdb
con= MySQLdb.connect()
cur=con.cursor()
def exe(order):
    cur.execute(order)
    return

create_database_personaddress="""CREATE DATABASE personaddress;"""

create_person_table="""CREATE TABLE person(
personID INT,
FirstName VARCHAR(32),
LastName VARCHAR(32),
PRIMARY KEY(personID))
;
"""

crate_address_table="""CREATE TABLE address(
addressID INT,
personID INT,
City VARCHAR(32),
State VARCHAR(32),
PRIMARY KEY(addressID))
;
"""

query="""select person.FirstName, person.LastName, address.City , address.State 
from person, address
where person.personID=address.addressID
;
"""

exe(create_database_personaddress)
exe("""use personaddress;""")
exe(create_person_table)
exe(create_address_table)
exe(query)
