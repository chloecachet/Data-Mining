import cherrypy
import functions

class QualifierPage:
    def index(self, num=None):
        # Note the relative link back to the Links page!
        request = cherrypy.request
        if request.method == 'POST':
            top = functions.pagetop()
            return top+'''
           
            blah blah blah ceci est le resultat qualifier!!!'''+ functions.pagebase()
        return functions.pagetop()+'''<form method="POST" action = '/Qualifier/'>

                        <h2>Course qualifier function:</h2>
                            <label> Course Number: </label>
                                <input type="text" name="num">

                        <p><input type="reset" value="Reset">
                            <input type="submit" value="Submit"></p>
                    </form>'''+functions.pagebase()
    index.exposed = True
