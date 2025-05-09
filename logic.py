from storage import load_votes, load_voters, save_vote

class VoteCounter:
    """
    Handles vote tallying logic and ensures users do not vote multiple times.
    Votes are persisted using a CSV file.
    """
    def __init__(self):
        self.votes = load_votes()
        self.voter_records = load_voters()

    def add_vote(self, user_id: str, candidate: str) -> str:
        """
        Add a vote for a candidate from a user ID.
        Returns a status message.
        """
        if user_id in self.voter_records:
            return "already_voted"

        if candidate in self.votes:
            self.votes[candidate] += 1
            self.voter_records.add(user_id)
            save_vote(user_id, candidate)
            return "success"
        else:
            return "invalid_candidate"

    def get_results(self) -> dict:
        """Return current vote counts."""
        return self.votes.copy()

    def has_voted(self, user_id: str) -> bool:
        """Check if a user has already voted."""
        return user_id in self.voter_records
