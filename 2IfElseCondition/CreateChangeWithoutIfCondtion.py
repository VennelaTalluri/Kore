print('Enter amount')
amount = int(input())

print('Amount is %d 1 bucks, %d 2 bucks, %d 5 bucks, %d 10 bucks, %d 20 bucks, %d 50 bucks, %d 100 bucks, %d 500 bucks' % ((((((((amount % 500) % 100) % 50) % 20) % 10) % 5) % 2) / 1,
                                                                                                                        ((((((amount % 500) % 100) % 50) % 20) % 10) % 5) / 2,
                                                                                                                        (((((amount % 500) % 100) % 50) % 20) % 10) / 5,
                                                                                                                        ((((amount % 500) % 100) % 50) % 20) / 10,
                                                                                                                        (((amount % 500) % 100) % 50) / 20,
                                                                                                                        ((amount % 500) % 100) / 50,
                                                                                                                        (amount % 500) / 100,
                                                                                                                        (amount / 500)))