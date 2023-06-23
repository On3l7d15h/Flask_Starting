const vars = {
    svgs: document.querySelectorAll(".container .sidebar svg")
}

// Checking if svgs has values.
if(vars?.svgs?.length > 0){
    vars?.svgs?.forEach(svg => {
        svg.addEventListener("click", () => {
            alert(`Click in svg!!`)
        })
    })
}