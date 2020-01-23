import json

emp_details='{"1":{"Name":"Prathap","Project":"CIGNA","Place":"HYD"}}'

data=json.loads(emp_details)

#Print the dict as a Json Object with indentation

print(json.dumps(data,indent=4))

# write data onto a physical file

filepath=open("EmpDetails.Json",'w')
json.dump(data,filepath,indent=5)
