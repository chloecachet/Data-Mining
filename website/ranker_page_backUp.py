import cherrypy
import functions
from storage.static_storage import StaticStorage
from model.department import Department
from ranker.course_ranker import CourseRanker
from facade import facade

class RankerPage:

    def departments(self):
        list_dep = facade.list_departments()
        for dep in list_dep:
            yield '<option value="'+dep.name_en+'">'+dep.name_en+'</option>'

    def courses(self, dep = None, level = None):
        courses_list = facade.course_ranking(dep, level)
        for course in courses_list:
            yield '<tr><td>'+course.code+'<td>'+course.title_en+'<td>'+str(course.department)+'</td>'

    def index(self, num=None, dep=None, level=None):
        # Note the way we link to the extra links page (and back).
        request = cherrypy.request
        if request.method == 'POST':
            num = request.params['num']
            top = functions.pagetop()
            dep = request.params['dep']
            level = request.params['level']
            return top+'<table>'+str(list(self.courses(dep, level)))+'</table>'+ functions.pagebase()
        return functions.pagetop()+'''
                    <form method="POST" action = '/Ranker/'>

                        <h2>Course ranker function:</h2>

                        <table>
                            <tr><td>Course Number:
                                <td><input type="text" id="num" name="num"></td>
                            <tr><td>Departement:                             
                                <td><select id="dep" name="dep"><option value=""></option>'''+str(list(self.departments()))+'''</select></td>
                            <tr><td>Level: 
                                <td><input type="radio" id="level" name="level" value="" checked>all
                                    <input type="radio" id="level" name="level" value="bsc">Bsc
                                    <input type="radio" id="level" name="level" value="ms">Master
                                    <input type="radio" id="level" name="level" value="phd">Phd</td>
                        </table>

                        <p><input type="reset" value="Reset">
                            <input type="submit" value="Submit"></p>
                    </form>'''+functions.pagebase()

    index.exposed = True

