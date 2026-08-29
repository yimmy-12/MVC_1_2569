class Member:
    def __init__(self, member_id: str, name: str, role: str, active: bool = True):
        self.id = member_id
        self.name = name
        self.role = role
        self.active = active