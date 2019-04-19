import re
func_name="library"
fields="book_id, book_name, edition, quantity"
primary_keys="book_id"
fields=re.split(",| ", fields)
fields2=list()
for i in fields:
	if i:
		fields2.append(i)
fields=fields2
# print(fields)
primary_keys=re.split(",| ", primary_keys)
primary_keys2=list()
for i in primary_keys:
	if i:
		primary_keys2.append(i)
primary_keys=primary_keys2

f=open("./templates/{}.py".format(func_name), "w+")


string='''@app.route('/{}')
def {}():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM {}')
    return render_template('{}.html', results=results)'''.format(func_name,func_name,func_name,func_name)
f.write(string)
f.write("\n")
f.write("\n")

string='''@app.route('/{}_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def {}_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':'''.format(func_name, func_name)
string+="\n"
f.write(string)

string=""
for i in fields:
	string+= "\t\t" + i + " = request.form['" + i + "']\n" 

string+= "\t\tquery = 'INSERT INTO " + func_name + " VALUES ("
for i in range(len(fields)):
	# string+=fields[i]
	if i == len(fields)-1:
		string+="{})'.format("
		break;
	else:
		string+='{},'

for i in range(len(fields)):
	string+=fields[i]
	if i == len(fields)-1:
		string+=")\n"
		break
	else:
		string+=','

string+="\t\tsql_insert_edit_delete(query)\n"
string+="\tresults = sql_query('SELECT * FROM {}')\n".format(func_name)
string+="\treturn render_template('{}.html', results=results)".format(func_name)
f.write(string)
f.write("\n")
f.write("\n")

string=""
string+='''@app.route('/{}_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def {}_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':\n'''.format(func_name,func_name)

for i in range(len(primary_keys)):
	string+="\t\t"+primary_keys[i]+" = request.args.get('" + primary_keys[i] + "')\n"

string+="\t\tquery='DELETE FROM "+ func_name + " WHERE "
for i in range(len(primary_keys)):
	string+=primary_keys[i]
	string+="="
	if i == len(primary_keys)-1:
		string+="{}'.format("
		break;
	else:
		string+= "{} AND "

for i in range(len(primary_keys)):
	string+=primary_keys[i]
	if i == len(primary_keys)-1:
		string+=")\n"
		break;
	else:
		string+= ","

string+="\t\tsql_insert_edit_delete(query)\n"
string+="\tresults = sql_query('SELECT * FROM {}')\n".format(func_name)
string+="\treturn render_template('{}.html', results=results)".format(func_name)
f.write(string)
f.write("\n")
f.write("\n")


string=""
string='''@app.route('/{}_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def {}_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':\n'''.format(func_name, func_name)

for i in range(len(primary_keys)):
	string+="\t\t"+primary_keys[i]+" = request.args.get('" + primary_keys[i] + "')\n"

string+="\t\teresults = sql_query('SELECT * FROM "+ func_name + " WHERE "
for i in range(len(primary_keys)):
	string+=primary_keys[i]
	string+="="
	if i == len(primary_keys)-1:
		string+="{}'.format("
		break;
	else:
		string+= "{} AND "

for i in range(len(primary_keys)):
	string+=primary_keys[i]
	if i == len(primary_keys)-1:
		string+="))\n"
		break;
	else:
		string+= ","

string+='\tresults = sql_query("SELECT * FROM {}")\n'.format(func_name)
string+="\treturn render_template('{}.html', eresults=eresults, results=results)".format(func_name)
f.write(string)
f.write("\n")
f.write("\n")

string=""

string='''@app.route('/{}_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def {}_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':\n'''.format(func_name, func_name)

for i in range(len(primary_keys)):
	string+="\t\told_"+primary_keys[i]+" = request.form['old_" + primary_keys[i] + "']\n"

for i in range(len(fields)):
	string+="\t\t"+fields[i]+" = request.form['" + fields[i] + "']\n"

string+="\t\teresults = sql_query('SELECT * FROM "+ func_name + " WHERE "
for i in range(len(primary_keys)):
	string+=primary_keys[i]
	string+="="
	if i == len(primary_keys)-1:
		string+="{}'.format("
		break;
	else:
		string+= "{} AND "

for i in range(len(primary_keys)):
	string+=primary_keys[i]
	if i == len(primary_keys)-1:
		string+="))\n"
		break;
	else:
		string+= ","

string+="\t\tquery = 'UPDATE {} set ".format(func_name)+" "
for i in range(len(fields)):
	string+=fields[i]+ " = {}"
	if i != len(fields)-1:
		string+=','

string+=" WHERE "
for i in range(len(primary_keys)):
	string+=(primary_keys[i] + " = {}")
	if i == len(primary_keys)-1:
		string+="'.format("
		break;
	else:
		string+= " AND "

for i in range(len(fields)):
	string+=fields[i]
	string+=','

for i in range(len(primary_keys)):
	string+="old_" + primary_keys[i]
	if i == len(primary_keys)-1:
		string+=")\n"
		break;
	else:
		string+= ","

string+="\t\tsql_insert_edit_delete(query)\n"
string+="\tresults = sql_query('SELECT * FROM {}')\n".format(func_name)
string+="\treturn render_template('{}.html', results=results)".format(func_name)
f.write(string)
f.write("\n")
f.write("\n")


f=open("./templates/{}.html".format(func_name), "w+")

string=""
string="""{% extends "layout.html" %}

{% block content1 %}
{% if '""" + func_name+"""_edit1' in request.url %}
<div style='margin-left: 100px; width: 45%;'>
  <div class="alert alert-info" role="alert">
   <strong>Your turn!</strong> Edit your selected data line here ...
 </div>

 {% for eresult in eresults %}\n"""

string+="<form action = \"" + func_name + "_edit2\" method = \"POST\">\n"

for i in range(len(fields)):
	string+="\t<p>" + fields[i] + "<input class=\"form-control\" type = \"text\" name = \"" + fields[i] + "\" style='width: 100%;' value='{{eresult[\"" + fields[i] + "\"]}}' /></p>\n"

for i in range(len(primary_keys)):
	string+="\t<p>" + "<input type = \"hidden\" name = \"" + "old_" + primary_keys[i] + "\" value='{{eresult[\"" + primary_keys[i] + "\"]}}' /></p>\n"

string+='''{% endfor %}

   <br>

   <p><input class="btn-primary" type = "submit" value = "Update Data" /></p>
 </form>
</div>

{% else %}
<div style='margin-left: 100px; width: 45%;'>
  <div class="alert alert-info" role="alert">
    <strong>Your turn!</strong> Insert your new data line with this form ...
  </div>

  <form action = "''' + func_name +"_insert\" method = \"POST\">\n"

f.write(string)
string=""
for i in range(len(fields)):
	string+="\t<p>" + fields[i] + ": <input class=\"form-control\" type = \"text\" name = \"" + fields[i] + "\" style='width: 100%;'/></p>\n"

string+='''\t<p><input class=\"btn-primary\" type = \"submit\" value = \"Insert Data\" /></p>
</form>
</div>


{% endif %}
{% endblock content1 %}

{% block content2 %}

<table class = 'table table-hover' style = 'margin-left: 100px; margin-right: 100px; width: 90%;'>
 <thead>
  <tr>\n'''

for i in range(len(fields)):
	string+="\t<th>" + fields[i] + "</th>\n"
	
string+='''</tr>
</thead>

{% for result in results %}
<tr>\n'''

f.write(string)
string=""
for i in range(len(fields)):
	string+="<td>{{result[\"" + fields[i] +"\"]}}</td>\"\n"

string2=""
for i in range(len(primary_keys)):
	if i ==len(primary_keys)-1:
		string2+="{}=result['{}'])".format(primary_keys[i],primary_keys[i]) 
	else:
		string2+="{}=result['{}'], ".format(primary_keys[i],primary_keys[i])

string+="<td align=\"center\"><a href = \"{{ url_for('" + func_name + "_edit1', " + string2 + """}}"><i class="fas fa-edit"></a></td>
   <td align="center"><a href = "{{ url_for('""" + func_name+ "_delete', " + string2 + """}}"><i class="fas fa-trash-alt"></a></td>
   </tr>
   {% endfor %}
 </table>
 {% endblock content2 %}"""
f.write(string)



f.close()
