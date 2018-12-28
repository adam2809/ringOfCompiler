//$(document).ready(function(){
    var code = document.getElementById('codemirror-textarea')//$("#codemirror-textarea");
    console.log(code)
    var editor = CodeMirror.fromTextArea(code, {

        lineNumbers : true,
        mode: "python"

    });
//});
