document.addEventListener('DOMContentLoaded',()=>{
    
    var username=window.location.pathname;
    username=username.substring(username.lastIndexOf('/')+1);//username for profile we are looing at
    
    if(document.querySelector('#invite_btn')!=null){

        document.querySelector('#invite_btn').onclick=()=>{
            return invite(username)
        }
    
        document.querySelector('#message_btn').onclick=()=>{
            return message(username)
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
    
}
function message(username){

}
function overview(username){
    
    fetch(`/info/${username}/overview`)
    .then(response=>response.json())
    .then(overview=>{
        document.querySelector('.header').innerHTML='Overview:'
        document.querySelector('.profile-info').innerHTML=overview
    })

}
function projects(username){

    fetch(`/info/${username}/projects`)
    .then(response=>response.json())
    .then(projects=>{
        document.querySelector('.header').innerHTML='Projects:'
        document.querySelector('.profile-info').innerHTML=projects
    })
}
function experience(username){

    fetch(`/info/${username}/experience`)
    .then(response=>response.json())
    .then(experience=>{
        document.querySelector('.header').innerHTML='Experience:'
        document.querySelector('.profile-info').innerHTML=experience
    })

}

