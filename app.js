const form = document.querySelector('form');

const input = document.querySelector('#symptoms');
const outputContainer = document.querySelector('#output-container');
const outputText = document.querySelector('#output-text');
const submitBtn = document.querySelector('#submit-btn');
const apiKey = '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';
const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions';
// const apiUrl = 'https://api.openai.com/v1/completions';

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const prompt = input.value.trim()
  if (prompt.length > 0) {
    submitBtn.disabled = true;
    outputText.textContent = 'Generating diagnosis...';

    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        prompt: "I am having following symptoms: ${prompt}, what do you think is wrong with me?",
        max_tokens: 100,
        n: 1,
        stop: ['\n']
      })
    })
    .then(response => response.json())
    .then(data => {
    //   outputText.textContent = data.choices[0].text.trim();
      outputText.textContent = data.choices[0].text.trim();
      submitBtn.disabled = false;
    })
    .catch(error => {
      console.error(error);
      outputText.textContent = 'An error occurred while generating the diagnosis. Please try again.';
      submitBtn.disabled = false;
    });
  } else {
    outputText.textContent = 'Please enter at least one symptom.';
  }
});