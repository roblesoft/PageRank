from crawler import crawler
from pageRank import pageRank

def main():
    world_wide_web = crawler()
    pagerank = pageRank(world_wide_web)
    for rank in pagerank:
        print(rank)

if __name__ == '__main__':
    main()