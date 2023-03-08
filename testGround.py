from import_frame import get_1_frame


inputparameters = {}
outputparameters = {}
ffreader = skvideo.io.FFmpegReader(reference,inputparameters, outputparameters)

oshow= get_1_frame(ffreader,12)
cv2_imshow(oshow)
