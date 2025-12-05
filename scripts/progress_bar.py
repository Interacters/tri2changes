from progress.bar import ChargingBar

# progress bar to tell how far along the code is
# configurable title
class ProgressBar:
    def __init__(self, userInfo, total):
        # variable initialization
        self.userInfo = userInfo
        self.total = total

        # create the bar at the start
        self.bar = ChargingBar(
            message=f"{userInfo} %(index)s/%(max)s",
            max=total,
            suffix="%(percent).1f%% (ETA %(eta)ds)",
        )

    def continue_progress(self):
        self.bar.next()

    def end_progress(self):
        self.bar.finish()

    def set_message(self, item=None):
        if item is not None:
            self.bar.message = f"{self.userInfo} {item} %(index)s/%(max)s"

    def set_suffix(self, item=None):
        if item is not None:
            self.bar.suffix = f"%(percent).1f%% (ETA %(eta)ds) {item}"

            #mood checker stuff

            const API_URL = "http://localhost:5000/api/mood";

function sendMood(mood) {
    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mood })
    })
    .then(res => res.json())
    .then(() => loadMoods());
}

function loadMoods() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("mood-list");
            list.innerHTML = "";

            data.forEach(entry => {
                const div = document.createElement("div");
                div.className = "mood-entry";
                div.textContent = `${entry.mood} — ${new Date(entry.timestamp).toLocaleString()}`;
                list.appendChild(div);
            });
        });
}

// Load all moods when page opens
loadMoods();

