const log = console.log

const textarea = document.querySelector("form textarea[name='data']")

textarea.addEventListener("input", () => {
  textarea.style.height = textarea.scrollHeight + "px"
  if (textarea.value.length == 0)
    textarea.style.height = "50px"
})

const checkPass = document.querySelector(".checkPass")

document.querySelector(".viewSaved").addEventListener("click", (e) => {
  e.stopPropagation()
  checkPass.classList.toggle("checkPassAct")
})

checkPass.addEventListener("click", (e) => {
  e.stopPropagation();
});

document.addEventListener("click", () => {
  checkPass.classList.remove("checkPassAct");
});

async function hashPassword(password) {
  const encoder = new TextEncoder();
  const data = encoder.encode(password);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
}

const form = document.querySelector('header form');
form.addEventListener('submit', async function (e) {
  e.preventDefault();

  const password = form.querySelector('#password').value;
  const hashed = await hashPassword(password);
  document.getElementById('hashed_password').value = hashed;

  form.submit();
});