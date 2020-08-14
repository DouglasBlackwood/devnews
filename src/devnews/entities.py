from dataclasses import dataclass
from datetime import datetime


@dataclass
class FeedEntry:
    feed_name: str
    title: str
    link: str
    description: str
    updated_at: datetime

    def __repr__(self):
        return f"{self.feed_name}: {self.title}"
