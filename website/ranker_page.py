import cherrypy
import functions
from storage.static_storage import StaticStorage
from ranker.course_ranker import CourseRanker
from facade import facade


class RankerPage:

    def courses(self, dep = None, level = None):
        courses_list = facade.course_ranking(dep, level)
        for course in courses_list:
            yield '<tr><td>'+course.code+'</td><td>'+course.title_en+'</td><td>'+str(course.department.name_en)+'</td><td></td></tr>'

    def index(self, num=None, dep=None, level=None):
        # Note the way we link to the extra links page (and back).
        request = cherrypy.request
        if request.method == 'POST':
            num = request.params['num']
            top = functions.pagetop()
            dep = request.params['dep']
            level = request.params['level']
            return top+'<h2>Courses corresponding to your research: </h2><table><th>Number</th><th>Course title</th><th>Department</th><th>Analysis</th>'+' '.join(list(self.courses(dep, level)))+'</table>'+ functions.pagebase()
        return functions.pagetop()+'''
                    <form method="POST" action = '/Ranker/'>

                        <h2>Course ranker function:</h2>

                            <label>Course Number: </label><input type="text" id="num" name="num">
                            <label> Departement: </label><select id="dep" name="dep"><option value=""></option>'''+str(list(functions.departments()))+'''</select>
                            <label> Level: </label><input type="radio" id="level" name="level" value="" checked>all
                                    <input type="radio" id="level" name="level" value="bsc">Bsc
                                    <input type="radio" id="level" name="level" value="ms">Master
                                    <input type="radio" id="level" name="level" value="phd">Phd
                        <p><input type="reset" value="Reset">
                            <input type="submit" value="Submit"></p>
                    </form>'''+functions.pagebase()

    index.exposed = True

