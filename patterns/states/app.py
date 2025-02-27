from abc import ABC
from datetime import datetime
import json
from helper import Logger
from uuid import uuid4

from helper import InvalidStateTransition, TransactionStates


class TransactionState(ABC):  # Abstract interface for transactions
    def __init__(
        self, state_machine: "TransactionsStateMachine", state: TransactionStates
    ):
        self.state_machine = state_machine
        self.__state = state

    @property
    def internal_state(self):
        return self.__state

    def submit(self):
        raise InvalidStateTransition(
            f"Transaction cannot be Submitted. Transaction is Currently {self.internal_state.value}."
        )

    def approve(self):
        raise InvalidStateTransition(
            f"Transaction cannot be Approved. Transaction is Currently {self.internal_state.value}."
        )

    def activate(self):
        raise InvalidStateTransition(
            f"Payment cannot be Confirmed for the Transaction. Transaction is Currently {self.internal_state.value}."
        )

    def settle(self):
        raise InvalidStateTransition(
            f"Settlement cannot be Confirmed for the Transaction. Transaction is Currently {self.internal_state.value}."
        )

    def reject(self):
        raise InvalidStateTransition(
            f"Transaction cannot be Rejected. Transaction is Currently {self.internal_state.value}."
        )

    def cancel(self):
        raise InvalidStateTransition(
            f"Transaction cannot be Cancelled. Transaction is Currently {self.internal_state.value}."
        )


class DRAFT(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.DRAFT)

    def submit(self):
        if self.state_machine.state.internal_state != TransactionStates.DRAFT:
            super().submit()
            return False
        self.state_machine.state = SUBMITTED(self.state_machine)
        self.state_machine.log.info(
            f"{self.internal_state.value} Transaction Submitted."
        )
        return True


class SUBMITTED(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.SUBMITTED)

    def approve(self):
        if self.state_machine.state.internal_state != TransactionStates.SUBMITTED:
            super().approve()
            return False
        self.state_machine.state = APPROVED(self.state_machine)
        self.state_machine.log.info(
            f"{self.internal_state.value} Transaction Approved."
        )
        return True


class APPROVED(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.APPROVED)

    def activate(self):
        if self.state_machine.state.internal_state != TransactionStates.APPROVED:
            super().activate()
            return False
        self.state_machine.state = ACTIVE(self.state_machine)
        self.state_machine.log.info(
            f"{self.internal_state.value} Transaction Activated."
        )
        return True

    def reject(self, reason: str):
        if self.state_machine.state.internal_state != TransactionStates.ACTIVE:
            super().settle()
            return False
        self.state_machine.state = REJECTED(self.state_machine, reason)
        self.state_machine.log.info(
            f"{self.internal_state.value} Transaction Rejected."
        )
        return True


class ACTIVE(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.ACTIVE)

    def settle(self):
        if self.state_machine.state.internal_state != TransactionStates.ACTIVE:
            super().settle()
            return False

        self.state_machine.state = SETTLED(self.state_machine)
        self.state_machine.log.info(f"{self.internal_state.value} Transaction Settled.")
        return True

    def cancel(self):
        if self.state_machine.state.internal_state != TransactionStates.ACTIVE:
            super().settle()
            return False
        self.state_machine.state = CANCELLED(self.state_machine)
        self.state_machine.log.info(
            f"{self.internal_state.value} Transaction Cancelled."
        )
        return True


class SETTLED(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.SETTLED)


class REJECTED(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.REJECTED)


class CANCELLED(TransactionState):
    def __init__(self, state_machine: "TransactionsStateMachine"):
        super().__init__(state_machine, TransactionStates.CANCELLED)


class TransactionsStateMachine:  # A concrete transaction implementation
    def __init__(self, balance: float):
        self.__state = DRAFT(self)
        self.log = Logger()  # Use the logger
        self.__id = uuid4()
        self.__balance = balance
        self.__payments = []
        self.reason = None
        self.__credit = 0

    @property
    def transaction_id(self):
        return str(self.__id)

    @property
    def balance(self):
        return self.__balance

    @property
    def credit(self):
        return self.__credit

    @property
    def payments(self):
        return self.__payments

    def update_balances(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Invalid Balance.")
        if amount <= 0:
            raise ValueError("Invalid Value for Balance Change.")

        if self.__balance - amount > 0:
            self.__balance -= amount
        else:
            self.__credit = amount - self.__balance
            self.__balance = 0

        self.__payments.append(
            {
                "id": str(uuid4()),
                "transaction_id": self.transaction_id,
                "amount": float(amount),
                "timestamp": datetime.now().isoformat(),
                "status": self.__state.internal_state.value,
                "balance": float(self.__balance),
                "credit": float(self.__credit)
            }
        )

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: TransactionState):
        self.__state = state

    def submit(self):
        self.__state.submit()

    def approve(self):
        self.__state.approve()

    def activate(self):
        self.__state.activate()

    def settle(self, amount: float):
        if self.__balance <= 0:
            self.__state.settle()
        self.update_balances(amount)
        transaction.log.info(
            f"Transaction ID {transaction.transaction_id}: Balance Updated R{transaction.balance}."
        )

    def reject(self, reason: str):
        self.reason = reason
        self.__state.reject()

    def cancel(self, reason: str):
        self.reason = reason
        self.__state.cancel()


# Example Usage
transaction = TransactionsStateMachine(1000000)
transaction.log.info(
    f"Transaction ID {transaction.transaction_id}: {transaction.state.internal_state.value} State R{transaction.balance}."
)

transaction.submit()
transaction.approve()
transaction.activate()
transaction.settle(float(500000))
transaction.settle(float(500000))
transaction.settle(float(500000))
# try:
# except:
#     pass
transaction.log.info(
    f"Transaction {transaction.transaction_id}: {transaction.state.internal_state.value} State. Balance: {transaction.balance}. Repayments: {json.dumps(transaction.payments, indent=4)}"
)
