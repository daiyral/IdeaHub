document.addEventListener('DOMContentLoaded',()=>{
    
    var username=window.location.pathname;
    username=username.substring(username.lastIndexOf('/')+1);//username for profile we are looing at
    
    if(document.querySelector('#invite_btn')!=null){

        document.querySelector('#invite_form').onsubmit=()=>{
            document.getElementById('closemodal').click();
            invite(username)
            return false;
        }
    
    }
    document.querySelector('#overview_link').onclick=()=>{
        return overview(username)
    }
    
    document.querySelector('#projects_link').onclick=()=>{
        return projects(username)
    }

    document.querySelector('#experience_link').onclick=()=>{
        return experience(username)
    }
})
function invite(username){
    
    const project_invite=document.querySelector('#invite-assigned');

    fetch(`/invite/${username}`,{
        method:'POST',
        body:JSON.stringify({
            invite:`${project_invite.value}`
        })
    })
    .then(response=>response.json())
    .then(answer =>{
        console.log(answer)

            
    })
    
}

function overview(username){
    
    var info=document.querySelector('.profile-info');
    fetch(`/info/${username}/overview`)
    .then(response=>response.json())
    .then(overview=>{
        console.log(overview);
        document.querySelector('.header').innerHTML='Overview:';
        if(overview=="")
            info.innerHTML="No info yet.";
        else    
            info.innerHTML=overview;
    })

}
function projects(username){

    fetch(`/info/${username}/projects`)
    .then(response=>response.json())
    .then(projects=>{
        console.log(projects);
        document.querySelector('.header').innerHTML='Projects:';
        document.querySelector('.profile-info').innerHTML="";
        projects.forEach(create_project_card);
            
    })
}
function create_project_card(project){
    var info=document.querySelector('.profile-info');
    var project_card=document.querySelector('.profile_project').cloneNode(true);
    project_card.style.display='flex';
    project_card.querySelector('.profile_project_img').src=`${project['img']}`;
    project_card.querySelector('.profile_project_title').innerHTML=`${project['name']}`;
    project_card.querySelector('.profile_project_text').innerHTML=`${project['headline']}`;
    info.appendChild(project_card);
}
function experience(username){
    var info=document.querySelector('.profile-info');
    fetch(`/info/${username}/experience`)
    .then(response=>response.json())
    .then(experience=>{
        console.log(experience);
        document.querySelector('.header').innerHTML='Experience:';
        if(experience=="")
            info.innerHTML='No info yet.';
        else    
            info.innerHTML=experience;
    })

}

