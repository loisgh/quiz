        function checkCorrect() {
            var correct = document.getElementById("correct").value.split(",")
            var answer = document.getElementsByClassName("radio-check");
            for (i = 0; i < answer.length; i++) {
                if (correct.includes(answer[i].value)) {
                    document.getElementsByTagName("li")[i].style.backgroundColor = "green";
                    }
                if (answer[i].checked == true) {
                    if (correct.includes(answer[i].value)) {
                        ;
                    }else{
                        document.getElementsByTagName("li")[i].style.backgroundColor = "red";
                    }
                }
            }
        }
