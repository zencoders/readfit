#Test file for crawler module

#import sys to append updater folder to search path
import sys
sys.path.append("../updater/")
import unittest
import re
from crawler import Crawler
#The following function is an example of function to supply to Crawler class
#this function caracterize the fetching policy of the Crawler class
def _reddit_fetch_function(tag,attr):
    if tag=="a":
       if 'href' in attr:
            if 'class' in attr:
                if re.search('title',attr['class']):
                    print "link with class=\"title\":",attr['href']
                    return attr['href']
    return ""

class CrawlerTestCase(unittest.TestCase):
    """Test class for the Crawler class"""
    def testCrawl(self):
        """This method tests the Crawler.crawl() method"""
        list_to_check=["http://pixel.redditmedia.com/click?id=t3_tijgd-programming&hash=b3db953f1e54a0ee2af2ca0ae4939e2dd0ca9640&url=http%3A%2F%2Fwww.startuphire.com%2F%3Futm_source%3Dreddit%26utm_medium%3Dbanner%26utm_campaign%3D2012_Launch%26utm_content%3Dprog","https://github.com/mroth/lolcommits","http://www.hanselman.com/blog/PleaseLearnToThinkAboutAbstractions.aspx","http://www.zopyx.de/blog/goodbye-mongodb","http://dijkstra.cs.virginia.edu/projects/readability/","http://www.gamedev.net/blog/355/entry-2254622-rapid-fire-debugging-thoughts/","https://docs.google.com/macros","http://dbmsmusings.blogspot.co.uk/2012/05/if-all-these-new-dbms-technologies-are.html","http://www.tomshardware.com/news/nvidia-nsight-ide-eclipse-visual-studio,15639.html","http://stackoverflow.com/tags/language-agnostic/info","http://www.kickstarter.com/projects/568774734/emacsy-an-embeddable-emacs","http://jeromyanglim.blogspot.com.au/2012/05/getting-started-with-r-markdown-knitr.html","http://michaelfeathers.typepad.com/michael_feathers_blog/2012/05/the-long-tail-of-technical-debt.html","http://www.slideshare.net/arungupta1/java-ee7-latest","http://indieambitions.com/idevblogaday/perlin-noise-gpu-gpuimage/","http://blog.jgc.org/2012/05/to-boldly-go-where-node-man-has-gone.html","http://weblogs.asp.net/jgalloway/archive/2012/05/16/why-i-taught-my-daughter-to-code-a-little.aspx#.T7QwY6Z7uTc.reddit","http://developer.amd.com/tools/CodeAnalyst/Pages/default.aspx","http://phpmaster.com/handling-collections-of-aggregate-roots/","http://garysieling.com/blog/building-a-website-scraper-using-chrome-and-node-js","http://en.nerdaholyc.com/memory-snipping-a-simple-example-in-assembly-codemerging-two-vectors/","http://jamesshore.com/Blog/Lessons-Learned-Lint-and-Javascript.html","http://openreplica.org/","http://programmers.stackexchange.com/questions/148978/what-is-the-connection-between-literate-programming-and-the-semantic-web","http://nuts.redsquirrel.com/post/23200685522/programming-as-a-foreign-language","http://www.xboxmb.com/forum/52-programming/111877-conjuguemos-auto-complete-script.html"]
        #Step 1 use this input as Crawler.crawl() input and save output in a variable
        crawler=Crawler("./CrawlingTestData/reddit_programming.html",_reddit_fetch_function)
        #Step 2 check if previous output list is equal to a manual manually defined one,list_to_check
        output=crawler.crawl()
        self.assertEqual(list_to_check,output) 
#def __main():
#    reddit_crawler=Crawler("http://www.reddit.com/r/programming",__reddit_fetch_function)
#    reddit_crawler.crawl()
if __name__ == "__main__":
    unittest.main()
