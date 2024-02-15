import json

class payload_model:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

# # Create an instance of the Employee class and serialize it
# employee = payload_model("morpheus", "leader")
# serialized_employee = employee.serialize()
#
# # Print the serialized POJO
# print(serialized_employee)