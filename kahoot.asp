<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--<
        This line refreshes the entire html page each second
    meta http-equiv="refresh" content="1">-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100&display=swap" rel="stylesheet">

    <style>
        body {
            margin: 0;
            font-family: 'Roboto Mono', monospace;
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


</head>
<body>

    <section class="blue">
        <h1>The Wooster Voting Game</h1>
        <p>You ready to answer some questions?</p>
        <p style="text-align:center">Answer these questions correctly and see how many you get right! Compare your answers with other players!</p>
    </section>
    <div class="row">
        <div class="center">
            <img src="images/SilverBear.jpg" alt="SilverBear" style="width:75%">
        </div>
    </div>
    <div class="row">
      <div class="center">
      <!--<div class="column"><button id="Q2No">No</button>-->
        <button onclick="fakefunction4()" class="button">Silverback Gorilla</button>
        <button onclick="fakefunction5()" class="button"> Grizzly Bear</button>
        <!--<span id = "fakeResult2"></span>-->
      </div>
    </div>

    <div class="row">
        <div class="center">
            <img src="images/SilverBear.jpg" alt="SilverBear" style="width:75%">
        </div>
    </div>
    <div class="row">
      <div class="center">
      <!--<div class="column"><button id="Q2No">No</button>-->
        <button onclick="fakefunction4()" class="button">Silverback Gorilla</button>
        <button onclick="fakefunction5()" class="button"> Grizzly Bear</button>
        <!--<span id = "fakeResult2"></span>-->
      </div>
    </div>

    <div class="row">
        <div class="center">
            <img src="images/SilverBear.jpg" alt="SilverBear" style="width:75%">
        </div>
    </div>
    <div class="row">
      <div class="center">
      <!--<div class="column"><button id="Q2No">No</button>-->
        <button onclick="fakefunction4()" class="button">Silverback Gorilla</button>
        <button onclick="fakefunction5()" class="button"> Grizzly Bear</button>
        <!--<span id = "fakeResult2"></span>-->
      </div>
    </div>

    <div class="row">
        <div class="center">
            <img src="images/SilverBear.jpg" alt="SilverBear" style="width:75%">
        </div>
    </div>
    <div class="row">
      <div class="center">
      <!--<div class="column"><button id="Q2No">No</button>-->
        <button onclick="fakefunction4()" class="button">Silverback Gorilla</button>
        <button onclick="fakefunction5()" class="button"> Grizzly Bear</button>
        <!--<span id = "fakeResult2"></span>-->
      </div>
    </div>


</body>
</html>
