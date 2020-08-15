from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    source_name: str
    title: str
    link: str
    description: str
    updated_at: datetime

    def __repr__(self):
        return f"{self.source_name}: {self.title}"

    @property
    def search_words(self) -> set:
        words = self.source_name.split() + self.title.split() + self.description.split()
        lower_words = map(str.lower, words)
        return set(lower_words)

    def contains(self, words: set):
        return words.issubset(self.search_words)
