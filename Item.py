class Item:
    def __init__(self, name, cost, subtype, replacementDuration):
        self.itemName = name
        self.cost = cost
        self.subtype = subtype
        self.replacementDuration = replacementDuration
    def getItemName(self):
        return self.itemName

    def getCost(self):
        return self.cost

    def getSubtype(self):
        return self.subtype

    def getReplacementDuration(self):
        return self.replacementDuration

# Todo : Have a date created attribute for the item