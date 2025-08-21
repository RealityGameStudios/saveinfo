const header = document.querySelector(".headerSection")

function SetHeader(header) {
  header.innerHTML =
    `
        <div class="header">
          <div class="headerGrp">
            <h3>
              <a href="/">
                Reality Studios
              </a>
            </h3>
          </div>
          <div class="headerGrp">
            ${document.body.id == "index" ?
      `
            <button class="viewSaved">
              View saved data
            </button>
            <div class="checkPass">
              <h3>Enter password :</h3>
              <form action="/data" method="GET">
                <input type="password" id="password">
                <input type="hidden" name="p" id="hashed_password">
                <button>
                  Go
                </button>
              </form>
            </div>
              `:
      `
              <a href="/">
                <button>
                  Back
                </button>
              </a>
              `
    }
          </div>
        </div>
  `
}

SetHeader(header)