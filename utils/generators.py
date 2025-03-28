import random
import string


class Generators:

    # TODO: Implement date based getAlphaNum

    @staticmethod
    def getAlphaNum(size: int) -> str:
        return ''.join(
            random.SystemRandom()
                .choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            for _ in range(size)
        )
