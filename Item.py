class Item:
    def __init__(self, name, cost, subtype, replacementDuration, dateCreated, dateOfReplacement):
        self.itemName = name
        self.cost = cost
        self.subtype = subtype
        self.replacementDuration = replacementDuration
        self.dateCreated = dateCreated
        self.dateOfReplacement = dateOfReplacement

    def getItemName(self):
        return self.itemName

    def getCost(self):
        return self.cost

    def getSubtype(self):
        return self.subtype

    def getReplacementDuration(self):
        return self.replacementDuration

    def getDateCreated(self):
        return self.dateCreated

    def getDateOfReplacement(self):
        return self.dateOfReplacement