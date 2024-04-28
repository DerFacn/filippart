let idCounter = 0;

const addBtn = document.getElementById('addBtn')
addBtn.addEventListener('click', addInput)

function addInput() {
  idCounter++;

  const inputGroup = document.createElement('div');
  inputGroup.classList.add('card');

  const colLeft = document.createElement('div');
  colLeft.classList.add('col-left');

  const pictureLabel = document.createElement('label');
  const pictureImg = document.createElement('img');
  pictureImg.src = "/static/icons/picture.svg";
  pictureImg.alt = "Picture frame";
  pictureLabel.appendChild(pictureImg);

  const pictureInput = document.createElement('input');
  pictureInput.type = 'file';
  pictureInput.id = `picture_${idCounter}`;
  pictureInput.name = `picture_${idCounter}`;
  pictureInput.classList.add('hidden');
  pictureInput.addEventListener('change', function() {
    previewImage(this);
  });
  pictureLabel.htmlFor = `picture_${idCounter}`;

  const inputName = document.createElement('input');
  inputName.type = 'text';
  inputName.name = `name_${idCounter}`;
  inputName.classList.add('heavy');
  inputName.placeholder = 'Picture name';

  const inputPrice = document.createElement('input');
  inputPrice.type = 'number';
  inputPrice.name = `price_${idCounter}`;
  inputPrice.placeholder = 'Price';

  const deleteButton = document.createElement('button');
  deleteButton.textContent = '✖ Delete picture';
  deleteButton.classList.add('warning');
  deleteButton.addEventListener('click', function() {
    inputGroup.remove();
  });

  colLeft.appendChild(pictureLabel);
  colLeft.appendChild(pictureInput);
  colLeft.appendChild(inputName);
  colLeft.appendChild(inputPrice);
  colLeft.appendChild(deleteButton);

  const colRight = document.createElement('div');
  colRight.classList.add('col-right');

  const inputDescription = document.createElement('textarea');
  inputDescription.placeholder = 'Picture description';
  inputDescription.name = `description_${idCounter}`;

  colRight.appendChild(inputDescription);

  inputGroup.appendChild(colLeft);
  inputGroup.appendChild(colRight);

  document.getElementById('content').appendChild(inputGroup);
}

function previewImage(input) {
  const pictureLabel = input.previousElementSibling;
  const previewImg = pictureLabel.querySelector('img');

  const reader = new FileReader();
  reader.onload = function(e) {
    previewImg.src = e.target.result;
  };
  reader.readAsDataURL(input.files[0]);
}
