import json
import psycopg2

connection = psycopg2.connect(database="Alexandrie", host="localhost", user="postgres", password="", port="5432")
cursor = connection.cursor()
print(connection)

a = open('./auteurs.json')
auteurs = json.load(a)

u = open('./utilisateurs.json')
utilisateurs = json.load(u)

l = open('./livres.json')
livre = json.load(l)

nl = open('./notes_livres.json')
livre_note = json.load(nl)

values = [list(x.values()) for x in livre_note]
# print(values)

# get the column names
columns = [list(x.keys()) for x in livre_note][0]

# value string for the SQL string
values_str = ""

# enumerate over the records' values
for i, record in enumerate(values):

    # declare empty list for values
    val_list = []
   
    # append each value to a new list of values
    for v, val in enumerate(record):
        if type(val) == str:
            val = "'{}'".format(val.replace("'", "''"))
        val_list += [ str(val) ]

    # put parenthesis around each record string
    values_str += "(" + ', '.join( val_list ) + "),\n"

# remove the last comma and end SQL with a semicolon
values_str = values_str[:-2] + ";"
# print(values_str)
# concatenate the SQL string
table_name = "livre_note"
sql_string = "INSERT INTO %s (%s)\nVALUES\n%s" % (
    f'"{table_name}"',
    ', '.join(columns),
    values_str
)

cursor.execute(sql_string)
connection.commit()
