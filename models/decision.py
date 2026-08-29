class Decision:
    def __init__(self, request_id: str, member_id: str, result: str):
        self.request_id = request_id
        self.member_id = member_id
        self.result = result  # 'APPROVE' หรือ 'REJECT'