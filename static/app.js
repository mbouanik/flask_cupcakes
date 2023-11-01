const form = $("#form");

form.on("submit", async (evt) => {
  evt.preventDefault();
  const res = await add_cupcake();
  const cupcake = $("<div>").addClass("cupcake");
  const rating = $(
    `<div class='rating'> ⭐️ ${res.data.cupcake.rating} </div>`,
  );
  const img = $("<div>").append(`<img src=${res.data.cupcake.image}>`);
  await img.append(
    `<div class="flavor"> <p> ${res.data.cupcake.size} </p> <p> ${res.data.cupcake.flavor} </p>  </div>`,
  );
  cupcake.append(rating, img);
  $("#cupcakes").append(cupcake);
});

async function add_cupcake() {
  const data = {
    flavor: $("input[type=text][name=flavor]").val(),
    size: $("input[type=text][name=size]").val(),
    rating: parseFloat($("input[type=number][name=rating]").val()),
    image: $("input[type=text][name=image]").val(),
  };
  return await axios.post("/api/cupcakes", data);
}
