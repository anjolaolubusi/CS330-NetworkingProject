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

      table{
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }

      td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }

  </style>

  <script>

    $(document).ready(function(){
      $.get("GetTally", null, function(data, status){
        let temp = JSON.parse(data);
        console.log(data);
        console.log(temp);
        console.log(temp[1]);
        // console.log(data["1"])
        // document.getElementById("resulttable").innerHTML = temp;
        // document.getElementById("Question 1").innerHTML = "Question 1";

        // Question 1
        document.getElementById("Grizzly").innerHTML = Object.keys(temp[1])[0] + " - " + temp[1][Object.keys(temp[1])[0]];
        document.getElementById("Silverback").innerHTML = Object.keys(temp[1])[1] + " - " + temp[1][Object.keys(temp[1])[1]];

        // Question 2
        document.getElementById("2000").innerHTML = Object.keys(temp[2])[0] + " - " + temp[2][Object.keys(temp[2])[0]];
        document.getElementById("1000").innerHTML = Object.keys(temp[2])[1] + " - " + temp[2][Object.keys(temp[2])[1]];

        // Question 3
        document.getElementById("Yes").innerHTML = Object.keys(temp[3])[0] + " - " + temp[3][Object.keys(temp[3])[0]];
        document.getElementById("No").innerHTML = Object.keys(temp[3])[1] + " - " + temp[3][Object.keys(temp[3])[1]];

        // Question 4
        document.getElementById("Good").innerHTML = Object.keys(temp[4])[0] + " - " + temp[4][Object.keys(temp[4])[0]];
        document.getElementById("Bad").innerHTML = Object.keys(temp[4])[1] + " - " + temp[4][Object.keys(temp[4])[1]];

        // document.getElementById("test2").innerHTML = JSON.stringify(data);
        // console.log("hi");
        // console.log("bye");
      });
    });
  </script>

</head>

<body>

  <div class="Results">
    <div style="center">
      <!-- <p id="resulttable"></p> -->
      <p id="test1"></p>
      <p id="test2"></p>

      <table>
        <tr>
          <th>Question</th>
          <th>Option 1</th>
          <th>Option 2</th>
        </tr>
        <tr>
          <th id="Question 1">Who Wins:</th>
          <th id="Grizzly"></th>
          <th id="Silverback"></th>
        </tr>
        <tr>
          <th id="Question 2">How Many Students Does Wooster Have?</th>
          <th id="2000"></th>
          <th id="1000"></th>
        </tr>
        <tr>
          <th id="Question 3">Are Bananas Berries?</th>
          <th id="Yes"></th>
          <th id="No"></th>
        </tr>
        <tr>
          <th id="Question 4">Which Do You Want To Hear First?</th>
          <th id="Good"></th>
          <th id="Bad"></th>
        </tr>



    </div>
    <!-- </div> -->

</body>
</html>
