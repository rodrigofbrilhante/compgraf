from PIL import Image
import numpy as np

picture=Image.open("picture.jpg")
scene=Image.open("scene.jpg")
#picture=Image.open("picture2.jpg")
#scene=Image.open("scene2.jpeg")

(x,y)=picture.size
(z,w)=scene.size

#Pontos de picture
p=[(0,0,1),(x,0,1),(0,y,1),(x,y,1)]

#Pontos de destino da picture
q=[(1619,59,1),(1886,176,1),(1640,677,1),(1913,725,1)]
#q=[(462,49,1),(901,128,1),(449,846,1),(869,762,1)]

# A.t = B 

A = np.array([
				 [ p[0][0] , p[0][1] , p[0][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ],
				 [    0    ,    0    ,    0    , p[0][0] , p[0][1] , p[0][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ],
				 [    0    ,    0    ,    0    ,    0    ,    0    ,    0    , p[0][0] , p[0][1] , p[0][2] ,    0    ,    0    ,    0    ],
				 [ p[1][0] , p[1][1] , p[1][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,-q[1][0] ,    0    ,    0    ],
				 [    0    ,    0    ,    0    , p[1][0] , p[1][1] , p[1][2] ,    0    ,    0    ,    0    ,-q[1][1] ,    0    ,    0    ],
				 [    0    ,    0    ,    0    ,    0    ,    0    ,    0    , p[1][0] , p[1][1] , p[1][2] ,-q[1][2] ,    0    ,    0    ],
				 [ p[2][0] , p[2][1] , p[2][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,-q[2][0] ,    0    ],
				 [    0    ,    0    ,    0    , p[2][0] , p[2][1] , p[2][2] ,    0    ,    0    ,    0    ,    0    ,-q[2][1] ,    0    ],
				 [    0    ,    0    ,    0    ,    0    ,    0    ,    0    , p[2][0] , p[2][1] , p[2][2] ,    0    ,-q[2][2] ,    0    ],
				 [ p[3][0] , p[3][1] , p[3][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,    0    ,-q[3][0] ],
				 [    0    ,    0    ,    0    , p[3][0] , p[3][1] , p[3][2] ,    0    ,    0    ,    0    ,    0    ,    0    ,-q[3][1] ],
				 [    0    ,    0    ,    0    ,    0    ,    0    ,    0    , p[3][0] , p[3][1] , p[3][2] ,    0    ,    0    ,-q[3][2] ],
				 ])
B = np.array([0 for x in range(12)])
for i in range(0,3):
	B[i] = q[0][i]

# A.t = B ----> t = inv(A).B
t = np.linalg.inv(A).dot(B)
H = np.array([[t[3*j+i] for i in range(3)] for j in range(3)])
#Calculo da Inversa
Hinv = np.linalg.inv(H)

#Troca dos pixels em scene
for a in range(z):
    for b in range(w):
        v = (a,b,1)
		
#Calculo do produto Hinv*v
        i = Hinv[0][0]*v[0]+Hinv[0][1]*v[1]+Hinv[0][2]*v[2]
        j = Hinv[1][0]*v[0]+Hinv[1][1]*v[1]+Hinv[1][2]*v[2]
        k = Hinv[2][0]*v[0]+Hinv[2][1]*v[1]+Hinv[2][2]*v[2]
        
#Normalizacao da ultima coordenada
        i=int(i/k)
        j=int (j/k)
        if i>=0 and j>=0 and i<x and j<y:
            scene.putpixel([ a, b ], picture.getpixel((int(i), int(j))))
		
scene.save("result.jpg")
#scene.save("result2.jpg")
scene.show()
