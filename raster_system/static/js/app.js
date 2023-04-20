const job_status_list = document.getElementsByClassName('jobstatus');

function rename_status(list){
    for (let i = 0; i < list.length; i++) {
        if (list[i].innerHTML=="False") {
            list[i].innerHTML="NIE";
          }
    else {
      list[i].innerHTML="TAK"
    }
      }
}

rename_status(job_status_list)

