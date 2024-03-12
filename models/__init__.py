from models.engine.file_storage import FileStorage

__all__ = ["BaseModel", "User", "State", "Amenity", "Review", "Place"]
storage = FileStorage()  # creates a file storage
storage.reload()  # deserializes the JSON file to __objects
