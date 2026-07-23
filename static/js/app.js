/**
 * UK Vehicle History Report Generator — Frontend JavaScript
 * Handles form submission, file upload preview, color sync, and PDF download.
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reportForm');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.getElementById('btnLoader');
    const statusMessage = document.getElementById('statusMessage');
    const coverLogoUpload = document.getElementById('coverLogoUpload');
    const coverLogoInput = document.getElementById('coverLogo');
    const coverLogoPlaceholder = document.getElementById('coverLogoPlaceholder');
    const coverLogoPreview = document.getElementById('coverLogoPreview');

    const headerLogoUpload = document.getElementById('headerLogoUpload');
    const headerLogoInput = document.getElementById('headerLogo');
    const headerLogoPlaceholder = document.getElementById('headerLogoPlaceholder');
    const headerLogoPreview = document.getElementById('headerLogoPreview');

    // ── Country Tab Switcher ────────────────────────────────────
    window.switchCountry = function(country) {
        const countryTabs = document.querySelectorAll('.country-tab');
        const countryInput = document.getElementById('country');
        const plateIcon = document.getElementById('plateIcon');
        const regInput = document.getElementById('registration');
        const inputHint = document.getElementById('inputHint');

        countryTabs.forEach(t => t.classList.remove('active'));
        const activeTab = document.querySelector(`.country-tab[data-country="${country}"]`) || document.getElementById(`tab-${country}`);
        if (activeTab) activeTab.classList.add('active');

        if (countryInput) countryInput.value = country;

        if (country === 'de') {
            if (plateIcon) {
                plateIcon.textContent = 'DE';
                plateIcon.style.background = '#000000';
            }
            if (regInput) {
                regInput.placeholder = 'WVWZZZ3CZWE123456';
                regInput.maxLength = 17;
            }
            if (inputHint) {
                inputHint.textContent = 'Geben Sie die 17-stellige Fahrgestellnummer (FIN / VIN) ein';
            }
        } else {
            if (plateIcon) {
                plateIcon.textContent = 'GB';
                plateIcon.style.background = '#003da5';
            }
            if (regInput) {
                regInput.placeholder = 'AB12 CDE';
                regInput.maxLength = 8;
            }
            if (inputHint) {
                inputHint.textContent = 'Enter the UK registration number (e.g., AB12CDE, AB12 CDE)';
            }
        }
    };

    const countryTabs = document.querySelectorAll('.country-tab');
    countryTabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            if (e) e.preventDefault();
            const country = tab.getAttribute('data-country') || tab.dataset.country;
            window.switchCountry(country);
        });
    });

    // ── Package Selection ──────────────────────────────────────
    const packageCards = document.querySelectorAll('.package-card');
    packageCards.forEach(card => {
        card.addEventListener('click', () => {
            card.querySelector('input[type="radio"]').checked = true;
        });
    });

    // ── Logo Upload ────────────────────────────────────────────
    function setupLogoUpload(uploadDiv, inputEl, placeholder, preview) {
        uploadDiv.addEventListener('click', () => inputEl.click());

        inputEl.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                if (file.size > 5 * 1024 * 1024) {
                    showStatus('Logo file must be under 5MB.', 'error');
                    return;
                }
                const reader = new FileReader();
                reader.onload = (ev) => {
                    preview.src = ev.target.result;
                    preview.style.display = 'block';
                    placeholder.style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        });
    }

    setupLogoUpload(coverLogoUpload, coverLogoInput, coverLogoPlaceholder, coverLogoPreview);
    setupLogoUpload(headerLogoUpload, headerLogoInput, headerLogoPlaceholder, headerLogoPreview);

    // ── Color Sync ─────────────────────────────────────────────
    const primaryColor = document.getElementById('primaryColor');
    const primaryHex = document.getElementById('primaryColorHex');
    const primaryPreview = document.getElementById('primaryPreview');
    const accentColor = document.getElementById('accentColor');
    const accentHex = document.getElementById('accentColorHex');
    const accentPreview = document.getElementById('accentPreview');

    function syncColor(picker, hex, preview) {
        picker.addEventListener('input', () => {
            hex.value = picker.value;
            preview.style.background = picker.value;
        });
        hex.addEventListener('input', () => {
            if (/^#[0-9a-fA-F]{6}$/.test(hex.value)) {
                picker.value = hex.value;
                preview.style.background = hex.value;
            }
        });
    }

    syncColor(primaryColor, primaryHex, primaryPreview);
    syncColor(accentColor, accentHex, accentPreview);

    // ── Preset Colors ──────────────────────────────────────────
    document.querySelectorAll('.preset-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const primary = btn.dataset.primary;
            const accent = btn.dataset.accent;
            primaryColor.value = primary;
            primaryHex.value = primary;
            primaryPreview.style.background = primary;
            accentColor.value = accent;
            accentHex.value = accent;
            accentPreview.style.background = accent;
        });
    });

    // ── Form Submission ────────────────────────────────────────
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const registration = document.getElementById('registration').value.trim();
        if (!registration) {
            showStatus('Please enter a registration number.', 'error');
            return;
        }

        // Show loading state
        submitBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'flex';
        hideStatus();

        try {
            const formData = new FormData(form);
            
            const response = await fetch('/api/generate-report', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            
            if (!data.success) {
                throw new Error(data.error || 'Failed to generate report.');
            }

            // Redirect to download the file natively
            window.location.href = data.download_url;

            showStatus('✓ Report generated successfully! Your download should start automatically.', 'success');

        } catch (err) {
            showStatus(err.message || 'Something went wrong. Please try again.', 'error');
        } finally {
            submitBtn.disabled = false;
            btnText.style.display = 'inline';
            btnLoader.style.display = 'none';
        }
    });

    // ── Utility Functions ──────────────────────────────────────
    function showStatus(message, type) {
        statusMessage.textContent = message;
        statusMessage.className = `status-message ${type}`;
        statusMessage.style.display = 'block';
    }

    function hideStatus() {
        statusMessage.style.display = 'none';
    }

    // ── Registration Auto-format ───────────────────────────────
    const regInput = document.getElementById('registration');
    regInput.addEventListener('input', () => {
        regInput.value = regInput.value.toUpperCase();
    });
});
