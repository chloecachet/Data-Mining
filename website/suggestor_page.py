import cherrypy
import functions

class SuggestorPage:
    def index(self,num=None):
        # Note the relative link back to the Links page!
        request = cherrypy.request
        if request.method == 'POST':
            top = functions.pagetop()
            return top+'''
           
            blah blah blah ceci est le resultat suggestor!!!'''+ functions.pagebase()
        return functions.pagetop()+'''<form method="POST" action = '/Suggestor/'>

                        <h2>Course suggestor function:</h2>

                            <label>Course Number: </label>
                                <input type="text" id="num" name="num">
                            <label> Departement: </label>                             
                                <select id="dep" name="dep"><option value=""></option>'''+str(list(functions.departments()))+'''</select>
                            <label> Level: </label> 
                                <input type="radio" id="level" name="level" value="" checked>all
                                    <input type="radio" id="level" name="level" value="bsc">Bsc
                                    <input type="radio" id="level" name="level" value="ms">Master
                                    <input type="radio" id="level" name="level" value="phd">Phd

                        <p><input type="reset" value="Reset">
                            <input type="submit" value="Submit"></p>
                    </form>'''+functions.pagebase()
    index.exposed = True
