<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="preconnect" href="https://fonts.googleapis.com"> 
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet">

    <style>
        body {
            margin: 0;
            font-family: 'Lato', sans-serif;
            color: white;
            background: #202731;
        }

        section{
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 50px;
            padding: 100px 20vw;
        }

        .blue {background: #4682b4;}
        .red {background: indianred;}
        .green {background: seagreen;}
        .dark {background: slategray;}

        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            text-align:center;
            padding: 5px;
        }

        .button {
            background-color: #4caf50; /* Green */
            border: none;
            border-radius:10px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
        }

        .button:hover {
            background-color:#235324;
            transition: 0.2s;
        }

        .button:active {
            background-color: #143115;
        }

        .column {
            float: left;
            width: 33.33%;
            padding: 5px;
        }

        /* Clearfix (clear floats) */
        .row::after {
            content: "";
            clear: both;
            display: table;
        }

    </style>

    <script>
    var currentQuestion = 1;
    var userId = 0;
    function UpdateQuestion(data){
        let test = JSON.parse(data);
        console.log(test);
        document.getElementById("question_image").src = test['image'];
        document.getElementById("Option1Text").innerHTML = test['option1'];
        document.getElementById("Option1").value = test['option1'];
        document.getElementById("Option2Text").innerHTML = test['option2'];
        document.getElementById("Option2").value = test['option2'];
        document.getElementById("Option1").checked = false;
        document.getElementById("Option2").checked = false;
    }

    $(document).ready(function(){
        $.get("RegisterUser", null, function(data, status){
          let temp = JSON.parse(data);
          userId = temp['user_id'];
        })

        $.post("getQuestionsById",
                JSON.stringify({question_id: currentQuestion})
                , function(data, status) {
                    UpdateQuestion(data);
                }); 
                
        $("#PrevQ").click(function(){
                currentQuestion = currentQuestion - 1;
                if(currentQuestion < 1){
                    currentQuestion = 1;
                }
                $.post("getQuestionsById",
                JSON.stringify({question_id: currentQuestion})
                , function(data, status) {
                  UpdateQuestion(data);
                });
            });

            $("#NextQ").click(function(){
                currentQuestion = currentQuestion + 1;
                if(currentQuestion > 4){
                    currentQuestion = 4;
                }
                $.post("getQuestionsById",
                JSON.stringify({question_id: currentQuestion})
                , function(data, status) {
                  UpdateQuestion(data);
                });
            });

            $("#Option1").click(function(){
              console.log(userId)
              $.post("acceptAnswer",
                JSON.stringify({question_id: currentQuestion, answer: $("#Option1").val(), user_id: userId})
                , function(data, status) {
                    console.log(data);
                }); 
            });

            $("#Option2").click(function(){
              console.log(userId)
              $.post("acceptAnswer",
                JSON.stringify({question_id: currentQuestion, answer: $("#Option2").val(), user_id: userId})
                , function(data, status) {
                    console.log(data);
                }); 
            });
    }); 
    
    

    </script>

</head>
<body>

    <section class="blue">
        <h1>The Wooster Voting Game</h1>
        <p>You ready to answer some questions?</p>
        <p style="text-align:center">Answer these questions correctly and see how many you get right! Compare your answers with other players!</p>
    </section>
    <button id="PrevQ">Previous Question</button>
    <button id="NextQ">Next Question</button>
    <div class="question_wrap">
        <div class="center">
            <img id="question_image" style="width: 75%"/>
        </div>
        <div class="row center">
            <input type="radio" id="Option1">
            <label id="Option1Text">Yes</label> <br />
            <input type="radio" id="Option2">
            <label id="Option2Text">No</label> <br />
        </div>
    </div>

</body>
</html>
