const form = document.getElementById("prediction-form");
const submitBtn = document.getElementById("submit-btn");
const resultBox = document.getElementById("result-box");
const priceText = document.getElementById("predicted-price");
const errorMessage = document.getElementById("error-message");

function formatPrice(value) {
    return new Intl.NumberFormat("en-GB", {
        style: "currency",
        currency: "GBP",
        maximumFractionDigits: 0
    }).format(value);
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    errorMessage.classList.add("hidden");
    resultBox.classList.add("hidden");
    submitBtn.disabled = true;
    submitBtn.textContent = "Hesaplanıyor...";

    const payload = {
        brand: document.getElementById("brand").value.trim(),
        model: document.getElementById("model").value.trim(),
        year: Number(document.getElementById("year").value),
        transmission: document.getElementById("transmission").value,
        km: Number(document.getElementById("km").value),
        fuelType: document.getElementById("fuelType").value,
        enginSize: Number(document.getElementById("enginSize").value)
    };

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 12000);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            signal: controller.signal,
            cache: "no-store",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`Tahmin isteği başarısız oldu (${response.status}).`);
        }

        const data = await response.json();
        priceText.textContent = formatPrice(data.predicted_price);
        resultBox.classList.remove("hidden");
    } catch (error) {
        if (error.name === "AbortError") {
            errorMessage.textContent = "İstek zaman aşımına uğradı. Sunucu çalışıyor mu kontrol edip tekrar deneyin.";
        } else {
            errorMessage.textContent = "Bir hata oluştu. Lütfen girdi bilgilerini kontrol edip tekrar deneyin.";
        }
        errorMessage.classList.remove("hidden");
    } finally {
        clearTimeout(timeoutId);
        submitBtn.disabled = false;
        submitBtn.textContent = "Fiyat Tahmini Yap";
    }
});
