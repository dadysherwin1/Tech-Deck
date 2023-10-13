# configs
path = 'C:/Users/24562353/Desktop/Week8/'

import maya.cmds as cmds
sequenceName = ""
shotName = ""

def getTextFields():
    sequenceName = cmds.textField("sequence", q=True, text=True)
    shotName = cmds.textField("shot", q=True, text=True)

def exportSequenceLighting(buttonInfo):
    getTextFields()
    cmds.file(path + sequenceName + "/sequence_lighting.mb", force=True, typ="mayaBinary", exportSelected=True)
    
def exportShotLighting(buttonInfo):
    getTextFields()
    cmds.file(path + sequenceName + "/" + shotName + ".mb", force=True, typ="mayaBinary", exportSelected=True)

cmds.window(widthHeight=(10,10), resizeToFitChildren=True)
cmds.columnLayout(columnAlign="left")

# sequence and shot text fields
cmds.separator(h=10, style="none")
cmds.rowLayout(numberOfColumns=2)
cmds.text(label="Sequence name: ", width=200)
cmds.textField("sequence",width=200)
cmds.setParent("..")
cmds.rowLayout(numberOfColumns=2)
cmds.text(label="Shot name (if applicable): ", width=200)
cmds.textField("shot",width=200)

# export 
cmds.setParent("..")
cmds.separator(h=30, style="none")
cmds.text(label="Export selected lights")
cmds.separator(h=10, style="none")
cmds.rowLayout(numberOfColumns=2)
cmds.button(label="Export as Sequence", command=exportSequenceLighting, width=200)
cmds.button(label="Export as Shot", command=exportShotLighting, width=200)

cmds.showWindow()