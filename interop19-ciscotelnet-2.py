import getpass
import telnetlib

def user_credentials_prompt():
    """ user credentials prompt """

    # user message
    usr_msg = "Please type in your router credentials."
    print(usr_msg)

    # user credential prompt
    HOST = input("Enter your Device IP or Hostname: ")
    user = input('User: ')
    user_pw = getpass.getpass('Login Password: ')
    enable_pw = getpass.getpass('Enable Password: ')

    # console formatting
    print('')

    return HOST, user, user_pw, enable_pw

user_data = user_credentials_prompt()

tn = telnetlib.Telnet(user_data[0])
tn.read_until(b"Username: ")
tn.write(user_data[1].encode('ascii') + b"\n")
if user_data[2]:
    tn.read_until(b"Password: ")
    tn.write(user_data[2].encode('ascii') + b"\n")

tn.write(b"enable\n")
if user_data[3]:
    tn.read_until(b"Password: ")
    tn.write(user_data[3].encode('ascii') + b"\n")

tn.write(b"conf t\n")

for n in range (654,660):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr mem\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
