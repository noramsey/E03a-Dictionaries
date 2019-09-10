if __name__ == '__main__':

    birthday_log = {
      "Langston Hughes": "February 1, 1902", 
        "John Linell": "June 12, 1959",
        "Terry Pratchett": "April 28, 1948",
     "Vladimir Nabakov": "April 22, 1899",
     "Bernadette Peters": "February 28, 1948",
     "Dolly Parton": "Janurary 19, 1946",
       "Janelle Monae": "December 1, 1985",
      "Nalo Hopkinson": "December 20, 1960",
      "Tara Strong": "February 12, 1973",
        "Phil LaMarr": "Janurary 24, 1967"
}

    print('I know the birthdays of these people:')
    for name in birthday_log:
        print(name)

    print("\nWhose birthday do you want to know?")
    name = input()
    if name in birthday_log:
        print('{}\'s birthday is {}'.format(name, birthday_log[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))