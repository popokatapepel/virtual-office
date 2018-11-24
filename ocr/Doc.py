import pytesseract, enum, re
from PIL import Image

class DocType(enum.Enum):
    PAYROLL = 1
    BILL = 2
    REGISTRATIONCERT = 3


class Doc:
    prefLang = "de"

    def __init__(self, path):
        self.path = path
        self.text = None
        self.type = None
        self.sender = None
    def extract(self):
        self.text = pytesseract.image_to_string(Image.open(self.path))
    def classifyType(self):
        if self.text != None:
            if "Entgeltabrechung" in self.text:
                self.type = DocType.PAYROLL
            if "RECHNUNG" in self.text:
                self.type = DocType.BILL
            if "Meldebescheinigung" in self.text:
                self.type = DocType.REGISTRATIONCERT
        return self.type
    def analyzeSender(self):
        if self.text != None:
            if "KIT" in self.text:
                self.sender = "KIT"
            if "DPD" in self.text:
                self.sender = "DPD"
            if "Sozialversicherung" in self.text:
                self.sender = "Sozialversicherung"
        return self.sender
    def getTodotext(self):
        if self.type == DocType.BILL or self.sender == "DPD":
            pattern = re.compile('[0-9]{2}( [0-9]{5}){5}')
            match = pattern.search(self.text)
            print(match)
            if match == None:
                return "Bezahle Rechnung"
            else:
                return "Bezahle Rechnung " + match.group(0)
        if self.type == DocType.REGISTRATIONCERT or self.sender == "Sozialversicherung":
            return "Steuererklärung einreichen"
