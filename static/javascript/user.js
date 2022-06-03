      let request = null;
      function getCorrectAns() {
        console.log("in process function");
        request = new XMLHttpRequest();
        request.onreadystatechange = getCorrectAnsResults;
        request.open("GET", "/api", true);
        request.send(null);
      }
      function getCorrectAnsResults() {
        if (request.readyState == 4) {
          var response = JSON.parse(request.responseText);
          console.log(typeof response);
          console.log(response);
          correctanslist = [];

          for (obj of response) {
            correctanslist.push(obj["fields"]["corrans"]);
          }
          console.log("size :" + correctanslist.length);
          useranslist = [];
          for (let i = 1; i <= correctanslist.length; i++) {
            if (document.getElementById(String(i) + "option1").checked) {
              useranslist.push(
                document.getElementById(String(i) + "option1").value
              );
            } else if (document.getElementById(String(i) + "option2").checked) {
              useranslist.push(
                document.getElementById(String(i) + "option2").value
              );
            }
          }
          let request2 = new XMLHttpRequest();
           request2.onreadystatechange = function () {
            if (request2.readyState == 4) {
              let obj = JSON.parse(request2.responseText);
              console.log(obj.score + "," + obj.right + "," + obj.percentage);
              let div = document.getElementById("result");
              div.innerHTML = "<h1><center><i><u>RESULT PAGE<u><i><center><h1>";
              div2 = document.getElementById("score");
              result = "<center><h1>SCORE : " + obj.score + "<h1>";
              result += "<h1>CORRECT :" + obj.right + "<h1>";
              result += "<h1>PERCENTAGE :" + obj.percentage + "<h1>";
              if (obj.percentage >= 50) {
                result += "<h1>WELL DONE BUDDY YOU PASSED!<h1></center>";
              } else {
                result += "<h1>OOPS!YOU<h1></center>";
              }
              div2.innerHTML = result;
            }
          };
          request2.open(
            "GET",
            "/result?userans=" +
              JSON.stringify(useranslist) +
              "&corrans=" +
              JSON.stringify(correctanslist),
            true
          );
          request2.send(null);
        }
      }
    