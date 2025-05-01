import requests
import pyodbc
from datetime import date

currentdate = date.today()



conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=D:\pycodes\dbpubchem.mdb;'
    r'PWD=your_password;'
    )

cursor = conn.cursor()


SelectQuery = "select * from tblpubchem where (updateS = '' or updateS is null)"

cursor.execute(SelectQuery)

Getresult = cursor.fetchall()

for row in Getresult:
    cid = row.cid
    MolecularFormula = row.MolecularFormula
    
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight,InChIKey,InChI,IUPACName/JSON"
    
        
    response = requests.get(url)
    properties = ""
        
    if response.status_code == 200:
        data = response.json()
        try:
                properties = data['PropertyTable']['Properties']
        except Exception as e:
                print(e)
        else:
                MolecularFormula = properties[0]["MolecularFormula"]
                if MolecularFormula is not None and MolecularFormula != '':
                    MolecularFormula = MolecularFormula
                



        UpdateQuery = (f"update tblpubchem set MolecularFormula = '{MolecularFormula}',addeddate = '{currentdate}',updateS = 'yes' where cid = '{cid}'")
        #print(UpdateQuery) 
        cursor.execute(UpdateQuery)
        cursor.commit()

        print("*"*20,cid,"*"*20)











        