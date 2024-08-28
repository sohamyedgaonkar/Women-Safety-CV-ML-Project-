import os
# importing the module 

from PIL import Image 
def abc (fil):
    # loading the image 
    img = Image.open(fil) 

    # fetching the dimensions 
    wid, hgt = img.size 

    # displaying the dimensions 
    return wid,hgt
k=0
folder_path=r"""c:\Users\DELL\Desktop\ok check\labels"""
image_folder=r"""c:\Users\DELL\Desktop\human\yolo\OIDv4_ToolKit\OID\Dataset\train\images\train"""

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if filename.endswith('.txt'):
        with open(file_path, 'r') as file:
            data = file.readlines()
            #print(data)
            w,h =abc(image_folder+"\\" +filename[:-3]+"jpg")
            final=[]
            for i in data:
                x=i.split()
                temp=[]
                if x[0]=="Man" or x[0]=="0":
                    temp.append("0")
                else:
                    temp.append("1")
                xmin=float(x[1])
                xmax=float(x[3])
                ymin=float(x[2])
                ymax=float(x[4])
                bwid=(xmax/w)-(xmin/w)
                bhei=(ymax/h)-(ymin/h)
                xcen=(xmin/w)+(bwid/2)
                ycen=(ymin/h)+(bhei/2)
                temp.append(str(xcen))
                temp.append(str(ycen))
                temp.append(str(bwid))
                temp.append(str(bhei))
                m=" ".join(temp)
                final.append(m +"\n")

        k=k+1
        print(k)
        print(final)   
        #data = data.replace('Man', '0').replace('Woman', '1')
        with open(file_path, 'w') as file:
            
            file.writelines(final)
print("Replacement completed!")