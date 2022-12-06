from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <a href = "https://ria.ru/20150611/1069025484.html"><h1>Жак-Ив Кусто́</h1></a>
    <img src="https://www.rgo.ru/sites/default/files/styles/head_image_article/public/1034295-e1477344635669-1.jpg?itok=4U4Dw9en" />
    <strong><p>Жак-Ив Кусто́ — французский исследователь Мирового океана,</strong><br> 
    фотограф, режиссёр, изобретатель, автор множества книг и фильмов.</p>
    <p>Являлся членом Французской академии. Командор ордена Почётного легиона.<br>
     Известен как Капитан Кусто. Совместно с Эмилем Ганьяном в 1943 году разработал и испытал акваланг.</p>
    """
    return page_content


app.run()

