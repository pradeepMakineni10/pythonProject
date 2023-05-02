import mysql.connector




def data_connection():
    mycon = mysql.connector.connect(host="Makinenis-Mac-mini.local", user="root", passwd="Trine10101992", auth_plugin='mysql_native_password', database = "mysql")
    print(mycon)
    csr = mycon.cursor()
    #query = """Create table employee (name varchar(200), sal int(20))"""
    #query = """Show tables"""
    # query  = """insert into employee (name, sal) values (%s, %s)"""
    # employees = [("rani", 100000), ("ranga", 150000), ("ajith", 120000)]
    # csr.executemany(query, employees)

    csr.execute()
    mycon.commit()





    return


