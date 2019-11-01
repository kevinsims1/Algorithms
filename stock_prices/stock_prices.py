#!/usr/bin/python

import argparse

# def find_max_profit(prices):
#   maximum = prices[1] - prices[0]
#   for i in range(0, len(prices) - 1): 
#     for k in range(i + 1, len(prices) - 1):
#       if prices[k] - prices[i] > maximum:
#         maximum = (prices[k] - prices[i])
#         # print(prices[i], 'i')
#         # print(prices[k], 'k')
#         # print(maximum)
#   return maximum

def find_max_profit(prices):
  lowestBuy = prices[0]
  maximum = prices[1] - lowestBuy
  for i in range(1, len(prices) - 1):
    if prices[i] - lowestBuy > maximum:
      maximum = (prices[i] - lowestBuy)
    if prices[i] < lowestBuy:
      lowestBuy = prices[i]
  return maximum


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))