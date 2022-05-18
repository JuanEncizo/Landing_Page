import torch
import pandas as pd

def detec_son(path_imagen):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\User\\Desktop\\Landing_Page\\src\\pesos\\best.pt', force_reload=True) 
    # Image\
    img = path_imagen
    # Inference
    model.conf = 0.7
    model.exist_ok = True

    results = model(img)
    # Results, change the flowing to: results.show()
    results.save()
    print(results)  # or .show(), .save(), .crop(), .pandas(), etc
    #results.pandas()

    print("robert")

    return

