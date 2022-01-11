import enum


class RoleType(enum.Enum):
    unknown = "Unknown"
    bulgargaz = "Bulgargaz"
    energo_pro = "Energo-pro"
    data_entry = "data_entry"
    data_analyst = "data_analyst"
    accountant = "accountant"
    ceo = "CEO"


class State(enum.Enum):
    rejected = "Rejected"
    pending = "Pending"
    approved = "Approved"
