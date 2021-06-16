# Read a file which contains command these command will run on CLI of Linux Terminal after login
# into the command prompt of CLI
import os

f = open('resources/device_management/cmd.txt', 'r')
cmd_list = "".join([i.replace('\n', '') for i in f.readlines()])


def get_user_name_password(ip_address, port, user_name, password):
    """
    Take required details from user
    :param ip_address: Ip address given by user
    :param port: port number give by user default is 6022
    :param user_name: User name is given by user
    :param password: password give by user
    :return: for now return same command
    """
    cmd = f'gnome-terminal -- bash -c "sshpass -p {password} ssh {user_name}@{ip_address} echo Processing start; {cmd_list} echo processing end ;read line"'
    print(cmd)
    return cmd


if __name__ == '__main__':
    pwd = input("Enter Password: \n")
    ip = input("Enter Machine IP address: \n")
    user = input("Enter username: \n")
    get_user_name_password(ip, 6022, user, pwd)
