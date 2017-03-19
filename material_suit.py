from visual import *
checkerboard = ( (1,0,1,0), 
                 (0,1,0,1),
                 (1,0,1,0),
                 (0,1,0,1))
tex = materials.texture(data=checkerboard,
                     mapping="rectangular",interpolate=false)
box(axis=(0,0,1), color=color.cyan, material=tex)
