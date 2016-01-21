$(document).ready(function () {

  $("#submit_button").click(function (e) {
    var parent_element = $(e.currentTarget.parentElement);
    // get solo hacker's name
    // var solo_hacker_name = parent_element.find("#soloname").val();
    // console.log("solo_hacker_name");
    // console.log(solo_hacker_name);
    
    // get solo hacker's Slack ID
    var solo_hacker_slackid = parent_element.find("#solo_slack_id").val();
    console.log("solo_hacker_slackid");
    console.log(solo_hacker_slackid);
    // get solo hacker's list of skills
    var skills_list = [];

    console.log('$("#soloname").val()')
    console.log($("#soloname").val());
    var solo_hacker_name = $("#soloname").val()



    $(".skill").each( function() {
      if ($(this).is(":checked")) {
        // console.log("Passed the first check!");
        var skill = $(this).next('label').text();
        // console.log(skill);
        skills_list.push(skill);
      }
      console.log(skills_list);
    });

    // send this information over to main.app
    $.ajax({ method: "post",
             url: "/solo_hacker_info",
             data: { name : solo_hacker_name,
                    slackid : solo_hacker_slackid,
                    skill : JSON.stringify(skills_list) }
    }).done( function(data) {
      console.log("AJAX finished.");
    });

  });

});
