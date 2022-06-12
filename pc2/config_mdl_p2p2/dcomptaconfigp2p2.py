#----------------------------------------------------------
#!/usr/bin/env python3
"""
Created on Sunday September 26 18:37:33 2021
@author: alem fitwi
"""
#----------------------------------------------------------
#----------------------------------------------------------
# Relative path to configuration file, CONFIG_PATH
#---------------------------------------------------------- 
CONFIG_PATH = "config_mdl_p2p2"

#----------------------------------------------------------
# Input_output path setting,IO_PATH
#---------------------------------------------------------- 
IO_PATH = "C:\\Users\\Alem\\Desktop\\DC_OMP_TA\\MATLAB\\"
# IO_PATH = "D:\\DC_OMP_TA_Project\\" # for Windows OS
#----------------------------------------------------------
# User-defined Message Header-size, HEADER_SIZE
#----------------------------------------------------------
HEADER_SIZE = 17

#----------------------------------------------------------
# Server Port Number (p2p1.py), SERV_PORT
#----------------------------------------------------------
SERV_PORT = 55577

#----------------------------------------------------------
# IPv4 Address of p2p1, SERV_IP
#----------------------------------------------------------
SERV_IP = '128.226.80.61'

#----------------------------------------------------------
# List of IDs of the three Nodes, namely p2p1, p2p2, & p2p3
#----------------------------------------------------------
NODES_ID = ['obj_g1w1', 'obj_g2w2', 'obj_g3w3']
CUR_NODE_ID = 'obj_g2w2'
#----------------------------------------------------------
# Number of Bytes received in a single communication
#----------------------------------------------------------
# Linux OS: 
    # TCP Receive Buffer Size (Min Default Max) in Bytes
        # $ cat /proc/sys/net/ipv4/tcp_rmem
        # $ sudo sysctl net ipv4.tcp_rmem
    # TCP Send Buffer Size (Min Default Max) in Bytes
        # $ cat /proc/sys/net/ipv4/tcp_wmem
        # $ sudo sysctl net ipv4.tcp_wmem
RECV_BYTES = 1048576 #Bytes

#----------------------------------------------------------
# Step-3 & Step-7 Read-Trigger Filenames
#----------------------------------------------------------
TRIGGERS = ['step3triggerw2g2.txt','step6triggerw2f2.txt']
             #step3triggerw2g2.txt
#----------------------------------------------------------
# Object names for Step-3 & Step-6 of DC-OMP_TA
#----------------------------------------------------------
MAT_FILE_NAME3 = ["obj_g2w2", "obj_mat_all"]
MAT_FILE_NAME6 = ["obj_f2w2", "obj_mat_fs"]

#----------------------------------------------------------
# Names of Pertinent DC-OMP_TA Steps
#----------------------------------------------------------
TA_STEPS = ['step3', "step6"]

#----------------------------------------------------------
# --------------------------END---------------------------
#----------------------------------------------------------
