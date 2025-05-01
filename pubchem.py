import requests
import pyodbc
from datetime import date
currentdate = date.today()
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=D:\pycodes\dbpubchem_.accdb;'
    r'PWD=your_password;'
)
cursor = conn.cursor()
SelectQuery = "SELECT * FROM tbpubchem_ WHERE (updateS = '' OR updateS IS NULL)"
cursor.execute(SelectQuery)
Getresult = cursor.fetchall()
for row in Getresult:
    cid = row.cid
    Title = row.Title
    synonyms = row.Synonyms
    
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight,InChIKey,InChI,IUPACName,Title/JSON"
    url2 = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{Title}/synonyms/JSON"
    



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
            MolecularWeight = properties[0]["MolecularWeight"]
            if MolecularWeight is not None and MolecularWeight != '':
                MolecularWeight = MolecularWeight
            InChI = properties[0]["InChI"]
            if InChI is not None and InChI != '':
                InChI = InChI
            InChIKey = properties[0]["InChIKey"]
            if InChIKey is not None and InChIKey != '':
                InChIKey = InChIKey
            IUPACName = properties[0]["IUPACName"]
            if IUPACName is not None and IUPACName != '':
                IUPACName = IUPACName
            Title = properties[0]["Title"]
            if Title is not None and Title != '':
                Title = Title

    response1 = requests.get(url2)
    properties2 = ""

    if response1.status_code == 200:
        data1 = response1.json()
        try:
            properties2 = data1['InformationList']['Information']
        except Exception as e:
            print(e)
        else:
            synonyms = properties2[0]['Synonym']
            if synonyms is not None and synonyms != '':
                synonyms = ', '.join(synonyms)
    UpdateQuery = f"update tbpubchem_ set MolecularFormula = '{MolecularFormula}', MolecularWeight = '{MolecularWeight}', InChI = '{InChI}', InChIKey = '{InChIKey}', IUPACName = '{IUPACName}', Title = '{Title}', addeddate = '{currentdate}', Synonyms = '{synonyms}', updateS = 'yes' WHERE cid = '{cid}'"
    cursor.execute(UpdateQuery)
    cursor.commit()
    print(cid)
