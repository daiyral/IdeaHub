document.addEventListener('DOMContentLoaded',()=>{ 
    var project_name=window.location.pathname;
    project_name=project_name.substring(project_name.lastIndexOf('/')+1);
    load_apply(project_name);
    document.querySelector('#apply_btn').onclick=()=>{
        return apply(project_name)
    }
})
function load_apply(project_name){
    apply_btn=document.querySelector('#apply_btn');
    fetch(`/apply/${project_name}`,{
        method:"GET"
    })
    .then(response=>response.json())
    .then(is_applied=>{
        if(is_applied ==1){//if we get 1 as a response means user is already applied
            apply_btn.innerHTML='Cancel';
            apply_btn.style.background='#D3D3D3';        }
        else//user is not applied yet
            apply_btn.innerHTML='Apply';    
    })

}
function apply(project_name){
    apply_btn=document.querySelector('#apply_btn');
    fetch(`/apply/${project_name}`,{
        method:"POST"
    })
    .then(response=>response.json())
    .then(answer=>{
        console.log(answer)
        if (answer == 1){//User successfully applied
            apply_btn.innerHTML='Cancel';
            apply_btn.style.background='#D3D3D3';
        }
        else if(answer == -1)//User is already part of the project
            document.querySelector('.cantapply').style.display='flex';
        else{//user wants to cancel application
            apply_btn.innerHTML='Apply';
            apply_btn.style.background='#009578';
        }    
          
            
    })
    
}