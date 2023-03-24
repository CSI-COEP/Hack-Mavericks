const chatbotMessages = document.querySelector('.chatbot-messages');
const chatbotInput = document.querySelector('.chatbot-input input');
const chatbotSendButton = document.querySelector('.chatbot-input button');

chatbotSendButton.addEventListener('click', sendMessage);

function sendMessage() 
{
  const messageText = chatbotInput.value;
  if (!messageText) return;

  const messageElement = document.createElement('div');
  messageElement.classList.add('chatbot-message', 'sent');
  messageElement.innerHTML = `<p>${messageText}</p>`;
  chatbotMessages.appendChild(messageElement);

  chatbotInput.value = '';
  chatbotInput.focus();
}
