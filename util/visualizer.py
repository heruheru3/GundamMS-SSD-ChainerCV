import numpy as np
from PIL import Image,ImageDraw

# draw bounding-box and label
def draw_bbox(img, bbox, labels, score, label_color, padding=1, is_bgr=False):
    dr = ImageDraw.Draw(img)
    for i,axiz in enumerate(bbox):
        label = list(label_color.keys())[labels[i]]
        axiz = np.int32(axiz)
        
        ms_name, ms_color = label_color[label]
        if is_bgr:
            ms_color = ms_color[2],ms_color[1],ms_color[0]
        label_score = "{0} {1}, {2:2.2f}".format(label, ms_name , score[i])
        stp = (axiz[1],axiz[0])
        edp = (axiz[3],axiz[2])
        edp_back = (axiz[3],axiz[0]+10)
        
        rect = Image.new("RGB", (axiz[3]-axiz[1],axiz[2]-axiz[0]), color=ms_color)
        mask=Image.new('L', rect.size, color=64)
        img.paste(rect, stp , mask=mask)
        
        dr.rectangle((stp,edp_back),fill=ms_color)
        dr.rectangle((stp,edp),outline=ms_color)
        dr.rectangle(((stp[0]-padding, stp[1]-padding),(edp[0]+padding,edp[1]+padding)),outline=ms_color)
        
        stp_text = (axiz[1]+5,axiz[0])
        dr.text(stp_text, label_score)
    return img