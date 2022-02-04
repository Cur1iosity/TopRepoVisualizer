class Repo():
    """Репозитории"""

    def __init__(self, name, owner, stars, repository, created, updated, description):
        self.name = name
        self.owner = owner
        self.stars = stars
        self.repository = repository
        self.created = created
        self.updated = updated
        self.description = description

    def print_summary(self):
        print(f"Name: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Stars: {self.stars}")
        print(f"Repository: {self.repository}")
        print(f"Created: {self.created}")
        print(f"Updated: {self.updated}")
        print(f"Description: {self.description}")
        return True

    def get_attributes(self):
        return {attribute.capitalize(): value for attribute, value in self.__dict__.items()}
