const toggle = document.querySelector(".menu-icon .toggle");
const sidebar = document.getElementById("sidebar");

document.onclick = function (e) {
   if (e.target.id !== "sidebar") {
      if (e.target !== document.querySelector(".menu-icon .toggle")) {
         if(sidebar.classList.contains("active")) {
            document.querySelector(".main-header .article-overlay").remove();
         }
         sidebar.classList.remove("active");
      }
   }
};

document.querySelector(".menu-icon ").onclick = function () {
   sidebar.classList.toggle("active");
   let overlay = document.createElement("div")
   overlay.classList.add("article-overlay")
   document.querySelector(".header .main-header").appendChild(overlay);
   window.onscroll= (event)=>{
      event.preventDefault();
   }
};

// landing Background 
let landingBackground = document.querySelector(".home .image-slide");
console.log(landingBackground);
let arrayOflandings = ["landing01.jpg","landing02.jpg","landing03.png","landing04.jpg","landing05.jpg"]

function landingImage() {
   let position = 0;
   setInterval(()=>{
      if(position == arrayOflandings.length)
         position = 0;
      landingBackground.style.backgroundImage = `url("imgs/` + arrayOflandings[position] + `")`
      position++;
      console.log(position)
   },8000)
}
landingImage();


let articleBox = document.querySelectorAll(".article-warpper .article-text");
// console.log(articleBox[0])
articleBox.forEach(function(article) {
   article.onclick = ()=> {
      //first create the overlay 
      let overlay = document.createElement("div")
      overlay.classList.add("article-overlay")
      document.body.appendChild(overlay);
      // second create the Pop Article
      let popBox = document.createElement("div");
      popBox.classList.add("article-pop");
      // create close button
      let closeBtn = document.createElement("button");
      closeBtn.classList.add("article-close");
      closeBtn.appendChild(document.createTextNode("X"));
      popBox.appendChild(closeBtn);
      console.log("closeBtn");
      //check if the article has image and append it if exit in pop box
      if(article.children[0].nodeName == "IMG") {
         // console.log(article.children[0])
         // console.log(article.children[0].nodeName)
         // console.log(article.children[0].src)
         // console.log("img")
         let imageEle = document.createElement("img")
         imageEle.src =article.children[0].src;
         imageEle.classList.add("article-image");
         popBox.appendChild(imageEle);
      }
      else console.log("not img")
      //check if the article has article text and append it if exit in pop box
      if(article.children[1].nodeName == "DIV") {
         let articleText = document.createElement("div");
         articleText.classList.add("article-text")
         // console.log(article.children[1].children[0])
         // console.log(article.children[1].children[1])
         if (article.children[1].children[0].nodeName == "H5"){
            let titleEle = document.createElement("h5")
            titleEle.classList.add("article-title");
            titleEle.innerHTML = article.children[1].children[0].innerText
            articleText.appendChild(titleEle);
         }
         if (article.children[1].children[1].nodeName == "SMALL"){
            console.log(article.children[1].children[1].innerText)
            let descriptionEle = document.createElement("small")
            descriptionEle.classList.add("article-desc");
            descriptionEle.innerHTML = article.children[1].children[1].innerText;
            articleText.appendChild(descriptionEle);
         }
         popBox.appendChild(articleText)
      }
      else console.log("not title")
      document.body.appendChild(popBox)
      closeBtn.onclick = ()=>{
         popBox.remove();
         overlay.remove();
      }
   }
})

// let videoBox = document.querySelectorAll(".sections-videos .article-text");
// videoBox.forEach(video => {
//    video.onclick = function(e) {
//       console.log(video);
//       // createOverlay();
//       let overlay = createOverlay();
//       console.log(overlay);
//       let popBox = document.createElement("div");
//       popBox.classList.add("article-pop");
//       let closeBtn = createCloseBtn(popBox)
//       console.log(closeBtn);
//       let videoEle = document.createElement("video");
//       videoEle.src = "http://127.0.0.1:5500/My%20Project/videos.html";
//       // videoEle.src = "../video/Child development- 5-6 years.mp4" ;
//       // videoBox[0].children[1].children[0].baseURI
//       videoEle.controls = true;
//       videoEle.muted = true;

//       popBox.appendChild(videoEle)
//       document.body.appendChild(popBox);
//    }
// })
function createOverlay(){
   let overlay = document.createElement("div")
      overlay.classList.add("article-overlay")
      document.body.appendChild(overlay);
      return overlay
}
function createCloseBtn(parent) {
   let closeBtn = document.createElement("button");
   closeBtn.classList.add("article-close");
   closeBtn.appendChild(document.createTextNode("X"));
   parent.appendChild(closeBtn);
   return closeBtn
}
let videoTestEle = document.querySelector(".video-holder video");
console.log(videoTestEle);