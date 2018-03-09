
from __future__ import print_function

import os

from oauth2client import tools, client
from oauth2client.client import Storage


class Authentication:

    def __init__(self):
        try:
            import argparse
            self.flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            self.flags = None

        self.setDefaultCredentialProperties()

    def setDefaultCredentialProperties(self):
        self.homeDir = os.path.expanduser('~')
        self.credentialDir = os.path.join(self.homeDir, '.credentials')
        if not os.path.exists(self.credentialDir):
            os.makedirs(self.credentialDir)
        self.credentialPath = os.path.join(self.credentialDir, 'calendar-python-quickstart.json')

    def getCredentials(self, myClient):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        store = Storage(self.credentialPath)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(myClient.getSecretFileName(), myClient.getScopeByType('readonly'))
            flow.user_agent = myClient.applicationName
            if self.flags:
                credentials = tools.run_flow(flow, store, self.flags)
            print('Storing credentials to ' + self.credentialPath)
        return credentials
