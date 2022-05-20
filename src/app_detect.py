import torch
import pandas as pd

def detec_son(path_imagen):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='.\\src\\pesos\\yolov5s.pt', force_reload=True) 
    # Image\
    img = path_imagen
    # Inference
    model.conf = 0.6
    results = model(img)
    # Results, change the flowing to: results.show()
    results.save()
    print(results)  # or .show(), .save(), .crop(), .pandas(), etc
    #results.pandas()
    indicador=1
    return