import maya.cmds as cmds
import functools
from boids import *

def createUI( pWindowTitle, pApplyCallback ):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
        
    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True )

    cmds.columnLayout(adj = True)

    logopath = cmds.internalVar(upd=True)+"icons/logo.jpg"

    print 'cWwight: %s' % ( logopath )

    cmds.image(w=350, h=100, image=logopath)


    cmds.separator( h=20, style='none' )
    cmds.text( label='Boids' )
    cmds.separator( h=10, style='none' )

    numberOfBoids = cmds.intSliderGrp( label = "Number of boids:", min=0, max=100, field=True, value=10)
    boidSize = cmds.floatSliderGrp( label = "Size of boids:", min=0, max=10, field=True, value=1, step=0.001)
    maxSpeed = cmds.floatSliderGrp( label = "Speed limit:", min=0, max=100, field=True, value=10, step=0.001)

    cmds.separator( h=20, style='none' )
    cmds.text( label='Animation' )
    cmds.separator( h=10, style='none' )

    numberOfFrames = cmds.intSliderGrp( label = "Number of frames:", min=1, max=10000, field=True, value=500)

    cmds.separator( h=20, style='none' )
    cmds.text( label='Rules' )
    cmds.separator( h=10, style='none' )

    cohesionRadius = cmds.floatSliderGrp( label = "Cohesion radius:", min=0, max=100, field=True, value=20, step=0.001)
    cohesionWeight = cmds.floatSliderGrp( label = "Cohesion weight:", min=0, max=10, field=True, value=1, step=0.001)
    cmds.separator( h=5, style='none' )

    separationRadius = cmds.floatSliderGrp( label = "Separation radius:", min=0, max=100, field=True, value=10, step=0.001)
    separationWeight = cmds.floatSliderGrp( label = "Separation weight:", min=0, max=10, field=True, value=1, step=0.001)
    cmds.separator( h=5, style='none' )

    alignmentRadius = cmds.floatSliderGrp( label = "Alignment radius:", min=0, max=100, field=True, value=6, step=0.001)
    alignmentWeight = cmds.floatSliderGrp( label = "Alignment weight:", min=0, max=10, field=True, value=1, step=0.001)


    cmds.separator( h=15, style='none' )

    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[ (1,100), (2,100) ] )
    
    cmds.button( label='Run', command=functools.partial( pApplyCallback,
                                                  numberOfBoids,
                                                  boidSize,
                                                  numberOfFrames,
                                                  maxSpeed,
                                                  separationWeight,
                                                  separationRadius,
                                                  cohesionWeight,
                                                  cohesionRadius,
                                                  alignmentWeight,
                                                  alignmentRadius ) )
    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )
    
    cmds.button( label='Cancel', command=cancelCallback )
    
    cmds.showWindow()
 
def applyCallback( pNumberOfBoidsField, pBoidSize, pNFrames, pMaxSpeed, pSeparationWeight, pSeparationRadius, pCohesionWeight, pCohesionRadius, pAlignmentWeight, pAlignmentRadius, *pArgs ):
 
    nBoids = cmds.intSliderGrp( pNumberOfBoidsField, query=True, value=True )
    bScale = cmds.floatSliderGrp( pBoidSize, query=True, value=True )

    nFrames = cmds.intSliderGrp( pNFrames, query=True, value=True )

    mSpeed = cmds.floatSliderGrp( pMaxSpeed, query=True, value=True )

    cWeight = cmds.floatSliderGrp( pCohesionWeight, query=True, value=True )
    cRadius = cmds.floatSliderGrp( pCohesionRadius, query=True, value=True )

    sWeight = cmds.floatSliderGrp( pSeparationWeight, query=True, value=True )
    sRadius = cmds.floatSliderGrp( pSeparationRadius, query=True, value=True )

    aWeight = cmds.floatSliderGrp( pAlignmentWeight, query=True, value=True )
    aRadius= cmds.floatSliderGrp( pAlignmentRadius, query=True, value=True )

    main(nBoids, bScale, nFrames, mSpeed, cWeight, cRadius, sWeight, sRadius, aWeight, aRadius)





