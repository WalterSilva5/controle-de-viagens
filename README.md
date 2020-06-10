<h1> SISTEMA DE CONTROLE DE FLUXO DE VIAGENS </h1>
----------- estrutura do projeto -----------
<pre>
project/
    mvc_app.py              # main application with App class
    mvc_app_rc.py           # auto-generated resources file (using pyrcc.exe or equivalent)
    controllers/
        main_ctrl.py        # main controller with MainController class
        other_ctrl.py
    model/
        model.py            # model with Model class
    resources/
        mvc_app.qrc         # Qt resources file
        main_view.ui        # Qt designer files
        other_view.ui
        img/
            icon.png
    views/
        main_view.py        # main view with MainView class
        main_view_ui.py     # auto-generated ui file (using pyuic.exe or equivalent)
        other_view.py
        other_view_ui.py
</pre>
--------------------------------------------
