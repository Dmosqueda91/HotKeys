import pyodbc

conn = pyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
    r"DBQ=C:\Users\MosquedaDaniel\OneDrive - Orbis Solutions, Inc\Desktop\HotKeys\ClientList.accdb;")
cursor = conn.cursor()
cursor.execute("SELECT PrimaryDomainName FROM Clients")
   
for row in cursor.fetchone():
    domains = (row)
    print(domains)

#SophosTest = 'SophosSetup.exe --customertoken="' + (v) + '"--epinstallerserver="dzr-api-amzn-us-west-2-fa88.api-upe.p.hmr.sophos.com" --products="antivirus,intercept" --quiet'
#print(SophosTest)
