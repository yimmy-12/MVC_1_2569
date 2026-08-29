from typing import Dict, List
from models.member import Member
from models.change_request import ChangeRequest
from models.decision import Decision

class RequestRepository:
    def __init__(self):
        self.members: Dict[str, Member] = {}
        self.requests: Dict[str, ChangeRequest] = {}
        self.auto_id = 5
        self._seed_data()

    def _seed_data(self):
        self.members = {
            "M01": Member("M01", "คุยกันได้", "PRODUCER", True),
            "M02": Member("M02", "ใบเสร็จอยู่ไหน", "FINANCE", True),
            "M03": Member("M03", "ตัดคลิปก่อน", "EDITOR", True),
            "M04": Member("M04", "เพื่อนกันตลอดไป", "CREATOR", True),
            "M05": Member("M05", "อ่านแชตย้อนหลัง", "CREATOR", True),
        }
        self.requests = {
            "C01": ChangeRequest("C01", "M01", "M02", "EDITOR", "PENDING"),
            "C02": ChangeRequest("C02", "M02", "M03", "CREATOR", "PENDING"),
            "C03": ChangeRequest("C03", "M03", "M04", "EDITOR", "PENDING"),
            "C04": ChangeRequest("C04", "M04", "M05", "PRODUCER", "PENDING"),
        }

        # Current
        self.requests["C01"].decisions.append(Decision("C01", "M03", "APPROVE"))
        self.requests["C02"].decisions.append(Decision("C02", "M04", "REJECT"))
        self.requests["C04"].decisions.append(Decision("C04", "M01", "APPROVE"))

    def get_all_members(self) -> List[Member]:
        return list(self.members.values())

    def get_all_requests(self) -> List[ChangeRequest]:
        return list(self.requests.values())

    def get_member(self, member_id: str) -> Member:
        return self.members.get(member_id)

    def get_request(self, request_id: str) -> ChangeRequest:
        return self.requests.get(request_id)

    def add_request(self, requester_id: str, target_id: str, new_role: str) -> ChangeRequest:
        new_id = f"C{self.auto_id:02d}"
        self.auto_id += 1
        req = ChangeRequest(new_id, requester_id, target_id, new_role, "PENDING")
        self.requests[new_id] = req
        return req