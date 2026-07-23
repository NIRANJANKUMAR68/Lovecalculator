async function senddata() {

    const name1 = document.getElementById("name1").value.trim();
    const name2 = document.getElementById("name2").value.trim();

    // Validation
    if (name1 === "" || name2 === "") {
        alert("Please enter both names.");
        return; // Stop execution here
    }

    const response = await fetch("http://127.0.0.1:8000/sregister", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name1: name1,
            name2: name2
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = data;

    // Clear the input fields
    document.getElementById("name1").value = "";
    document.getElementById("name2").value = "";
}