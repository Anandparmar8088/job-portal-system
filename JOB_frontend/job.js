let form = document.getElementById("jobForm");
let responseBox = document.getElementById("responseBox");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    let jobData = {
        job_title: document.getElementById("job_title").value,
        job_description: document.getElementById("job_description").value,
        contact_info: document.getElementById("contact_info").value,
    };

    try {
        let res = await fetch("http://127.0.0.1:8000/api/job/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(jobData)
        });

        let data = await res.json();

        if (data.success) {
            responseBox.innerHTML = `<p style="color:green;">✅ Job Posted Successfully!</p>`;
            form.reset();
        } else {
            responseBox.innerHTML = `<p style="color:red;">❌ Error: ${JSON.stringify(data.Message)}</p>`;
        }
    } catch (err) {
        responseBox.innerHTML = `<p style="color:red;">⚠️ Something went wrong: ${err}</p>`;
    }
});
