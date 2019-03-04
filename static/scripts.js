        function checkCorrect() {
            var correct = getCorrect();
            var answer = getAnswer();
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

        function getCorrect() {
            return document.getElementById("correct").value.split(",");
        }
        function getAnswer() {
            return document.getElementsByClassName("radio-check");
        }
        function getAnswerAsString() {
            var answers = document.getElementsByClassName("radio-check");
            var ans = "";
            for (i = 0; i++; i < answers.length) {
                if (answers[i].checked == true) {
                    ans += answers[i].value;
                    ans += ",";
                }
            }
            return ans.substring(0, str.length - 1);
        }

