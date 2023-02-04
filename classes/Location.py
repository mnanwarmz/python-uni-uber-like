class Location:
    def __init__(self, locationId, locationName):
        self.id = locationId
        self.name = locationName

    def __str__(self):
        return "Location: " + self.name + " (" + self.id + ")"
