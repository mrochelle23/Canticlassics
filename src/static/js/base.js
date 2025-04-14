// Function to update character count and resize the textarea
function updateCharacterCountAndResize() {
    var messageBox = document.getElementById("message");
    var charCount = document.getElementById("charCount");

    // Show the character counter when the user starts typing
    if (messageBox.value.length > 0) {
        charCount.style.display = "block";
    } else {
        charCount.style.display = "none";
    }

    // Update the character count
    charCount.textContent = messageBox.value.length + " / 500";

    // Resize the textarea based on the content
    messageBox.style.height = 'auto'; // Reset the height to auto
    messageBox.style.height = (messageBox.scrollHeight) + 'px'; // Set height based on content
}
// Event listener that links to the footer
window.addEventListener('DOMContentLoaded', (event) => {
// Check if the page has been loaded with the #contact hash
if (window.location.hash === "#contact") {
    // Remove the hash from the URL to prevent auto-scrolling
    history.replaceState(null, null, window.location.pathname);

    // Scroll to the footer smoothly after a slight delay
    setTimeout(function() {
        const footer = document.getElementById('contact');
        if (footer) {
            // Custom smooth scroll function
            smoothScrollTo(footer, 700); // 5000 is the duration in milliseconds (5 seconds)
        }
    }, 500);  // Delay scroll for 500ms after page load (adjust as necessary)
}

// Add event listener for the Contact button click
const contactButton = document.querySelector('a[href="#contact"]');
if (contactButton) {
    contactButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default action (jumping directly to the section)
        
        const footer = document.getElementById('contact');
        if (footer) {
            smoothScrollTo(footer, 700); // Smooth scroll to the footer
        }
    });
}
});

// Custom smooth scroll function
function smoothScrollTo(target, duration) {
    const start = window.scrollY || window.pageYOffset;
    const end = target.getBoundingClientRect().top + start;
    const change = end - start;
    const startTime = performance.now();

    function animateScroll(currentTime) {
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        window.scrollTo(0, start + change * progress);

        if (elapsedTime < duration) {
            requestAnimationFrame(animateScroll);
        }
    }

    requestAnimationFrame(animateScroll);
}

//JavaScript for Hamburger Menu
document.addEventListener('DOMContentLoaded', function () {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('#navbarNav');

    navbarToggler.addEventListener('click', function () {
    navbarCollapse.classList.toggle('show');
    });
});




// Fade-in Scrolling Functionality
document.addEventListener("scroll", function() {
    let songs = document.querySelectorAll(".song");
    songs.forEach(song => {
        let rect = song.getBoundingClientRect();
        if (rect.top < window.innerHeight - 50) {
            song.style.opacity = "1";
            song.style.transform = "translateY(0)";
        }
    });
});


// Audio Player & Progress Bar Functionality
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".playPause").forEach(button => {
        button.addEventListener("click", function() {
            const songContainer = this.closest(".song");
            const audio = songContainer.querySelector("audio");
            const progressBar = songContainer.querySelector(".progress-bar");
            const buttonIcon = this.querySelector("i"); // Select the <i> element inside the button

            if (audio.paused) {
                // Pause all other audio elements before playing
                document.querySelectorAll("audio").forEach(a => {
                    if (a !== audio) {
                        a.pause();
                        a.currentTime = 0;
                        const otherButtonIcon = a.parentElement.querySelector(".playPause i");
                        otherButtonIcon.classList.remove("bi-pause-fill");
                        otherButtonIcon.classList.add("bi-play-fill");
                    }
                });

                audio.play();
                buttonIcon.classList.remove("bi-play-fill");
                buttonIcon.classList.add("bi-pause-fill");
            } else {
                audio.pause();
                buttonIcon.classList.remove("bi-pause-fill");
                buttonIcon.classList.add("bi-play-fill");
            }

            // Update progress bar
            audio.addEventListener("timeupdate", function() {
                let percentage = (audio.currentTime / audio.duration) * 100;
                progressBar.style.width = percentage + "%";
            });

            // Reset progress bar on song end
            audio.addEventListener("ended", function() {
                progressBar.style.width = "0%";
                buttonIcon.classList.remove("bi-pause-fill");
                buttonIcon.classList.add("bi-play-fill");
            });
        });
    });

    document.querySelectorAll(".nextTrack").forEach(button => {
        button.addEventListener("click", function() {
            const currentSongDiv = this.closest(".song");
            const nextSongDiv = currentSongDiv.nextElementSibling;

            if (nextSongDiv && nextSongDiv.classList.contains("song")) {
                const currentAudio = currentSongDiv.querySelector("audio");
                const currentPlayButtonIcon = currentSongDiv.querySelector(".playPause i");
                const currentProgressBar = currentSongDiv.querySelector(".progress-bar");

                const nextAudio = nextSongDiv.querySelector("audio");
                const nextPlayButtonIcon = nextSongDiv.querySelector(".playPause i");
                const nextProgressBar = nextSongDiv.querySelector(".progress-bar");

                // Stop current audio
                currentAudio.pause();
                currentAudio.currentTime = 0;
                currentPlayButtonIcon.classList.remove("bi-pause-fill");
                currentPlayButtonIcon.classList.add("bi-play-fill");
                currentProgressBar.style.width = "0%";

                // Play next audio
                nextAudio.play();
                nextPlayButtonIcon.classList.remove("bi-play-fill");
                nextPlayButtonIcon.classList.add("bi-pause-fill");

                // Update progress bar for new audio
                nextAudio.addEventListener("timeupdate", function() {
                    let percentage = (nextAudio.currentTime / nextAudio.duration) * 100;
                    nextProgressBar.style.width = percentage + "%";
                });

                // Reset progress bar on next song end
                nextAudio.addEventListener("ended", function() {
                    nextProgressBar.style.width = "0%";
                    nextPlayButtonIcon.classList.remove("bi-pause-fill");
                    nextPlayButtonIcon.classList.add("bi-play-fill");
                });
            }
        });
    });

    document.querySelectorAll(".previousTrack").forEach(button => {
        button.addEventListener("click", function() {
            const currentSongDiv = this.closest(".song");
            const prevSongDiv = currentSongDiv.previousElementSibling;

            if (prevSongDiv && prevSongDiv.classList.contains("song")) {
                const currentAudio = currentSongDiv.querySelector("audio");
                const currentPlayButtonIcon = currentSongDiv.querySelector(".playPause i");
                const currentProgressBar = currentSongDiv.querySelector(".progress-bar");

                const prevAudio = prevSongDiv.querySelector("audio");
                const prevPlayButtonIcon = prevSongDiv.querySelector(".playPause i");
                const prevProgressBar = prevSongDiv.querySelector(".progress-bar");

                // Stop current audio
                currentAudio.pause();
                currentAudio.currentTime = 0;
                currentPlayButtonIcon.classList.remove("bi-pause-fill");
                currentPlayButtonIcon.classList.add("bi-play-fill");
                currentProgressBar.style.width = "0%";

                // Play previous audio
                prevAudio.play();
                prevPlayButtonIcon.classList.remove("bi-play-fill");
                prevPlayButtonIcon.classList.add("bi-pause-fill");

                // Update progress bar for previous audio
                prevAudio.addEventListener("timeupdate", function() {
                    let percentage = (prevAudio.currentTime / prevAudio.duration) * 100;
                    prevProgressBar.style.width = percentage + "%";
                });

                // Reset progress bar on previous song end
                prevAudio.addEventListener("ended", function() {
                    prevProgressBar.style.width = "0%";
                    prevPlayButtonIcon.classList.remove("bi-pause-fill");
                    prevPlayButtonIcon.classList.add("bi-play-fill");
                });
            }
        });
    });
});



// JavaScript for Overlay Menu
const menuToggle = document.getElementById('menu-toggle');
const overlayMenu = document.getElementById('overlay-menu');

menuToggle.addEventListener('click', () => {
    overlayMenu.classList.toggle('hidden'); // Show/hide the overlay menu
    const icon = menuToggle.querySelector('i'); // Get the Font Awesome icon inside the button

    // Toggle between the hamburger icon (fa-bars) and the "X" icon (fa-times)
    if (icon.classList.contains('fa-bars')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }

    // Toggle the "open" class to change the icon color
    menuToggle.classList.toggle('open');
});