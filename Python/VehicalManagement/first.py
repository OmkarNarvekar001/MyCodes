class manage():
    def __init__(self, oname, vname, vno, phno, type='fuel'):
        self.oname = oname
        self.vname = vname
        self.vno = vno
        self.phno = phno
        self.type = type

    def setoname(self, oname):
        self.oname = oname

    def getoname(self):
        return self.oname

    def setvname(self,vname):
        self.vname = vname

    def getvname(self):
        return self.vname

    def setvno(self, vno):
        self.vno = vno

    def getvno(self):
        return self.vno

    def setphno(self, phno):
        self.phno = phno

    def getphno(self):
        return self.phno

    def settype(self, type):
        self.type = type

    def gettype(self):
        return self.type

