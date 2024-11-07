
class Film:
    def __init__(self, rating, name, ears, director, genre):
        self.rating = rating
        self.name = name
        self.ears = ears
        self.director = director
        self.genre = genre

    def __str__(self):
        return (f"Рейтинг: {self.rating}\n"
                f"Название: {self.name}\n"
                f"Год: {self.ears}\n"
                f"Режиссёр: {self.director}\n"
                f"Жанр: {self.genre}")

