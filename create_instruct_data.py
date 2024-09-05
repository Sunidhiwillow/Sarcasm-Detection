import json
import pandas as pd
import os

image_path = '/data/soumyadeep/PA/multimodal_data/dataset_image'


#files = ['train.json', 'valid.json', 'test.json']
files = ['test.json']

for file in files:
    dataset = []
    f1= open(file,'r',encoding='utf-8')
    datas = json.load(f1)

    for data in datas:
        data_dict=dict()
        image_id = data['image_id']
        sentence = data['text']
        label = data['label']
        if os.path.isfile(image_path+'/'+str(image_id)+".jpg"):
        
            data_dict = {
                            "id": str(image_id),
                            "image": str(image_id) + '.jpg',
                            "conversations": 
                            [
                                {
                                    "from": "human",
                                    "value": f'The text associated with the image reads <{sentence}>. Is the image-text pair sarcastic?'
                                },
                                {
                                    "from": "gpt",
                                    "value": str(label)
                                },
                            ]
                        }
        
            dataset.append(data_dict)



    # convert into json
    with open(f"mmsd2_{file}_instruct.json", "w") as final:
        json.dump(dataset, final, indent=4)
    
    print('saved')