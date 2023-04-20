const job_status_list = document.getElementsByClassName('jobstatus');

function rename_status(list){
  for (let i = 0; i < list.length; i++) {
    if (list[i].innerHTML=="False") {
      list[i].innerHTML="NIE";
      list[i].parentElement.classList.add("bg-danger");
      list[i].parentElement.classList.add("bg-opacity-25");
    }
    else {
      list[i].innerHTML="TAK"
      list[i].parentElement.classList.add("bg-success");
      list[i].parentElement.classList.add("bg-opacity-25");
    }
  }
}

rename_status(job_status_list)

