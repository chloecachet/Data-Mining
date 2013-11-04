"""
Course mining web page generator.
"""

import cherrypy
import os.path
from index_page import Index
from ranker_page import RankerPage
from suggestor_page import SuggestorPage
from qualifier_page import QualifierPage



# Of course we can also mount request handler objects right here!
root = Index()
root.Ranker = RankerPage()
root.Qualifier = QualifierPage()
root.Suggestor = SuggestorPage()

conf = os.path.join(os.path.dirname(__file__), 'conf.conf')
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(root, config=conf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(root, config=conf)

