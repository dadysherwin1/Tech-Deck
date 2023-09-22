import os
import time
from os import listdir
from os.path import isfile, join
import re
import maya.cmds as cmds
path = 'C:/Users/24562353/Desktop/Week5/'
#cmds.AbcExport(h=True)
#cmds.AbcImport(h=True)
#cmds.ls(h=True)

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
    
    command = "-frameRange 1 120 -step 1 -wcs -root " + prop + " -file " + path + prop + "/" + prop + "_" + versionToString(getVersion(prop)+1) + ".abc"
    cmds.AbcExport(j = command)
    
def onExportSelected(*args):
    props = cmds.ls(selection=True)
    for prop in props:
        
        saveProp(prop)

def onExportAll(*args):
    # cmds.ls(assemblies=True, showType=True)
    props = cmds.ls(assemblies=True, visible=True)
    for prop in props:
        print(prop)
        cmds.select(prop)
        saveProp(prop)
        cmds.select(prop, toggle=False) 
    
def onImport(*args):
    cmds.file(f=True, new=True)
    folders = [f for f in listdir(path) if not isfile(join(path, f))]
    for prop in folders:
        command = path + prop + "/" + prop + "_" + versionToString(getVersion(prop)) + ".abc"
        print(command)
        cmds.AbcImport(command, mode="import")

cmds.window(widthHeight=(10,10), resizeToFitChildren=True)
cmds.columnLayout(columnAlign="left")

cmds.separator(h=10, style="none")

cmds.text(label="Save props to file")
cmds.separator(h=10, style="none")
cmds.rowLayout(numberOfColumns=2)
cmds.button(label="Export Selected", command=onExportSelected, width=200)
cmds.button(label="Export All", command=onExportAll, width=200)
cmds.setParent("..")

cmds.separator(h=30, style="none")

cmds.text(label="Creates a new scene with all set props")
cmds.separator(h=10, style="none")
cmds.button(label="Import", command=onImport, width=400)

cmds.showWindow()