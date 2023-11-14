import grpc
import svc_pb2
import svc_pb2_grpc
import constants
from typing import List, Optional


class Branch(svc_pb2_grpc.BranchServicer):
    def __init__(
        self, id: int, balance: int, branches: Optional[List["Branch"]] = None
    ):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = []
        # a list of received messages used for debugging purpose
        self.recvMsg = []
        # iterate the processID of the branches
        self.stub = None

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
        port_list[len(port_list) - len(id_list) :] = id_list
        return "".join(port_list)

    def createStub(self):
        """
        Create a gRPC stub to communicate with the Branch process.

        This method initializes a gRPC stub for communication with a Branch process.

        Returns:
            svc_pb2_grpc.BranchStub: The gRPC stub for the Branch process.

        Example:
            branch_stub = branch.createStub()
        """
        # Create a stub for the branch to enable branch to branch communication
        port = self.__port_logic()
        self.stub = svc_pb2_grpc.BranchStub(grpc.insecure_channel(f"localhost:{port}"))
        return self.stub

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
            branch.__debugOutput("Debug message: This is for debugging purposes.")
        """
        # Store the data in recvMsg into branchDebug.txt for debugging purpose
        with open("branchDebug.txt", "a") as f:
            for msg in self.recvMsg:
                f.write(str(msg))
                f.write("\n")
                f.write("-" * 100)
                f.write("\n")

    def Query(self, request, context):
        """
        Process a balance query request.

        This method is called to process a balance query request from a customer. It handles
        the request and retrieves the branch's current balance, sending it back as a response.

        Args:
            request (svc_pb2.QueryRequest): The request for querying the branch's balance.
            context: The gRPC context.

        Returns:
            svc_pb2.QueryResponse: The response containing the branch's current balance.

        Example:
            response = branch.Query(request, context)
        """
        # Return the balance of the current branch
        self.recvMsg.append(request)
        response = svc_pb2.QueryResponse()
        response.balance = self.balance
        response.message = constants.SUCCESS
        return response

    def Withdraw(self, request, context):
        """
        Process a withdrawal request.

        This method is called to process a withdrawal request from a customer. It handles
        the request, decreases the branch's balance based on the request parameters, and
        sends a response back.

        Args:
            request (svc_pb2.WithdrawRequest): The request containing parameters for
                the withdrawal.
            context: The gRPC context.

        Returns:
            svc_pb2.WithdrawResponse: The response to the withdrawal request.

        Example:
            response = branch.Withdraw(request, context)
        """
        self.recvMsg.append(request)
        response = svc_pb2.Response()

        # If the current balance of the branch is less than the requested withdraw amount, return "fail"
        if self.balance < request.amount:
            result = constants.FAIL
        else:
            # If the current balance of the branch is atleast the requested withdraw amount, withdraw the
            # amount from the balance of the current branch and return "success"
            self.balance -= request.amount
            result = constants.SUCCESS
        response.message = result
        return response

    def Deposit(self, request, context):
        """
        Process a deposit request.

        This method is called to process a deposit request from a customer. It handles
        the request, increases the branch's balance based on the request parameters,
        and sends a response back.

        Args:
            request (svc_pb2.DepositRequest): The request containing parameters for
                the deposit.
            context: The gRPC context.

        Returns:
            svc_pb2.DepositResponse: The response to the deposit request.

        Example:
            response = branch.Deposit(request, context)
        """
        self.recvMsg.append(request)
        response = svc_pb2.Response()
        # Increase the balance of the branch by the requested amount
        self.balance += request.amount
        response.message = constants.SUCCESS
        return response

    def MsgDelivery(self, request, context):
        """
        Process a message delivery request.

        This method is called to process a message delivery request. It handles the
        request, performs the necessary actions based on the request parameters, and
        sends a response back to the Customer Process.

        Args:
            request (svc_pb2.MsgDeliveryRequest): The request containing parameters
                for message delivery.
            context: The gRPC context.

        Returns:
            svc_pb2.MsgDeliveryResponse: The response to the message delivery request.

        Example:
            response = branch.MsgDelivery(request, context)
        """
        self.recvMsg.append(request)
        event_result = {
            constants.ID_FIELD: request.id,
            constants.RECV_FIELD: [],
        }
        interface_type = request.interface
        money = request.money
        if interface_type == constants.QUERY:
            # If the request is for Query, then call the appropriate Branch stub and
            # return the balance
            query_response = self.stub.Query(
                svc_pb2.QueryRequest(customer_id=request.id)
            )
            event_result[constants.RECV_FIELD].append(
                {
                    constants.INTERFACE_FIELD: constants.QUERY,
                    constants.RESULT_FIELD: query_response.message,
                    constants.BALANCE_FIELD: query_response.balance,
                }
            )
            self.__debugOutput()

        elif interface_type == constants.WITHDRAW:
            # If the request is for Withdraw, then call the appropriate Branch stub and
            next_request = svc_pb2.WithdrawRequest(customer_id=request.id, amount=money)
            response = self.stub.Withdraw(next_request)
            event_result[constants.RECV_FIELD].append(
                {
                    constants.INTERFACE_FIELD: constants.WITHDRAW,
                    constants.RESULT_FIELD: response.message,
                }
            )
            # In order to maintain consistency, we call the Propogate Withdraw Request RPC
            # which will perform a withdraw operation on all the other branches
            propogate_withdraw_request = svc_pb2.PropagateWithdrawRequest(
                branch_id=request.id, amount=money
            )
            self.stub.Propagate_Withdraw(propogate_withdraw_request)
            self.__debugOutput()

        elif interface_type == constants.DEPOSIT:
            # In order to maintain consistency, we call the Propogate Deposit Request RPC
            # which will perform a deposit operation on all the other branches
            next_request = svc_pb2.DepositRequest(customer_id=request.id, amount=money)
            response = self.stub.Deposit(next_request)
            event_result[constants.RECV_FIELD].append(
                {
                    constants.INTERFACE_FIELD: constants.DEPOSIT,
                    constants.RESULT_FIELD: response.message,
                }
            )
            propogate_deposit_request = svc_pb2.PropagateDepositRequest(
                branch_id=request.id, amount=money
            )
            self.stub.Propagate_Deposit(propogate_deposit_request)
            self.__debugOutput()
        else:
            # If the operation is not found, return a "fail" message
            response = constants.FAIL
            self.__debugOutput()

        return svc_pb2.MsgDeliveryResponse(
            id=request.id, recv=event_result[constants.RECV_FIELD]
        )

    def Propagate_Withdraw(self, request, context):
        """
        Process a withdrawal propagation request between branches.

        This method is called to process a withdrawal propagation request from one
        branch to another. It handles the request, decreases the branch's balance
        based on the request parameters, and sends a response back.

        Args:
            request (svc_pb2.PropagateWithdrawRequest): The request containing
                parameters for withdrawal propagation.
            context: The gRPC context.

        Returns:
            svc_pb2.PropagateWithdrawResponse: The response to the withdrawal
            propagation request.

        Example:
            response = branch.Propagate_Withdraw(request, context)
        """
        self.recvMsg.append(request)
        # Propagate withdraw operation to other Branches to attain consistent balance
        for stubs in self.stubList:
            # Do not decrement the balance from the current branch as that is already done
            if stubs == self.stub:
                continue
            new_request = svc_pb2.WithdrawRequest(
                customer_id=None, amount=request.amount
            )
            # Run the withdraw operation on the other branches
            stubs.Withdraw(new_request)
            response = svc_pb2.Response()
            response.message = constants.SUCCESS
        return response

    def Propagate_Deposit(self, request, context):
        """
        Process a deposit propagation request between branches.

        This method is called to process a deposit propagation request from one
        branch to another. It handles the request, increases the branch's balance
        based on the request parameters, and sends a response back.

        Args:
            request (svc_pb2.PropagateDepositRequest): The request containing
                parameters for deposit propagation.
            context: The gRPC context.

        Returns:
            svc_pb2.PropagateDepositResponse: The response to the deposit
            propagation request.

        Example:
            response = branch.Propagate_Deposit(request, context)
        """
        self.recvMsg.append(request)
        # Propagate deposit operation to other Branches to attain consistent balance
        for stubs in self.stubList:
            # Do not increment the balance from the current branch as that is already done
            if stubs == self.stub:
                continue
            new_request = svc_pb2.DepositRequest(
                customer_id=None, amount=request.amount
            )
            # Run the deposit operation on the other branches
            stubs.Deposit(new_request)
            response = svc_pb2.Response()
            response.message = constants.SUCCESS
        return response
