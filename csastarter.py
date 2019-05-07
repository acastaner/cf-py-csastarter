#! python3

# Author: Arnaud Castaner | arnaud.castaner@spirent.com
# First started: 2019/05/06
# License: MIT

import sys
import argparse

from config import *
from cyberfloodClient import CfClient

def main():

    parser = argparse.ArgumentParser(description="CSA Test Starter")
    parser.add_argument('--testid', dest='testid',
                        help='The ID of the CSA test to execute')
    parser.add_argument('--testid', dest='testid',
                        help='The ID of the CSA test to execute')
    

    print("Welcome to the CyberFlood CSA Test Started!")
    print("Checking for connectivity & credentials...", end=" ")
    cfClient = CfClient(globalSettings["userName"],
                        globalSettings["userPassword"],
                        globalSettings["cfControllerAddress"]
                        )
    # Authentication
    cfClient.generateToken()
    if cfClient.isLogged():
        print("success! [" + cfClient.userName + "]")
    else:
        print("error! Please check your configuration.")
        sys.exit()

if __name__ == "__main__":
    main()
