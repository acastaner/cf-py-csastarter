#! python3

# Author: Arnaud Castaner | arnaud.castaner@spirent.com
# First started: 2019/05/06
# License: MIT

import sys
import argparse
from pprint import pprint
import json

from config import *
from cyberfloodClient import CfClient
from cyberfloodClient.Models import Profile
from lib import csaStarterLib


def main():

    parser = argparse.ArgumentParser(description="CSA Test Starter")
    parser.add_argument('--testid', dest='testid',
                        help='The ID of the CSA test to execute')
    parser.add_argument('--profileid', dest='profileid',
                        help='The ID of the Profile to use')

    args = parser.parse_args(sys.argv[1:])

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

    attackProfileResponse = csaStarterLib.getAttackProfile(
        cfClient, args.profileid)

    csaTestResponse = csaStarterLib.getCsaTest(cfClient, args.testid)
    csaTest = json.loads(csaTestResponse)
    attackProfile = json.loads(attackProfileResponse)
    newCsaTest = csaStarterLib.modifyCsaTest(
        cfClient, csaTest, attackProfile)
    # pprint(json.dumps(newCsaTest))
    # print(newCsaTest["id"])
    response = cfClient.updateCyberSecurityAssessmentTest(
        newCsaTest, args.testid)

    #response = cfClient.startCyberSecurityAssessmentTest(args.testid)

    cfClient.invalidateToken()
    print("(Authentication has been deleted)")


if __name__ == "__main__":
    main()
