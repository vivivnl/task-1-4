


import doctest


class Country:
    def __init__ (self, name, continent, capital, population, land_area) :
        self.name = name
        self.continent = continent
        self.population = population
        self.capital = capital
        self.land_area = land_area

    def calculate_population_density(self):
        return self.population / self.land_area
    
    def display_data(self):

        string = "Country name: {}, continent: {}, capital: {}, population: {}, land area: {} km^2, population density: {:.2f}/km^2"
        info = string.format(
            self.name,
            self.continent,
            self.capital,
            self.population,
            self.land_area,
            self.calculate_population_density(),
        )
        print(info)

if __name__ == "__main":
    doctest.testmod(verbose=False)
    c1 = Country("New Zealand", "Australasia", "Wellington", 4405200, 268700)
    c1.display_data()
    c2 = Country("China", "Asia", "Beihing", 1344130000, 9598000)
    c2.display_data()



