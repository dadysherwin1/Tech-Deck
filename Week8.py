# configs
path = 'C:/Users/24562353/Desktop/Week8/'

import maya.cmds as cmds
sequenceName = ""
shotName = ""

def exportSequenceLighting():
    cmds.file(path + sequence + "/sequence_lighting.mb", force=True, typ="mayaBinary", exportSelected=True)
    
def exportSequenceLighting():
    cmds.file(path + sequence + "/" + shotName + "/" + ".mb", force=True, typ="mayaBinary", exportSelected=True)


cmds.window(widthHeight=(10,10), resizeToFitChildren=True)
cmds.columnLayout(columnAlign="left")

# sequence and shot text fields
cmds.separator(h=10, style="none")
cmds.rowLayout(numberOfColumns=2)
cmds.text(label="Sequence name (if applicable): ", width=200)
sequenceName = cmds.textField(width=200)
cmds.setParent("..")
cmds.rowLayout(numberOfColumns=2)
cmds.text(label="Shot name (if applicable): ", width=200)
shotName = cmds.textField(width=200)

# export 
cmds.separator(h=30, style="none")
cmds.text(label="Export selected lights")
cmds.separator(h=10, style="none")
cmds.rowLayout(numberOfColumns=2)
cmds.button(label="Export as Sequence", command=exportSequenceLighting, width=200)
cmds.button(label="Export as Shot", command=exportShotLighting, width=200)

cmds.showWindow()