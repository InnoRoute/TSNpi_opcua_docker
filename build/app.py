import sys
sys.path.insert(0, "..")
import time
import os
from rt_hat import SIGGEN as RT_HAT_SIGGEN

from opcua import ua, Server

motor_speed=0

def set_speed(parent,new_speed):
	global motor_speed
	motor_speed=new_speed.Value
	print("Set new motor speed: "+str(motor_speed))
	root.get_child(["0:Objects", "0:PiccoloNode", "0:motor", "0:speed"]).set_value(motor_speed)
	RT_HAT_SIGGEN.set(0.5,int(motor_speed)*1000,0,0)
#	os.popen("docker-compose "+name+" start")
	return ""

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/piccolo/node/")
#    server.set_endpoint("http://0.0.0.0:4840/freeopcua/server/")
    
    server.import_xml("data2.xml");
		
    uri = "http://opcfoundation.org/UA/SecurityPolicy#None"
    idx = server.register_namespace(uri)

    objects = server.get_objects_node()
    root = server.get_root_node()
    server.link_method(root.get_child(["0:Objects", "0:PiccoloNode", "0:motor", "0:set_speed"]),set_speed)
    server.start()
    RT_HAT_SIGGEN.init("/hat_env.sh")
    
    try:
        count = 0
        while True:
           time.sleep(1)
#           root.get_child(["0:Objects", "0:PiccoloNode", "0:resources_available", "0:memory"]).set_value(int(os.popen("cat /proc/meminfo | grep MemFree | sed -e 's/[[:space:]]\+/ /g' | cut -d ' ' -f2").read()))

    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
