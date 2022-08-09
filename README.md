# congress-letterbank
Inspired by Election Profit Makers #158, how many historical congressperson last names share a letterbank with their state's capital.

Pulls data from https://github.com/unitedstates/congress-legislators and http://goodcsv.com/wp-content/uploads/2020/08/us-states-territories.csv. 

## Build and Execution
```bash
$ pipenv install
$ pipenv run python src/data_wrangler.py
Getting state capitals...
parsing...
Getting historical legislators...
parsing...
Getting current legislators...
parsing...
Iterating over all 12593 past and present legislators...
MATCHES FOUND!
JosiahTattnall was elected to to the great state of GA (capital Atlanta) on 1796-01-01
EdwardTattnall was elected to to the great state of GA (capital Atlanta) on 1821-12-03
JamesRichmond was elected to to the great state of VA (capital Richmond) on 1879-03-18
RichardCheney was elected to to the great state of WY (capital Cheyenne) on 1979-01-15
LizCheney was elected to to the great state of WY (capital Cheyenne) on 2017-01-03
```

## TODO/Needed
- State capitals change over time! What was the capital of the legislator's home state AT THE TIME THEY WERE ELECTED!
- Unit tests
- Refactor some of the plumbing into separate modules