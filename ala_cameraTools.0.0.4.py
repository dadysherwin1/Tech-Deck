# ala_cameraTools.0.03.py
# This tool creates a camera based on a real lworld camera, and lets user set Arri Master Prime focal lengths.

import maya.cmds as cmds

# gets slider value
class FocalLength:
    slider = None
    def get():
        return cmds.intSliderGrp(FocalLength.slider, q=True, v=True)   
class DepthOfField:
    slider = None
    def get():
        return cmds.intSliderGrp(DepthOfField.slider, q=True, v=True)

# creates an AlexaLF camera and sets the film back. Sets the Far Clip PLane to 10,000
def createNewCamera():
    cameraName = cmds.camera(horizontalFilmAperture=1.247, verticalFilmAperture=0.702, farClipPlane=100000, focalLength=FocalLength.get(), focusDistance=DepthOfField.get())
    cmds.setAttr(cameraName[0]+".locatorScale", 20)
    cmds.setAttr(cameraName[0]+".locatorScale", 20)

# Sets the camera Aperature made by the pipeline to match an AlexaLF camera
def applyToSelected():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".horizontalFilmAperture", 1.247)
            cmds.setAttr(cam_shp[0]+".verticalFilmAperture", 0.702)
            cmds.setAttr(cam_shp[0]+".farClipPlane", 100000)
            cmds.setAttr(cam_shp[0]+".focalLength", FocalLength.get())
            cmds.setAttr(cam_shp[0]+".focusDistance", DepthOfField.get())

def applyHDSettings():
    setResolutionWidth = cmds.setAttr('defaultResolution.width', 1920)
    setResolutionHeight = cmds.setAttr('defaultResolution.height', 1080)
    setDeviceAspectRatio = cmds.setAttr('defaultResolution.deviceAspectRatio', 1.778)

def cameraTools():
    
    if cmds.window('cameraTools', exists = True):
        cmds.deleteUI('cameraTools')
        
    cmds.window('cameraTools', resizeToFitChildren=True)
    
#    cmds.window('cameraTools', widthHeight=(200, 450))

    cmds.columnLayout(adjustableColumn=True)
    
    cmds.separator(h=10,style='none')
    cmds.text('Create a new AlexaLF camera, or apply AlexaLF settings to an existing one')
    cmds.separator(h=10,style='none')
    
    FocalLength.slider = cmds.intSliderGrp(field=True, label='Focal Length', minValue=12, maxValue=150, fieldMinValue=0, fieldMaxValue=300, value=35, sliderStep=2)
    DepthOfField.slider = cmds.intSliderGrp(field=True, label='DepthOfField', minValue=12, maxValue=150, fieldMinValue=0, fieldMaxValue=300, value=35, sliderStep=2)
    
    cmds.separator(h=10,style='none')
    cmds.button(label = 'Apply to Selected', command = 'applyToSelected()')
    cmds.button(label = 'Create New Camera', command = 'createNewCamera()')
    
    cmds.separator(h=30)
    cmds.text('Sets render settings to 1920x1080')
    cmds.separator(h=10,style='none')
    cmds.button(label = 'Apply HD Settings', command = 'applyHDSettings()')
    
    cmds.showWindow('cameraTools')
    
cameraTools()
