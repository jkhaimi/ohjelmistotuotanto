*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jesse  boshh123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  jh  boshh123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  jkh!  boshh123
    Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
    Input Credentials  jkhaimi  bosh
    Output Should Contain  Password is too short
    

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jkhaimi  boshbosh
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123