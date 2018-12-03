import sys
import CORBA

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
helloImpl = orb.string_to_object("Hello")
helloImpl.sayHello()
helloImpl.shutdown()


