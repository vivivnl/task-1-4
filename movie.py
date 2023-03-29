class Movie:
    def __init__(self, title , writer, director, genre, cost, revenue):
        self.title = title
        self.writer = writer
        self.director = director
        self.genre = genre
        self.cost = cost
        self.revenue = revenue

    def display_data(self):
        info = "Move title: {}, Writer: {}, Director: {}, Genre: {}".format(
            self.title, self.writer, self.director, self.genre
        )
    
        print(info)
        profit = "Net profits:${}K".format(self.calculate_profit())
        print(profit)

    def calculate_profit(self) :
        return self.revenue - self.cost

# main routine
if __name__ == "__main__":
    m1 = Movie("zootopia", "Phil Johnston", "Rich Moore", "Animation", "150000000", "3410000000")
    m1.display_data()