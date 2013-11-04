from facade import facade
from model.department import Department

def pagetop():
        return '''
         <!DOCTYPE html>
<html>
    <head>
        <STYLE type="text/css">
table {
    border-width: 1px; 
    border-style: solid; 
    border-color: black;
    border-collapse: collapse;
 }
td { 
    border-width: 1px;
    border-style: solid; 
    border-color: black;
    padding-left: 3px;
    padding-right: 3px;
    padding-top: 2px;
    padding-bottom: 2px;
 }
 th {
    border-width: 1px;
    border-style: solid; 
    border-color: black;
    font-weight: bold;
    padding-left: 3px;
    padding-right: 3px;
    padding-top: 2px;
    padding-bottom: 2px;
 }
        </STYLE>
        <title></title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="../base.css" media="all" />
        <link rel="stylesheet" type="text/css" href="../modele01.css" media="screen" />
    </head>
    <body>
        <div id="global">
            <div id="entete">
                <img STYLE="border: none;" src="../logo2.png" width="300" height="50"> 
                Data Mining using Python Project
            </div>
            <div id="centre">
                <div id="navigation">
                    <ol id="myol" start="1" type="1">
                        <li><a href = "../">Homepage</a></li>
                        <li><a href = "/Ranker/">Course Ranker</a></li>
                        
                    </ol>
                </div>
                <div id="contenu">'''

def pagebase():
        return '''
                </div>
            </div>
            <div id="pied">
                <p>Created by Pascal TIMSHEL (102848), Vladimir KROUPA (131509), Chloe CACHET (131316)</p>
                <br>
                <p><img STYLE="border: none;" src="../logo3.png" width="300" height="20"></p>
            </div>
        </div>
    </body>
</html>
        '''

def departments():
        list_dep = facade.list_departments()
        for dep in list_dep:
            yield '<option value="'+dep.name_en+'">'+dep.name_en+'</option>'
