créez un nouveau fichier de Build System et enregistrez-le sous. Le dossier doit contenir :..\Packages\User\SublimeREPL-python.sublime-build
{
    "target": "run_existing_window_command", 
    "id": "repl_python_run",
    "file": "config/Python/Main.sublime-menu"
}
Puis allez dans l’onglet fichier de Python et sélectionnez Outils > Build System > SublimeREPL-python. Maintenant, + doit exécuter le fichier Python actuel, avec la sortie dans un nouvel onglet. Si vous utilisez une disposition à deux colonnes, la sortie REPL devrait ouvrir dans la deuxième colonne. (Il utilisait Sublime texte 3).CtrlB

SublimeREPL\config\Python\Main.sublime-menu
Trouver la partie qui contient :.idrepl_python_run
Moins, ajouter. C’est tout.args/cmd-i
Pour référence, mine ressemble à ce qui suit :
{"command": "repl_open",
 "caption": "Python - RUN current file",
 "id": "repl_python_run",
 "mnemonic": "d",
 "args": {
     "type": "subprocess",
     "encoding": "utf8",
     "cmd": ["C:/Python34/python", "-u", "-i", "$file_basename"],
     "cwd": "$file_path",
     "syntax": "Packages/Python/Python.tmLanguage",
     "external_id": "python",
     "extend_env": {"PYTHONIOENCODING": "utf-8"}
 }
}