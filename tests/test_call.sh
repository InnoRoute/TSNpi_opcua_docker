curl localhost:9000/call -d '{"CLIENT": "opc.tcp://192.168.1.110:4840/piccolo/node/","PATH":["0:Objects", "0:PiccoloNode",  "0:motor"],"METHOD":"0:set_speed","PARAM1":20}' -H 'Content-Type: application/json'

