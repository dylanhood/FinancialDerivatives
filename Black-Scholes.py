import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
df.to_csv('data.csv', index=False)

class OptionPricing:

    def __init__(self, S0, E, T, rf, sigma, iterations):
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iterations = iterations

        def call_option_simulation(self):
            # we have two columns: the first with 0s and the second will store the payoff
            # I believe we'll need the first column of 0s: payoff function is max(0,S-E) for call option
            option_data = np.zereos([self.iterations, 2])

            #dimensions: 1 dimensional array with as many items as the iterations
            rand = np.random.normal(0, 1, [1, self.iterations])

            #equations for the S(t) stock price at T
            stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2)
                                            + self.sigma * np.sqrt(self.T) * rand)

            # also we need S-E because we have to calculate the max(S-E,0)
            option_data[:,1] = stock_price - self.E

            #average for the Monte-Carlo simulation
            #max() returns the max(0,S-E) according to the formula
            # This is the average value
            average = np.sum(np.amax(option_data, axis=1)) / float.astype('float16')(self.iterations)

            # need to use the exp(-rT) discount factor
            return np.exp(-1.0*self.rf*self.T)*average

        # Put Option (I don't think it's needed but I felt compelled to include it

        def put_option_simulation(self):
            # so because we have two columns: the first with 0s and the second will store the payoff
            # I believe we'll need the first column of 0s: payoff function is max(0,S-E) for call option
            option_data = np.zereos([self.iterations, 2])

            # dimensions: 1 dimensional array with as many items as the iterations
            rand = np.random.normal(0, 1, [1, self.iterations])

            # equations for the S(t) stock price at T
            stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2)
                                           + self.sigma * np.sqrt(self.T) * rand)

            # also we need S-E because we have to calculate the max(E-S,0)
            option_data[:, 1] = self.E - stock_price

            # average for the Monte-Carlo simulation
            # max() returns the max(0,S-E) according to the formula
            # This is the average value
            average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

            # need to use the exp(-rT) discount factor
            return np.exp(-1.0*self.rf*self.T)*average

if __name__ == '__main__':
    option = OptionPricing(100, 100, 1, 0.05, 0.2, 1000)
    print('Value of the call option is $%.2f' % model.call_option_simulation())
    print('Value of the put option is $%.2f' % model.put_option_simulation())
