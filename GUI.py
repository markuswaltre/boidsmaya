import maya.cmds as cmds
import functools
from boids import *

def createUI( pWindowTitle, pApplyCallback ):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
        
    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True )

    cmds.columnLayout(adj = True)

    cmds.separator( h=20, style='none' )
    cmds.text( label='Boids' )
    cmds.separator( h=10, style='none' )

    numberOfBoids = cmds.intSliderGrp( label = "Number of boids:", min=0, max=100, field=True)

    cmds.separator( h=20, style='none' )
    cmds.text( label='Rules' )
    cmds.separator( h=10, style='none' )

    separationScale = cmds.intSliderGrp( label = "Separation scale:", min=0, max=100, field=True)
    cohesionScale = cmds.intSliderGrp( label = "Cohesion scale:", min=0, max=100, field=True)
    alignmentScale = cmds.intSliderGrp( label = "Alignment scale:", min=0, max=100, field=True)
    
    cmds.separator( h=15, style='none' )

    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[ (1,100), (2,100) ] )
    
    cmds.button( label='Run', command=functools.partial( pApplyCallback,
                                                  numberOfBoids,
                                                  separationScale,
                                                  cohesionScale,
                                                  alignmentScale ) )
    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )
    
    cmds.button( label='Cancel', command=cancelCallback )
    
    cmds.showWindow()
 
def applyCallback( pNumberOfBoidsField, pSeparationScale, pCohesionScale, pAlignmentScale, *pArgs ):
 
    startTime = cmds.intSliderGrp( pNumberOfBoidsField, query=True, value=True )

    main(startTime)

    print 'Number of boids: %s' % ( startTime )




