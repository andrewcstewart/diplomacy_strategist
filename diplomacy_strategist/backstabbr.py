# -*- coding: utf-8 -*-

"""Backstabbr methods."""

import json
import pickle

def connect(browser='firefox', session=None):
  from seleniumrequests import Firefox
  driver = Firefox()
  driver.get("https://www.backstabbr.com/")

  # Restore previous session if specified
  if session:
    for cookie in pickle.load(open(session, "rb")):
      driver.add_cookie(cookie)

  return driver

class Backstabbr:
  """Backstabbr session instance"""

  def __init__(self):
    self.driver = connect()

  def save_session(self, path):
    pickle.dump(self.driver.get_cookies() , open("backstabbr.pkl","wb"))

  def get_game(self, game_id):
    for year in [1901, 1902, 1903, 1904, 1905, 1906, 1908, 1909]:
      for season in ['spring', 'fall', 'winter']:
        url = 'https://www.backstabbr.com/game/%s/%s/%s' % (game_id,year,season)
        response = self.driver.request('GET', url)
        yield parse_game_data(response.content)

  def get_sandbox(self, sandbox_id):
    url = ""
    response = self.driver.request('GET', url)
    return parse_sandbox_data(response.content)


def get_game_year(game_id):
    "https://www.backstabbr.com/game/6329975150477312/1901/spring"

def get_game_url(game_id, year, season):
  return 'https://www.backstabbr.com/game/%s/%s/%s' % (game_id,year,season)

def get_game_history(game_id):
  for year in [1901, 1902, 1903, 1904, 1905, 1906, 1908, 1909]:
      for season in ['spring', 'fall', 'winter']:
          url = 'https://www.backstabbr.com/game/%s/%s/%s' % (game_id,year,season)
          response = webdriver.request('GET', url)
          yield parse_game(response.content)

def parse_game_data(page_source):
  data = {}
  for line in page_source.splitlines():
    if line.strip().startswith("var"):
      parts = line.strip().split(' ', 3)
      if not parts[3].startswith('new'):
        rhs = parts[3].split(';')[0]
        data[parts[1]] = json.loads(rhs)
  return data

def parse_sandbox_data()
  data = {}
  for line in page_source.splitlines():
    if line.strip().startswith("var"):
      parts = line.strip().split(' ', 3)
      if not parts[3].startswith('new'):
        rhs = parts[3].split(';')[0]
        data[parts[1]] = json.loads(rhs)
  return data