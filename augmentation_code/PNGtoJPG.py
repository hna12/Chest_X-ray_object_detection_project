from PIL import Image
import glob
input_path = "/content/cutmix_ver5/*.png"
file_list = [f for f in glob.glob(input_path)]
from PIL import Image
for i in tqdm(range(0,len(file_list))):
    text = file_list[i].split('.')[-2]
    im = Image.open(text+".png").convert('RGB')
    text_1 = text.split('/')[-1]
    im.save('/content/drive/MyDrive/KDT/offline/project/cutmix/'+ text_1+'.jpg', 'jpeg') #png -> jpg
