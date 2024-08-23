#basic code for alert

import smtplib
from notifypy import Notify
import numpy as np
import cv2
from mss import mss
from PIL import Image

alert=Notify()
alert.title="Sexo Harrasso"
alert.message="oni chan ga ero shiteru"
alert.icon=r"""D:\plants and pokie\pokemon fire red\Pokemon Orange Generation\Pokemon Dragonstone_01.png"""
alert.send()