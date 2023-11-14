
import grpc
import svc_pb2
import svc_pb2_grpc
import constants
from typing import Dict, Union, List
from google.protobuf.json_format import MessageToDict



class Customer:
    def __init__(self, id: int, events: List[Dict[str, Union[int, str]]]):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = []
        # pointer for the stub
        self.stub = None

    def createStub(self):
        """
        Create a gRPC stub to communicate with the Branch.

        This method initializes a gRPC stub for communication with a Branch process.

        Returns:
            svc_pb2_grpc.BranchStub: The gRPC stub for the Branch process.

        Examples:
            branch_stub = branch.createStub()
        """
        # Initialize gRPC stub to communicate with the Branch
        self.stub = svc_pb2_grpc.BranchStub(
            grpc.insecure_channel(f"localhost:{self.__port_logic()}")
        )

    def __port_logic(self):
        """
        Determine the port for communication with the Branch process.

        This private method calculates and returns the port number for establishing
        communication with the Branch process based on a specific logic.

        Returns:
            str: The port number to use for communication.

        Example:
            port = self.__port_logic()
        """
        # Replace the last 'n' digits of the port string with the ID in order to create a unique port number
        port = "50000"
        port_list = list(port)
        id_list = list(str(self.id))
        digits_to_replace = len(id_list)
        port_list[len(port_list) - digits_to_replace :] = id_list
        return "".join(port_list)

    def __debugOutput(self):
        """
        Display a debug message for debugging purposes.

        This method is used to display a debug message for debugging and logging
        purposes.

        Args:
            message (str): The debug message to be displayed.

        Returns:
            None

        Example:
            branch.__debugOutput()
        """
        with open("customerDebug.txt", "a") as f:
            for msg in self.recvMsg:
                f.write(str(msg))
                f.write("\n")
                f.write("-" * 100)
                f.write("\n")

    def __formatResults(
        self, results: List[Dict[str, Union[int, List[Dict[str, Union[str, float]]]]]]
    ):
        """
        Format the results received from the Branch process.

        This private method takes the results received from the Branch process and
        formats them for further processing or display.

        Args:
            results (list[dict]): A list of dictionaries containing results from the
                Branch process.

        Returns:
            list[dict]: A formatted list of dictionaries with results.

        Example:
            formatted_results = self.__formatResults(results)
        """
        for each_query in results:
            for each_recv in each_query[constants.RECV_FIELD]:
                if (
                    each_recv[constants.INTERFACE_FIELD] == constants.QUERY
                    and constants.RESULT_FIELD in each_recv.keys()
                ):
                    each_recv.pop(constants.RESULT_FIELD)

        # Create a dictionary to temporarily store merged data
        # Group processed results by ID
        result_dict = {}
        for item in results:
            if item["id"] in result_dict:
                result_dict[item["id"]]["recv"].extend(item["recv"])
            else:
                result_dict[item["id"]] = {"id": item["id"], "recv": item["recv"]}

        # Convert the values of result_dict into a list
        return list(result_dict.values())

    def executeEvents(self) -> Dict[str, Union[int, List[Dict[str, Union[int, str]]]]]:
        """
        Execute a sequence of events using the gRPC stub.

        This method iterates through a list of events and uses the gRPC stub to send
        each event to the Branch process. It collects the results of these events and
        returns them in a structured format.

        Returns:
            Dict[str, Union[int, List[Dict[str, Union[int, str]]]]: A dictionary
            containing information about the execution of events, including event
            results.

        Example:
            event_results = self.executeEvents()
        """
        event_result = []
        if not self.stub:
            print("Error: gRPC stub not initialized")
            return

        for event in self.events:
            # Add a dummy money field in order to be sent to the Branch process
            if constants.MONEY_FIELD not in event.keys():
                event[constants.MONEY_FIELD] = None
                
            # Call the Branch MsgDelivery RPC
            response = self.stub.MsgDelivery(
                svc_pb2.MsgDeliveryRequest(
                    id=self.id,
                    interface=event[constants.INTERFACE_FIELD],
                    money=event[constants.MONEY_FIELD] or None,
                )
            )
            # Convert the result into a dictionary in order to store in recvMsg and results
            resp_dict = MessageToDict(response)
            self.recvMsg.append(resp_dict)
            event_result.append(resp_dict)

        # Store the recieved messages in customerDebug.txt file
        self.__debugOutput()
        # Format results as required in the output
        return self.__formatResults(event_result)
