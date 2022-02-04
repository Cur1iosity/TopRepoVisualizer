# TopRepoVisualiser script


This python script was written for simple purpose -- to visualise top-rated GitHub repositories in a barchart by keyword.
For me it is just a fast and simple way to find the most popular resource on GitHub.

Installation:
`pip install requests, pyplot`

Help:
`python TopRepoVisualiser.py --help`

```
usage: TopRepoVisualiser.py [-h] -k KEYWORD [-s] [-l LIMIT] [-o OUTPUT]

This script creating barchart with the most popular Git repositories found by
keyword

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        Keyword that you would like to search
  -s, --show            show list with repositories info
  -l LIMIT, --limit LIMIT
                        Searching result limit (default: 30)
  -o OUTPUT, --output OUTPUT
                        output list with repo and urls into provided file
```

Usage example:
`python TopRepoVisualiser.py --keyword anime --limit 5`

Result:
![Result](Example.png)
