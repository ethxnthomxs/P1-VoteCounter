import csv
from typing import Dict, Set

VOTE_FILE = 'votes.csv'

def load_votes() -> Dict[str, int]:
    """Load vote counts from the CSV file."""
    votes = {'John': 0, 'Jane': 0}
    try:
        with open(VOTE_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    _, candidate = row
                    if candidate in votes:
                        votes[candidate] += 1
    except FileNotFoundError:
        pass
    return votes

def load_voters() -> Set[str]:
    """Load the set of user IDs who have voted."""
    voters = set()
    try:
        with open(VOTE_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    user_id, _ = row
                    voters.add(user_id)
    except FileNotFoundError:
        pass
    return voters

def save_vote(user_id: str, candidate: str) -> None:
    """Append a new vote to the CSV file."""
    with open(VOTE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, candidate])
