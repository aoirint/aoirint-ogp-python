from typing import Optional, Dict, List
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

def get_ogp(url: str) -> Dict[str, List[str]]:
  headers = {
    'User-Agent': 'facebookexternalhit/1.1; aoirint-ogp-python/0.0.0',
  }

  res = requests.get(url, headers=headers)

  html = res.text
  bs = BeautifulSoup(html, 'html5lib')

  ogp_dict = {}
  for meta_tag in bs.select('meta'):
    prop = meta_tag.get('property')
    content = meta_tag.get('content')

    if prop is None:
      continue

    if prop not in ogp_dict:
      ogp_dict[prop] = []

    ogp_dict[prop].append(content)

  return ogp_dict


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('url', type=str)
  args = parser.parse_args()

  url = args.url

  print(get_ogp(url))

