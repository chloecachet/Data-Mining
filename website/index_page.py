import functions

class Index:
    def index(self):
        return functions.pagetop()+'''<h2>Welcome to our python project's website</h2>
        This project was made by Pascal Timshel, Vladimir Kroupa and Chloe Cachet.
        <h2>Project Description</h2>
        Our subject is Course Mining: using DTU's courses catalog we will provide a web interface
        to help students choose their courses.
        '''+functions.pagebase()
    index.exposed = True