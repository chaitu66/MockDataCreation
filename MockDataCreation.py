table_name='dummy7'
s=spark.table(table_name).dtypes
k=[]
insert_stmt="insert into {} values (".format(table_name)
print(insert_stmt)
for i in range(len(s)):
  if(s[i][1]) == 'string':
    j="'"+s[i][0]+'_1234'+"'"
    k.append(j)
    #print(k)
  elif(s[i][1]) == 'timestamp':
    j="'2021-03-18 00:17:13'"
    k.append(j)
    #print(k)
  elif(s[i][1]) in 'int':
    j= 1234
    k.append(j)
    #print(k)
  elif 'decimal' in (s[i][1]):
    j= 12.34
    k.append(j)
  elif 'boolean' in (s[i][1]):
    j= 'false'
    k.append(j)
    #print(k)
for i in range(len(k)):
  #print(type(i))
  if (i!=len(k)-1):
    print(str(k[i])+",")
    #print(i)
    #print("not reached end of pgm")
  else:
    print(str(k[i])+")")
