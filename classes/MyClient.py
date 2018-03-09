class MyClient:

    def __init__(self, secretFileName, applicationName):
        self.scopes = {'readonly' : 'https://www.googleapis.com/auth/calendar.readonly'}
        self.secretFile = self.getSecretFileName(secretFileName)
        self.applicationName = applicationName

    def getSecretFileName(self, secretFileName):
        return

    def getAllScopes(self):
        return self.scopes

    def getScopeByType(self, scopeType):
        if scopeType in self.scopes.keys():
            return self.scopes[scopeType]

        return False