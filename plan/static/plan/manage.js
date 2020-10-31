document.addEventListener('DOMContentLoaded',()=>{
    var project_name=window.location.pathname;
    project_name=project_name.substring(project_name.lastIndexOf('/')+1);
    load_tasks(project_name);


    const list_items=document.querySelectorAll('.listing');//all list items
    const lists=document.querySelectorAll('.lists');//all lists
    document.querySelector('#backlog-listing').style.display='none';

    lists.forEach(list=>{
        list.addEventListener("dragover",e=>{
            e.preventDefault();
        })
        list.addEventListener("drop",e=>{
            e.preventDefault();
            const dropped_id=e.dataTransfer.getData("text/plain");
            const dropped=document.getElementById(`${dropped_id}`);
            const box= dropped.querySelector('.box');
            const list_name=list.classList.item(1);
            list.querySelector('ul').appendChild(dropped);
            if(list_name == 'review')
                box.style.background='#1E90FF';
            else if(list.classList.item(1)=='done')
                box.style.background='#32CD32';
            else
                box.style.background='#e40046';    
            fetch(`/update_task/${dropped_id}`,{
                method:"POST",
                body:JSON.stringify({
                    col:`${list_name}`
                })
            })    
            .then(response=>response.json())
            .then(result=>{
                console.log(result)
            })
        })
    })

    document.querySelector('#task-form').onsubmit=()=>{
        document.getElementById('closemodal').click();
        add_task(project_name);
        document.getElementById('task-title').value="";
        document.getElementById('task-body').value="";
        return false;
    }
    
})

function load_tasks(project_name){

    fetch(`/tasks/${project_name}`,{
        method:"GET"
    })
    .then(response=>response.json())
    .then(tasks=>{
        console.log(tasks)
        tasks.forEach(create_task_cards);
    })
   
}


function add_task(project_name){

    const title=document.querySelector('#task-title');
    const body=document.querySelector('#task-body');
    const assigned=document.querySelector('#task-assigned');

    fetch(`/tasks/${project_name}`,{
        method:'POST',
        body:JSON.stringify({
            title:`${title.value}`,
            body:`${body.value}`,
            assigned:`${assigned.value}`
        })
    })
    .then(response => response.json())
    .then(task => {
        console.log(task)
        create_task_cards(task)
    })
   


}

function create_task_cards(task)
{
    var new_task=document.querySelector('#backlog-listing').cloneNode(true);
    var initials= task.assigned_first_name[0].toUpperCase()+task.assigned_last_name[0].toUpperCase();
    new_task.id=`${task['id']}`;
    new_task.classList.add('listing');
    new_task.querySelector('#backlog_title').innerHTML=`${task['title']}`;
    new_task.querySelector('#backlog_body').innerHTML=`${task['body']}`;
    new_task.querySelector('#backlog_img').src=`${task['assigned_img']}`;
    new_task.querySelector('#backlog_username').innerHTML=`${initials}`;
    new_task.querySelector('#backlog_timestamp').innerHTML=`${task['timestamp']}`
    new_task.style.display='inline-block';
    new_task.querySelector('#delete-task').onclick=()=>{
        fetch(`/delete_task/${task['id']}`,{
            method:"POST"
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result)
            new_task.style.animationPlayState="running";
            //new_task.remove();
            })
    }
    new_task.addEventListener('dragstart',e=>{
        e.dataTransfer.setData("text/plain",new_task.id)
    })
    const list=document.querySelector(`.${task['col']}-tasks`);
    if(task['col'] == 'review')
        new_task.querySelector('.box').style.background='#1E90FF';
    if(task['col'] =='done')
        new_task.querySelector('.box').style.background='#32CD32';
    list.insertBefore(new_task,list.firstChild);

}