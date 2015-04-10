def walktree(top):
     values = top.groups.values()
#     print values
     yield values
     for value in top.groups.values():
         for children in walktree(value):
             yield children
import Nio
f = Nio.open_file("tnested.nc") 
#print f
print "-----------------------"
print "all groups in the file:"
print "-----------------------"
print f.groups
print "--------------------------"
print "traversing the group tree:"
print "--------------------------"
rgroup = f.groups['/']
print "root group:",repr( rgroup)
print "\tgroup:",  rgroup.name, "contains", len(rgroup.groups), "groups", len(rgroup.variables), "variables,", len(rgroup.dimensions), "dimensions, and", len(rgroup.attributes), "group attributes"
for children in walktree(f.groups['/']):
    if len(children) > 0:
	print "groups:", children
    for child in children:
      print "\tgroup:",  child.name, "contains", len(child.groups), "groups", len(child.variables), "variables,", len(child.dimensions), "dimensions, and", len(child.attributes), "group attributes"
      
      #print child
#lat = f.variables['lat'][:]
#print lat
#latb = lat > 0
#print(latb)
#latsub = f.variables['lat'][(latb)]
#print latsub
