import json
import inspect
from pprint import pprint
from cyberfloodClient.Models import AttackProfile
from cyberfloodClient.Models import CyberSecurityAssessmentTest


def getAttackProfile(cfClient, attackProfileId):
    attackProfile = AttackProfile()
    response = cfClient.getAttackProfile(attackProfileId)
    if response.status_code == 200:
        attackProfile.id = json.loads(response.text)["id"]
        attackProfile.name = json.loads(response.text)["name"]
        attackProfile.description = json.loads(response.text)["description"]
        attackProfile.author = json.loads(response.text)["author"]
        attackProfile.scenarioTypes = json.loads(
            response.text)["scenarioTypes"]
        attackProfile.scenarios = json.loads(response.text)["scenarios"]
        attackProfile.updatedBy = json.loads(response.text)["updatedBy"]
        attackProfile.updatedAt = json.loads(response.text)["updatedAt"]
        attackProfile.createdAt = json.loads(response.text)["createdAt"]
        # DEBUG pprint(vars(attackProfile))
        # DEBUG
    else:
        print("Error fetching Attack Profile " + attackProfileId)
    # return attackProfile
    return response.text


def getCsaTest(cfClient, csaTestId):
    # csaTest = CyberSecurityAssessmentTest()
    response = cfClient.getCyberSecurityAssessmentTest(csaTestId)
    if response.status_code == 200:
        return response.text
    else:
        print("Error fetching CSA Test " + response)


def modifyCsaTest(cfClient, csaTest, attackProfile):
    # print("CSA Test:")
    # pprint(csaTest)
    updatedTest = {}
    updatedTest["name"] = csaTest["name"]
    updatedTest["projectId"] = csaTest["projectId"]
    updatedTest["description"] = csaTest["description"]
    updatedTest["config"] = csaTest["config"]
    updscenarioList = {
        'id': attackProfile["id"],
        'name': attackProfile["name"],
        'scenarioIds': [],
        'type': 'attack'}

    updscenarioIdsList = []

    for entry in attackProfile["scenarios"]:
        updscenarioIdsList.append(entry["id"])

    updscenarioList["scenarioIds"] = updscenarioIdsList
    # print(updscenarioList)
    updatedTest["config"]["scenarioProfiles"]["prevent"] = []
    updatedTest["config"]["scenarioProfiles"]["prevent"].append(
        updscenarioList)
    #print("Updated CSA Test:")
    # pprint(updatedTest)
    return updatedTest
    # pprint(updatedTest["config"]["scenarioProfiles"]["prevent"])
