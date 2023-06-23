// JS ARCHIVES 

// Our vars
const vars = {
    form: document.querySelector(".form"),
    svgs: document.querySelectorAll(".container .sidebar svg")
}

// functions
const handleOnSubmit = () => {
    // preventDefault
    event.preventDefault();

    // vars
    let name = vars.form.childNodes[3].childNodes[1].value

    // conditional
    if(name !== undefined && name !== "")
    {
        console.log(name)
        document.location.href = `/login/place/${name}`
        return;
    }

    alert("please, fill the field name.")
    return;

}

//



