import os 
import lxml.etree as ElementTree
from .groupmgr import GroupMgr



class ModelConfig:
    def __init__(self,filename=None):
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"modelcfg.xml")

        self.sep = None
        self.prettyMap = {}
        self.fmtMap = {}
        self.dtypeMap = {}
        self.multMap = {}
        self.fmtDefault="%f"
        self.dtypeDefault="f4"
        self.multDefault=1
        self.defaultHistograms=set()
        self.internalCols=set()
        self.invert=[]

        et=ElementTree.parse(filename)
        root = et.getroot()
        assert root.tag == "modelcfg"
        for child in root:
            if child.tag == "datsep" and child.text:
                self.sep=child.text
            if child.tag == "defaulthistograms":
                self.defaultHistograms=set(child.get("names").split(","))
            if child.tag == "hidden":
                self.internalCols=set(child.get("names").split(","))
            if child.tag == "fields":
                for field in child:
                    if field.get("nm") == "default":
                        self.fmtDefault=field.get("fmt")
                        self.dtypeDefault=field.get("dtype")
                        self.multDefault=float(field.get("mult"))
                    else:
                        if "fmt" in field.attrib:
                            self.fmtMap[field.get("nm")]=field.get("fmt")
                        if "dtype" in field.attrib:
                            self.dtypeMap[field.get("nm")]=field.get("dtype")
                        if "mult" in field.attrib:
                            self.multMap[field.get("nm")]=float(field.get("mult"))
                        if "prettyname" in field.attrib:
                            self.prettyMap[field.get("nm")]=field.get("prettyname")
                        if "invert" in field.attrib and field.get("invert") == "True":
                            self.invert.append(field.get("nm"))

    def prettyname(self,field):
        r=field
        if r.startswith(GroupMgr.prefix):
            r=field[len(GroupMgr.prefix):]
        if r in self.prettyMap:
            r=self.prettyMap[r]
        return r

    def dtype(self,field):
        r=self.dtypeDefault
        # but if it is a group, then it should be an int
        if field.startswith(GroupMgr.prefix):
            r='i4'
        if field in self.dtypeMap:
            r= self.dtypeMap[field]
        return r

    def fmt(self,field):
        r=self.fmtDefault
        # but if it is a group, then it should be an int
        if field.startswith(GroupMgr.prefix):
            r='%i'
        if field in self.fmtMap: # or if we already know what it should be
            r= self.fmtMap[field]
        return r

    def multvalue(self,field):
        r=self.multDefault
        if field in self.multMap:
            r= self.multMap[field]
        return r




