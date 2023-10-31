import jaydebeapi

driver = "io.trino.jdbc.TrinoDriver"

# need to change the value based on the cluster information
url = "jdbc:trino://192.168.43.244:29902/hive/default?serviceDiscoveryMode=hsfabric"
user = "YourUserName"
password = "YourPassword"
tenant = "YourTenant"
jdbc_location = "Your file path of the jdbc jar"

sql = "show tables"

if __name__ == '__main__':
    conn = jaydebeapi.connect(driver, url, {"user": user,
                                            "SSL": "true",
                                            "password": password,
                                            "tenant": tenant},
                              [jdbc_location])
    curs = conn.cursor()
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    curs.close()
    conn.close()