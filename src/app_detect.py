import torch
import pandas as pd
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\User\\Desktop\\Landing_Page\\src\\pesos\\best.pt', force_reload=True) 
# Image\
img = 'C:\\Users\\User\\Desktop\\Landing_Page\\src\\667-1.jpg'
# Inference
results = model(img)
# Results, change the flowing to: results.show()
results.save()
print(results)  # or .show(), .save(), .crop(), .pandas(), etc
#results.pandas()

print("robert")
