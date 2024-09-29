from duckduckgo_search import DDGS

def dictParser(result):
  for key, value in result.items():
    print(f"{key}: {value}")
  return result['href']





def SearchCode(searchterm):
    results = DDGS().text(searchterm, max_results=2)
    totalUrsl = []
    for result in results:
        totalUrsl.append(dictParser(result))
    return totalUrsl

