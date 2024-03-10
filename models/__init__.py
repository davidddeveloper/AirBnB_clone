from models.engine.file_storage import FileStorage

storage = FileStorage()  # creates a file storage
storage.reload()  # deserializes the JSON file to __objects
