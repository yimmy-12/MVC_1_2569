from repositories.request_repository import RequestRepository
from models.decision import Decision

class RequestController:
    def __init__(self, repo: RequestRepository):
        self.repo = repo

    def create_request(self, requester_id: str, target_id: str, new_role: str):
        if requester_id == target_id:
            return False, "ปฏิเสธ: ผู้เสนอไม่สามารถเป็นสมาชิกเป้าหมายของคำขอตนเองได้"

        for req in self.repo.get_all_requests():
            if req.target_id == target_id and req.status == "PENDING":
                return False, "ปฏิเสธ: สมาชิกเป้าหมายมีคำขอที่ยังรอพิจารณาอยู่แล้ว"

        req = self.repo.add_request(requester_id, target_id, new_role)
        return True, f"สร้างคำขอสำเร็จ ID: {req.id}"


    def vote_request(self, request_id: str, voter_id: str, result: str):
        req = self.repo.get_request(request_id)
        if not req:
            return False, "ปฏิเสธ: ไม่พบคำขอ"

        if req.status != "PENDING":
            return False, "ปฏิเสธ: คำขอนี้สิ้นสุดแล้ว ไม่สามารถลงความเห็นได้"

        if voter_id in (req.requester_id, req.target_id):
            return False, "ปฏิเสธ: ผู้เสนอหรือสมาชิกเป้าหมายไม่มีสิทธิ์ลงความเห็น"

        voter = self.repo.get_member(voter_id)
        if not voter or not voter.active:
            return False, "ปฏิเสธ: เฉพาะสมาชิกสถานะ Active เท่านั้นที่มีสิทธิ์"

        if any(d.member_id == voter_id for d in req.decisions):
            return False, "ปฏิเสธ: สมาชิกเคยลงความเห็นต่อคำขอนี้ไปแล้ว"

        req.decisions.append(Decision(request_id, voter_id, result))

        # Ckeck
        if req.approve_count >= 2:
            req.status = "APPROVED"
            target_member = self.repo.get_member(req.target_id)
            if target_member:
                target_member.role = req.new_role
            return True, "ลงความเห็นสำเร็จ: คำขออนุมัติ และเปลี่ยนบทบาทสมาชิกเรียบร้อย"

        elif req.reject_count >= 2:
            req.status = "REJECTED"
            return True, "ลงความเห็นสำเร็จ: คำขอไม่อนุมัติ"

        return True, "ลงความเห็นสำเร็จ"

    def cancel_request(self, request_id: str, requester_id: str):
        req = self.repo.get_request(request_id)
        if not req:
            return False, "ปฏิเสธ: ไม่พบคำขอ"

        if req.requester_id != requester_id:
            return False, "ปฏิเสธ: เฉพาะผู้เสนอเท่านั้นที่สามารถยกเลิกคำขอได้"

        if req.status != "PENDING":
            return False, "ปฏิเสธ: คำขอนี้ไม่ได้อยู่ในสถานะรอพิจารณา"

        if len(req.decisions) > 0:
            return False, "ปฏิเสธ: ไม่สามารถยกเลิกได้เนื่องจากมีสมาชิกลงความเห็นแล้ว"

        req.status = "CANCELLED"
        return True, "ยกเลิกคำขอสำเร็จ"