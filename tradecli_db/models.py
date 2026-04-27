from uuid import UUID
from dataclasses import dataclass, field

@dataclass
class TradeRecord:
    id: UUID
    variables: dict[str, list[float]] = field(default_factory=dict)
