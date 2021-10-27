curl localhost:9000/get -d '{"CLIENT": "opc.tcp://192.168.1.110:4840/piccolo/node/","PATH":["0:Objects", "0:PiccoloNode", "0:motor", "0:speed"]}' -H 'Content-Type: application/json'

