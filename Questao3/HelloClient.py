import sys
from ansys_corba import CORBA

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
print(orb)
'''''
helloImpl = orb.string_to_object("Hello")
helloImpl.sayHello()
helloImpl.shutdown()
'''
