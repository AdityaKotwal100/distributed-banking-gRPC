import time
import json
import constants
from customer import Customer

if __name__ == "__main__":
    objects_list = []

    # Read the input JSON
    # TODO: Change file path here according to requirements
    with open("input.json", "r") as f:
        json_data = json.load(f)

    # Instantiate the Customer objects based on the input JSON file
    branch_ids = []
    for item in json_data:
        if item[constants.TYPE_FIELD] == constants.CUSTOMER:
            customer_obj = Customer(
                id=item[constants.ID_FIELD], events=item[constants.EVENTS_FIELD]
            )
            # Create a Branch stub for each object of the customer
            customer_obj.createStub()
            objects_list.append(customer_obj)

    final_result = []
    for i,obj in enumerate(objects_list):
        # Adding a delay of 1 second between each event execution to give enough time for transactions to complete
        print(f"Execution of customer {i//2 + 1} events -> Started")
        # Execute events assigned to the objects
        event_result = obj.executeEvents()
        time.sleep(1)
        print(f"Execution of customer {i//2 + 1} events -> Finished")
        print("Sleeping for 1 second")
        final_result.extend(event_result)

    # Write the output into a file
    with open("output.json", "w+") as f:
        f.write(json.dumps(final_result))

    print("Results stored in output.json")
    print("Debug logs stored in branchDebug.txt & customerDebug.txt")
