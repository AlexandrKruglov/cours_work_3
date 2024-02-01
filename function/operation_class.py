
class Operation:
    def __init__(self, operation_id, date, state, operation_amount, description, operation_to):
        self.operation_id = operation_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.operation_to = operation_to
        self.description = description
#       self.name_amount = name_amount

    def __repr__(self):
        return (f"Operation({self.operation_id}, {self.date}, {self.state}, {self.operation_amount}, {self.description}, {self.operation_to})")

    def check_oeration_stage(self):
        pass
