<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--<
        This line refreshes the entire html page each second
    meta http-equiv="refresh" content="1">
    
    -->
    <title>Kahoot!! </title>

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

        .wave {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            overflow: hidden;
            line-height: 0;
            transform: rotate(180deg);
        }

        .wave svg {
            position: relative;
            display: block;
            width: calc(100% + 1.3px);
            height: 150px;
        }

        .wave .shape-fill {
            fill: #202731;
        }
        * {
            box-sizing: border-box;
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
        <h1>Kahoot!!</h1>
        <p>Answer the damn questions</p>
    </section>
    <div class="row">
        <div class="column">
          <img src="images/panda.jpg" alt="panda" style="width:100%">
        </div>
        <div class="column">
          <img src="images/racoon.png" alt="racoon" style="width:113%">
        </div>
    </div>
    <div class="row">
        <div class="column"><button id="yes"> Yes </button>
        </div>
        <div class="column"><button id="no"> No </button>
        </div>
    </div>


</body>
</html>