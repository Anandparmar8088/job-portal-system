let main = document.querySelector("main");

async function sendData() {
    let res = await fetch("http://127.0.0.1:8000/api/get/");
    let data = await res.json();

    // clear existing jobs
    main.innerHTML = "";

    if (data.success && data.jobs.length > 0) {
        data.jobs.forEach(job => {
            let card = document.createElement("div");
            card.classList.add("job-card");

            card.innerHTML = `
                <h2 class="job-title">${job.job_title}</h2>
                <p class="job-description">${job.job_description}</p>
                <p class="job-contact">📧 ${job.contact_info}</p>
                <div class="button-container">
                    <button class="apply-btn">Apply Now</button>
                    <button class="fav-btn">Interested</button>
                </div>
            `;

            main.appendChild(card);
        });
    } else {
        main.innerHTML = `<p>No jobs available.</p>`;
    }
}

// call it when page loads
sendData();




// let man = document.querySelector("main")

// async  function datadis()
// {
//     let res = await fetch("api")
//     let data = await res.json()



//     disdata(prompt.data)

// }


// function disdata()
// {
//     main.innerHTML="";

//     for ( i in data)
//     {
//         main.innerHTML+=`
//         <p>${data.name}</p>
//         <p>$
//         `
        
        
        
//     }

// }


// disdata()


// myform.addeventlistner("submit",(e)=>{
//     e.priventdefault();
//     let data = {

//         name =e.target[0],
//         age = e.target[1]
//     }
// })