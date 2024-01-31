import random


class NameGenerator:
    @staticmethod
    def generate_name(prefix: str) -> str:
        # This is a placeholder for more complex name generation logic
        return f'{prefix}_{random.randint(1000, 9999)}'
