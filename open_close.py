import socket
import re, time

def socket_connect(HOST, PORT, query):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("sending: ", query, "\n")
    time.sleep(0.100)
    s.send(query.encode())
    received = s.recv(4096)
    received = True
    response = ""
    while received:
        received = s.recv(4096)
        ureceived = str(received.decode("utf-8"))
        response += ureceived

    time.sleep(0.100)
    s.close()
    return response


HOST = str(input('Enter wik5 IP or for default press ENTER\nDefault 127.0.0.1  \n->'))
if HOST == '':
    HOST = '127.0.0.1'


PORT = str(input('Enter wik5 port or for default press ENTER\nDefault = 12345 \n->'))
if PORT == '':
    PORT = int(12345)

x = int(input("start login\n:"))

z = int(input("end login\n:"))

y = str(input("enter symbol\n:"))


start = str(input("Start spaming with query? Y/N \n"))

if start == "Y" or start == "y" or start == "":


    for a in range(x,z + 1):

        query1 = "action=openorder&login=" + str(a) + "&symbol=" + y + "&cmd=0&volume=2000&comment=Tristo"

        query2 = "action=getopenpositionsforlogin&login=" + str(a)



        query1_response = socket_connect(HOST, PORT, query1)

        print(query1_response)


        query2_response = socket_connect(HOST, PORT, query2)

        print(query2_response)

        regex = r"(?<=answer=)\d{0,10}|(?<=\n)\d{0,10}"

        positions_id = re.findall(regex, query2_response)
        print(positions_id)
        list_len = len(positions_id)
        print(list_len)

        for a in range(0, list_len - 1):
            query3 = "action=closeposition&position=" + str(positions_id[a])
            query3_response = socket_connect(HOST, PORT, query3)
            print(query3_response)
            time.sleep(0.150)


#        position_list = re.search(r"[^answer=]\S{0,1000};", str(query2_response[0]))
#        print(position_list)

#        print(query2_response)
