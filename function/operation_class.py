
class Operation:
    def __init__(self, operation_id, date, state, operation_amount, name_amount, description, operation_to, operation_from):
        self.operation_id = operation_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.operation_to = operation_to
        self.description = description
        self.name_amount = name_amount
        self.operation_from = operation_from

    def __repr__(self):
        return (f"Operation({self.operation_id}, {self.date}, {self.state},"
                f"{self.operation_amount}, {self.name_amount}, {self.description},"
                f"{self.operation_to}, {self.operation_from})")



    def check_opration_state(self):
        if self.state == "EXECUTED":
            return True
        elif self.state == "CANCELED":
            return False

    def return_date(self):
        date = self.date
        date_1 = date[0:10]
        thedate = date_1.split('-')
        form_date = thedate[::-1]
        new_date = ".".join(form_date)
        return new_date
