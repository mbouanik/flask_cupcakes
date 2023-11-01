const form = $("#form");

form.on("submit", (evt) => {
  evt.preventDefault();
  add_cupcake();
});

async function add_cupcake() {
  const data = {
    flavor: $("input[type=text][name=flavor]").val(),
    size: $("input[type=text][name=size]").val(),
    rating: parseInt($("input[type=number][name=rating]").val()),
    image: $("input[type=text][name=image]").val(),
  };
  await axios.post("/api/cupcakes", data);
}
