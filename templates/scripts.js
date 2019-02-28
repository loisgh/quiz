function checkCorrect(){
    var correct = document.getElementById("correct").TEXT_NODE
    answer = document.querySelectorAll('input[type=radio]')
    for (i=0; i++; i < answer.length){
        if (answer[i].checked)
            if (answer[i].value == correct)
                alert("You got the answer right")
            else
                alert("Sorry Wrong Answer")
}
