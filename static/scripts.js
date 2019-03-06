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
        function submit() {
            checkCorrect();
            httpGetAsync();

        }
        function getCategory() {
            return category = document.getElementById("category").value;
        }
        function getOrder() {
            return document.getElementById("order").value;
        }

        function getCorrect() {
            return document.getElementById("correct").value.replace(/,/g,'|');
        }
        function getAnswer() {
            return document.getElementsByClassName("radio-check");
        }
        function getAnswerAsString() {
            var answers = document.getElementsByClassName("radio-check");
            var ans = "";
            for (i = 0; i < answers.length; i++) {
                if (answers[i].checked == true) {
                    ans += answers[i].value;
                    ans += "|";
                }
            }
            return ans.substring(0, ans.length - 1);
        }

        function httpGetAsync()
        {
            var url = "/score_questions?" +
                "&order=" + getOrder() +
                "&answer=" + getAnswerAsString() +
                "&category=" + getCategory() +
                "&correct=" + getCorrect()

            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                    return(xmlHttp.responseText);
            }
            xmlHttp.open("GET", url, true); // true for asynchronous
            xmlHttp.send(null);
        }

