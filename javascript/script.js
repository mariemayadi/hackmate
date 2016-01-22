$(document).ready(function () {

  $("#btn").click(function (e) {
    e.preventDefault();
    // get solo hacker's list of skills
    var skills_list = [];

    var solo_hacker_name = $("#soloname").val();
    var solo_hacker_slackid = $("#solo_slack_id").val();


    $(".skill").each( function() {
      if ($(this).is(":checked")) {
        var skill = $(this).next('label').text();
        skills_list.push(skill);
      }
      console.log(skills_list);
      console.log('stringify');
      console.log(JSON.stringify(skills_list));
    });


    $.ajax({ method: "post",
             url: "/solo_hacker_info",
            //  url: "/groupinput",
             data: { name : solo_hacker_name,
                    slackid : solo_hacker_slackid,
                    skill : JSON.stringify(skills_list) }
    }).done( function(data) {
      console.log("AJAX finished.");
      // location.href = "http://www.example.com/ThankYou.html"
      location.href = "/groupinput";
    });

  });

});
