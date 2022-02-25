
function viewportResponse(){
    const viewportwidth = window.visualViewport.width;
    let introVideo = document.querySelector('.video_container');
    let introNav = document.querySelector('.header');
    let sideNav = document.querySelector('.side_nav')
    let main = document.querySelector('.main_container');
    let reg = document.querySelector('#container');
    let login = document.querySelector('.container2');
    let category1 = document.querySelector('.row1')
    let category2 = document.querySelector('.row2')
    let lessonImage = document.querySelector('.lesson_nav_img');
    let lessonNav = document.querySelector('.lesson_nav');
    let eggo = document.querySelector('.egg_overview');
    let iframe = document.getElementsByTagName("iframe")[0];
    let iframe2 = document.getElementsByTagName("iframe")[1];
    let foodUploads = document.querySelector(".upload_image_container");
    if(viewportwidth < 700 && introVideo != null){
        introVideo.style.display = 'none';
    }
    if(viewportwidth < 700 && introNav != null){
        introNav.style.backgroundImage = 'none';
    }
    if(viewportwidth < 700 && sideNav != null){
        sideNav.style.display = 'none';
    }
    if(viewportwidth < 700 && main != null && reg != null && login != null){
        console.log(main);
        console.log(reg)
        main.style.flexDirection = 'column';
        reg.style.width = '75%';
        login.style.width = '75%';
    }
    if(viewportwidth < 700 && category1 != null && category2 != null){
        category1.style.flexDirection = "column";
        category2.style.flexDirection = "column";
    }
    if(viewportwidth < 700 && lessonImage != null && lessonNav != null & eggo != null){
        lessonImage.style.display = "none";
        lessonNav.style.backgroundColor = "rgba(250, 250, 250, 0)";
        lessonNav.style.width = "100px";
        eggo.style.marginLeft = "50px";
        console.log(iframe);
        iframe.style.width = "300";
        iframe.style.height = "300";
        iframe2.style.width = "300";
        iframe2.style.height = "300";
    }

}
viewportResponse();


function foodImageZoom(id){
    let foodImage = document.querySelector('.myFood' + id);
    if(foodImage.style.transform == "scale(1)"){
        console.log(foodImage);
        foodImage.style.transition = "transform 0.25s ease"
        foodImage.style.transform = "scale(2)"
        foodImage.style.cursor = "zoom-out"
        foodImage.style.zIndex = "10";
    } else if (foodImage.style.transform = "scale(2)"){
        foodImage.style.transition = "transform 0.25s ease"
        foodImage.style.transform = "scale(1)"
        foodImage.style.cursor = "zoom-in"
        foodImage.style.zIndex = "0";
    }
}