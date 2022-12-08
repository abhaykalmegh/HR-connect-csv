import csv


class HandleCSV:

    filename = "employees.csv"
    all = []
    def __init__(self, FIRST_NAME: str, LAST_NAME: str, EMAIL:str,PHONE_NUMBER):

        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.EMAIL = EMAIL
        self.PHONE_NUMBER = PHONE_NUMBER

        HandleCSV.all.append(self)
    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()


    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

    @classmethod
    def instantiate_from_csv(cls):
        with open('employees.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            HandleCSV(
                first_name = str(item.get('FIRST_NAME')),
                last_name = str(item.get('LAST_NAME')),
                email = str(item.get('EMAIL'))
            )

    def __repr__(self):
        return f"Item('{self.FIRST_NAME}', {self.LAST_NAME}, {self.EMAIL})"


# TODO - ADD MORE SUCH METHODS HERE
# TODO - UNDERSTAND USAGE OF `classmethod` HERE

print(HandleCSV.all)