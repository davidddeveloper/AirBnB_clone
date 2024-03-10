#!/usr/bin/env python3
from models import storage
all_objs = storage.all()
print(dir(all_objs.values()))
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj.__dict__)
