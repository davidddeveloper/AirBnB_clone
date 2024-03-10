from models import storage
from models.base_model import BaseModel

"""print("calling storage.all")
print("----------------------------")
print(storage.all())
print("----------------------------")
model1 = BaseModel()
storage.new(model1)
storage.save()
print("Model 1 id\n", model1.id)
print("all the obj")
print("----------------------------")
print(storage.all())
print("----------------------------")"""

print("----------------test reload---------------")
storage.reload()
print("------------first reload--------------")
print(storage.all())
print("------------second reload--------------")
storage.reload()
print(storage.all())
# if both reloads are the same then reloads work properly
# that is we are checking if the object is already in __objects before creating a new one
