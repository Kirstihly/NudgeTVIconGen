'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
#-----------------------------------
# URL encoding
from datetime import datetime
from pytz import timezone
import bitly_api


API_USER =
API_KEY = 
b = bitly_api.Connection(API_USER, API_KEY)



def URL_encoding(name):
    
    eastern = datetime.now(timezone('US/Eastern')) # Ensure the correctness
    year = eastern.year
    
    if eastern.month > 2 and eastern.month <= 5:
        season = 'spring'
    elif eastern.month > 5 and eastern.month <= 8:
        season = 'summer'
    elif eastern.month > 8 and eastern.month <= 11:
        season = 'fall'
    else:
        season = 'winter'
    
    utm_source = 'nudgetv.com'
    utm_medium = 'nudgeicon'
    utm_campaign = 'nudge'+season+str(year) #Other specification
    longurl = name+'?utm_source='+utm_source+'&utm_medium='+utm_medium+'&utm_campaign='+utm_campaign
    
    return longurl

def Short_encoding(longurl, b):
    response = b.shorten(uri = longurl)
    return response['url']

#-----------------------------------
# Icon Generation
import numpy as np
from math import sin, cos, pi
from PIL import Image
from PIL import ImageDraw
from matplotlib.pyplot import imshow

COLOR_RED = (153, 255, 153)
COLOR_WHITE = (255, 255, 255)
ROUND = 6
CAMERA_WIDE = 800
CAMERA_HEIGHT = 500
LENS_SIZE = 80
FLASH_SIZE = 80
BUTTON_LENTH = 100
BUTTON_HEIGHT = 40
_BUTTON_LENTH = 70
_BUTTON_HEIGHT = 20
FLASH_BAR_LENTH = 400
FLASH_BAR_HEIGHT = 80
_FLASH_BAR_LENTH = 350
_FLASH_BAR_HEIGHT = 50
DATA_TRACK_THICKNESS = 20
FITST_DATA_TRACK_RADIUS = 80
DATA_TRACK_DISTANCE = 40
DATA_TRACK_NUMBER = 5
DATA_BIT_NUMBER_ON_DATA_TRACK = 4


def coordinate_transform(x, y):
    # The input is the coordinate based on the center of the lens
    # The output is the coordinate based on the left top corner of the image
    return x+CAMERA_WIDE/2, y+CAMERA_HEIGHT/2+FLASH_BAR_HEIGHT


def drawRoundRec(im, color, center, w, h, r):
    (x, y) =center
    r *= 2
    x -= w/2
    y -= h/2
    drawObject = ImageDraw.Draw(im)
    
    '''Rounds'''    
    drawObject.ellipse((x,y,x+r,y+r),fill=color)    
    drawObject.ellipse((x+w-r,y,x+w,y+r),fill=color)    
    drawObject.ellipse((x,y+h-r,x+r,y+h),fill=color)    
    drawObject.ellipse((x+w-r,y+h-r,x+w,y+h),fill=color)
    
    '''rec.s'''    
    drawObject.rectangle((x+r/2,y, x+w-(r/2), y+h),fill=color)    
    drawObject.rectangle((x,y+r/2, x+w, y+h-(r/2)),fill=color)
    
def drawRing(im, color, center, r, t):
    (x, y) =center
    
    drawObject = ImageDraw.Draw(im)
    
    drawObject.ellipse((x-r-t/2,y-r-t/2,x+r+t/2,y+r+t/2),fill=COLOR_WHITE)
    drawObject.ellipse((x-r+t/2,y-r+t/2,x+r-t/2,y+r-t/2),fill=color)
    
def drawData(im, color, center, t):
    (x, y) =center
    
    drawObject = ImageDraw.Draw(im)
    
    drawObject.rectangle((x-t/2, y-t/2, x+t/2, y+t/2),fill=color)
    
def generateIcon(int_input):
    image_wide = CAMERA_WIDE
    image_height = CAMERA_HEIGHT + FLASH_BAR_HEIGHT
    im = Image.new('RGBA', (image_wide, image_height+10), (255, 255, 255, 100))


    # draw the main part of the camera
    drawRoundRec(im, COLOR_RED, coordinate_transform(0,0), CAMERA_WIDE, CAMERA_HEIGHT, ROUND)


    # draw flash
    drawRoundRec(im, COLOR_WHITE, coordinate_transform(CAMERA_WIDE*3/8,-CAMERA_HEIGHT/3), FLASH_SIZE, FLASH_SIZE, ROUND)

    #draw button
    drawRoundRec(im, COLOR_RED, coordinate_transform(-CAMERA_WIDE*3/8,-CAMERA_HEIGHT/2), 
                 BUTTON_LENTH, BUTTON_HEIGHT, BUTTON_HEIGHT/2)

    #draw _button
    drawRoundRec(im, COLOR_WHITE, coordinate_transform(-CAMERA_WIDE*3/8,-CAMERA_HEIGHT/2), 
                 _BUTTON_LENTH, _BUTTON_HEIGHT, _BUTTON_HEIGHT/2)

    #draw flash bar
    drawRoundRec(im, COLOR_RED, coordinate_transform(0,-CAMERA_HEIGHT/2), 
                 FLASH_BAR_LENTH, FLASH_BAR_HEIGHT, FLASH_BAR_HEIGHT/2)

    #draw _flash bar
    drawRoundRec(im, COLOR_WHITE, coordinate_transform(0,-CAMERA_HEIGHT/2), 
                 _FLASH_BAR_LENTH, _FLASH_BAR_HEIGHT, _FLASH_BAR_HEIGHT/2)

    #draw data tracks
    for i in range(DATA_TRACK_NUMBER, 0, -1):
        drawRing(im, COLOR_RED, coordinate_transform(0,0), FITST_DATA_TRACK_RADIUS+(i-1)*DATA_TRACK_DISTANCE, DATA_TRACK_THICKNESS)

    # draw lens
    drawRoundRec(im, COLOR_WHITE, coordinate_transform(0,0), LENS_SIZE, LENS_SIZE, ROUND)

    # draw data
    bin_input = int(bin(int_input)[2:])
    for i in range(len(str(bin_input))):
        bit = bin_input%10
        bin_input = int(bin_input/10)

        if bit: 
            num_data_track = int(i/DATA_BIT_NUMBER_ON_DATA_TRACK)
            data_position = i % DATA_BIT_NUMBER_ON_DATA_TRACK

            r = FITST_DATA_TRACK_RADIUS+num_data_track*DATA_TRACK_DISTANCE

            x = r * cos(data_position*2*pi/DATA_BIT_NUMBER_ON_DATA_TRACK)
            y = r * sin(data_position*2*pi/DATA_BIT_NUMBER_ON_DATA_TRACK)

            drawData(im, COLOR_RED, coordinate_transform(x,y), DATA_TRACK_THICKNESS*2)

    im_name = 'images/'+str(int_input)+'.png'
    save_im_name = 'media/'+im_name
    im.save(save_im_name)
    
    return im_name

#-----------------------------------
# main
import sqlite3
import pandas
if __name__ == '__main__':
    
    pconn = sqlite3.connect('db.sqlite3')
    df_t1 = pandas.read_sql('SELECT * FROM NudgeTVURLInputs', pconn)
    df_t2 = pandas.read_sql('SELECT * FROM NudgeTVIcons', pconn)

    if df_t2.empty or df_t1.shape[0] > df_t2.shape[0]:
        for i in range(df_t2.shape[0], df_t1.shape[0]):
            text = df_t1['urls_text'][i]
            text_UTM = URL_encoding(text)
            text_short = Short_encoding(text_UTM, b)
            assigned_id = df_t1.at[i, 'id']
            im_name = generateIcon(assigned_id)
            add_row = pandas.DataFrame({'urls_input_id': [assigned_id],
                                       'urls_UTM': [text_UTM], 'urls_shortened': [text_short],
                                       'assigned_id': [assigned_id], 'icon_image': [im_name]})
            add_row.to_sql('NudgeTVIcons', pconn, if_exists='append')
    pconn.close()
