import grpc
import svc_pb2_grpc
from concurrent import futures
import json
import constants
import logging
import threading
import os
from branch import Branch


def clear_files():
    file_paths = ["customerDebug.txt", "branchDebug.txt", "output.json"]
    for file in file_paths:
        if os.path.exists(file):
            os.remove(file)
    print("Cleared output.json, branchDebug.txt & customerDebug.txt")


# Parallel function that starts a given server
def start_server(server):
    server.start()
    server.wait_for_termination()


def serve():
    # Clear all the previous files as the server has restarted
    clear_files()
    # Load the input data
    #TODO: Change file path here according to requirements
    with open("input.json", "r") as f:
        json_data = json.load(f)

    branches = []
    stub_list = []
    # Instantiate the objects of the Branch class
    for item in json_data:
        if item[constants.TYPE_FIELD] == constants.BRANCH:
            branch_obj = Branch(
                id=item[constants.ID_FIELD], balance=item[constants.BALANCE_FIELD]
            )
            # Create a Branch stub for each object of the Branch class
            current_branch_stub = branch_obj.createStub()
            stub_list.append(current_branch_stub)
            branches.append(branch_obj)

    server_list = []
    # For each branch, get the server object in a list
    for branch in branches:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        branch.branches = [each_branch.id for each_branch in branches]
        branch.stubList = stub_list
        # Add the Branch servicer as a listener to the server
        svc_pb2_grpc.add_BranchServicer_to_server(branch, server)
        # Generate a listening port on the server for the branches
        port = "50000"
        port_list = list(port)
        id_list = list(str(branch.id))
        port_list[len(port_list) - len(id_list) :] = id_list
        str_port = "".join(port_list)
        server.add_insecure_port(f"localhost:{str_port}")
        print(f"Listening on port {str_port}")
        server_list.append(server)

    # Now that we have a list of servers, start each of them on individual threads
    threads = []
    for serv in server_list:
        thread = threading.Thread(target=start_server, args=(serv,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


logging.basicConfig()

if __name__ == "__main__":
    serve()
