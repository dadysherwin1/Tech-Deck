import os
import time
from os import listdir
from os.path import isfile, join
import re
import maya.cmds as cmds
path = 'C:/Users/24562353/Desktop/Week5/'
#cmds.AbcImport(h=True)

def getVersion(prop):
    count = 0
    files = [f for f in listdir(path + prop) if isfile(join(path + prop, f))]
    for fileName in files:
        if re.search(prop + "_...\.abc" , fileName):
            count += 1
    return count
    
def versionToString(version):
    return "%03d" % (version)

def saveProp(prop):
    # make directory if needed
    if not os.path.exists(path + prop):
        os.makedirs(path + prop)
    
    command = "-file " + path + prop + "/" + prop + "_" + versionToString(getVersion(prop)+1) + ".abc"
    cmds.AbcExport(j = command)
    

def onExport(*args):
    props = cmds.ls(geometry=True)
    for prop in props:
        saveProp(prop)
    
def onImport(*args):
    folders = [f for f in listdir(path) if not isfile(join(path, f))]
    for prop in folders:
        command = '"' + path + prop + "/" + prop + "_" + versionToString(getVersion(prop)) + ".abc" + '"'
        print(command)
        cmds.AbcImport(j = command)

cmds.window(width=200)
cmds.columnLayout(adjustableColumn=True)

cmds.button(label="Export", command=onExport)
cmds.button(label="Import", command=onImport)

cmds.showWindow()