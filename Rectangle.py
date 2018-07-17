from Quadrilateral import Quadrilateral
from Vector3d import Vector3d
import numpy as np
from Triangle import Triangle

class Rectangle(Quadrilateral):
    """Rectangle."""
    def __init__(self, vertex0, vertex1, vertex2):
        """Constructor."""
        vec01 = vertex1 - vertex0
        vec12 = vertex2 - vertex1
        vec20 = vertex0 - vertex2
        
        if Triangle.isconsistent(vec01, vec12, vec20) is False:
            # Given points do not form a triangle."
            raise ValueError
        
        inp0112 = vec01 ** vec12
        inp1220 = vec12 ** vec20
        inp2001 = vec20 ** vec01
        
        prod = inp0112 * inp1220 * inp2001
        
        
        if np.abs(prod) > 0.0:
            # Triangle is not a right one."
            raise ValueError
        else:
            eps = np.finfo(float).eps
            if inp0112 < eps:
                
            
                    
            
            #super(Rectangle, self).__init__(vertex0, vertex1, vertex2, vertex3)

####
if __name__ == "__main__":
    vec0 = Vector3d()
    vec1 = Vector3d(1.0, 0.0, 0.0)
    vec2 = Vector3d(1.0, 1.0, 0.0)
    vec3 = Vector3d(0.0, 1.0, 0.0)
    
    vec = Vector3d(0.0, 1.0, 0.0)
    
    rect = Rectangle(vec0, vec1, vec2, vec3)
    rect.print_self()
