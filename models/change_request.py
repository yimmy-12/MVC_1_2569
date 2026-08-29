from typing import List
from models.decision import Decision

class ChangeRequest:
    def __init__(self, request_id: str, requester_id: str, target_id: str, new_role: str, status: str = "PENDING"):
        self.id = request_id
        self.requester_id = requester_id
        self.target_id = target_id
        self.new_role = new_role
        self.status = status  # 'PENDING', 'APPROVED', 'REJECTED', 'CANCELLED'
        self.decisions: List[Decision] = []

    @property
    def approve_count(self) -> int:
        return sum(1 for d in self.decisions if d.result == "APPROVE")

    @property
    def reject_count(self) -> int:
        return sum(1 for d in self.decisions if d.result == "REJECT")