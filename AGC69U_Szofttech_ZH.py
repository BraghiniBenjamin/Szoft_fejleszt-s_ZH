import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json


def jsopen(filename) -> dict:
    file = open(filename,'r')
    file_contents = json.load(file)
    file.close()
    return file_contents


panel1 = jsopen('Panels_1.json')
p10i = panel1['Panels_1'][0]['Images']
p11i = panel1['Panels_1'][1]['Images']
error = panel1['Panels_1'][2]
panel3 = jsopen('Panels_3.json')
p30i = panel3['Panels_3'][0]['Images']
p31i = panel3['Panels_3'][1]['Images']
panel6 = jsopen('Panels_6.json')
p60i = panel6['Panels_6'][0]['Images']
p61i = panel6['Panels_6'][1]['Images']
Panels = p10i + p11i + p30i + p31i + p60i + p61i


def drawing():
    imageName = '361_366_D211AABB3A20200005.jpg'
    fig, ax = plt.subplots()
    image = Image.open(imageName)
    j = 0
    found = False
    while(j < len(Panels) and not found):
        if Panels[j]['ImageName'] == imageName:
            for i in range(len (Panels[j]['BoundingBoxes'])):
                OI = Panels[j]['BoundingBoxes'][i]['ObjectIndex']
                print(Panels[j]['BoundingBoxes'][i]['ObjectIndex'])
                if OI == 1:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Green', facecolor='none')
                    ax.add_patch(rect)
    
                elif OI == 2:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width)
                    posy = (CenterY*image.height)
                    rect = patches.Circle((posx, posy), Width*image.width/2, linewidth=1, edgecolor='Blue', facecolor='none')
                    ax.add_patch(rect)
    
                elif OI == 3:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Purple', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 4:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Lime', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 5:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width)
                    posy = (CenterY*image.height)
                    rect = patches.Circle((posx, posy), Width*image.width/2, linewidth=1, edgecolor='Purple', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 6:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Red', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 7:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Blue', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 8:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Yellow', facecolor='none')
                    ax.add_patch(rect)

                elif OI == 0:
                    CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                    print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                    CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                    print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                    Width = Panels[j]['BoundingBoxes'][i]['Width']
                    print(Panels[j]['BoundingBoxes'][i]['Width'])
                    Height = Panels[j]['BoundingBoxes'][i]['Height']
                    print(Panels[j]['BoundingBoxes'][i]['Height'])
                    posx = (CenterX*image.width) - ((Width*image.width)/2)
                    posy = (CenterY*image.height) - ((Height*image.height)/2)
                    rect = patches.Rectangle((posx, posy), Width*image.width, Height*image.height, linewidth=1, edgecolor='Orange', facecolor='none')
                    ax.add_patch(rect)

                else:
                    print("Incorrect option")
        j = j+1
    ax.imshow(image)
    plt.show()

def main():
    drawing()

if __name__ == "__main__":
    main()