#  This code will open CLI of Linux OS
def get_user_name_password(ip_address, port, user_name, password):
    """
    Take required details from user
    :param ip_address: Ip address given by user
    :param port: port number give by user default is 6022
    :param user_name: User name is given by user
    :param password: password give by user
    :return: for now return same command
    """
    cmd = f'gnome-terminal -- bash -c "sshpass -p {password} ssh {user_name}@{ip_address}"'
    return cmd
