#!/usr/bin/python3

import json
import smtplib
import subprocess

sender = 'hoho@gaga.com'
receivers = ['leaonow1@gmail.com']
#smtpObj = smtplib.SMTP('gmail.com', 587)
tempGitPath = "/tmp/acrgit/"

def getJson(jsonFilePath):
  with open(jsonFilePath,'r') as this_data:
    return json.load(this_data)

def compareList(listA, listB):
  return [x for x in listA + listB if x not in listA or x not in listB]

def gitClone(team, git_repo):
  this_git_path = tempGitPath + team
  this_command = "git clone --depth=1 "+git_repo+" "+this_git_path
  this_execute = subprocess.Popen(this_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
  this_execute.communicate(input=b'yes\n')[0]

def processTeam(teamDict):
  this_team = teamDict['teamName']
  this_git = teamDict['git_repo']
  gitClone(this_team, this_git)
    
if __name__ == "__main__":
  try:
    allTeamsInfo = getJson('/Users/weiyu/temp/python_process/acr_teams.json')
  except :
    print("main arc_teams.json parse error, attention required immediately")
#    try:
#      smtpObj.sendmail(sender, receivers, "acr_scopemap shit is fucked")
#    except :
#      print('Cannot even send email alert, fuck it')
    raise

  for team in allTeamsInfo['teams']:
    processTeam(team) 
  
#  print allTeamsInfo['teams']
#  mydata = getJson('/Users/weiyu/temp/python_process/scope_def.json')
#  actions = mydata['actions']
#  print actions
#  print '''#################'''
#  mydata1 = getJson('/Users/weiyu/temp/python_process/scope_def1.json')
#  actions1 = mydata1['actions']
#  print actions1
#  print '''#################'''
#  
#  print compareList(actions,actions1)
