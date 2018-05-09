'''
    Create By KuoYinPo
    4,19,2018
    For Yolo Lables create tools
'''
import sys
import os
from PIL import Image
#============================#
def BBox_yolo(bbox,imsize):
    imw = imsize[0]
    imh = imsize[1]
    lux = float(bbox[0])
    luy = float(bbox[1])
    rdx = float(bbox[2])
    rdy = float(bbox[3])
    bbw = rdx - lux #lux -rdx
    bbh = rdy - luy #luy -rdy
    centerx = (lux+rdx)/2
    centery = (luy+rdy)/2
    x = centerx/imw
    y = centery/imh
    w = bbw/imw
    h = bbh/imh
    print("lux:{} luy:{} rdx:{} rdy{}:".format(lux,luy,rdx,rdy))
    return[str(x),str(y),str(w),str(h)]
#==============================#
categroys = {'person':'0'}
outputpath = "/Users/kevinkuo/anaconda3/envs/bbox/BBox-Label-Tool/Labels/new/"
imagepath = "/Users/kevinkuo/anaconda3/envs/bbox/BBox-Label-Tool/Examples/001/"
print("pwd: {}".format(os.getcwd()))
path = "/Users/kevinkuo/anaconda3/envs/bbox/BBox-Label-Tool/Labels/001/"

# 1.Read dir. and filename to create a list #

#print(path)
filename = os.listdir(path)
#print(filename)
listd =[]
listf =[]
for f in filename:
    dirpath = os.path.join(path,f)
    if os.path.isfile(dirpath):
        listf.append(dirpath)
    if os.path.isdir(dirpath):
        listd.append(dirpath)

imagename = os.listdir(imagepath)
#print(imagename)
listimg =[]
for I in imagename:
    if I.split('.',1)[1]=='JPEG':
        imgpath = os.path.join(imagepath,I)
        if os.path.isfile(imgpath):
            listimg.append(imgpath)
#print(listimg)
#print(listf)
#print(listd)
#===========================================

# 2. Read txt file and collect all data in there
bbox =[]#data struct
txtlist =[]
i=1
for N in listf:
    #print(N.split('.',1)[1])
    if N.split('.',1)[1] == 'txt': # pretect the file profix didn't txt will cause code error
        with open(N) as txt:
            txtdata = txt.read()
            txtlist = txtdata.split('\n') # Reslove bbox
            print("textlist:{}".format(txtlist))
            for cats in range(int(txtlist[0])): #create bbox object
                bbox=txtlist[cats+1].split( )
                #print(N.split("Labels",1)[1])
                TempStr = N.split("Labels",1)[1]
                print(TempStr.split('.',1)[0])
                imp = N.split("Labels",1)[0] + "Examples"+TempStr.split('.',1)[0]+".JPEG"
                #print(imp)
                im = Image.open(imp)
                ims= im.size
                print("bbox:{},image_size{}".format(bbox,ims))
                Yolobox = BBox_yolo(bbox,ims)
                print(Yolobox)
                # Write the new Yolo lable test (not sure the format)
                lable = TempStr.split('/')[2]
                #print("Hello:{}".format(TempStr.split('/')))
                outtxt = outputpath + lable
                #print(outtxt)
                out = open(outtxt,'a')
                Yolobox.insert(0,categroys['person'])
                for writ in Yolobox:
                    e=writ+" "
                    out.write(e)
                out.write("\n")
                print("Lable/{} done".format(lable))
                out.close()
                print("")
                #print(cats)
        txt.close()

