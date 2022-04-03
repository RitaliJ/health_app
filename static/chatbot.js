const userInput = document.querySelector('#userInput');
const conversationTable = document.querySelector('#conversationTable');
const button = document.querySelector('#queryButton');
const output = document.querySelector('#output');

$(document).keypress(
  function(event){
    if (event.which == '13') {
      event.preventDefault();
    }
});

function getAnswer() {
    var userInput = $('#userInput').val();
    addMsg(1, userInput)
    $.ajax({
      url: "/ask",
      type: "GET",
      data: {userInput: userInput},
      success: function(response) {
      addMsg(2, response)

   },
   error: function(xhr) {
     //Do Something to handle error
  }
  });
};

function addMsg(people, msg) {
  
  console.log('addMsg');
  var side = 'right';
  var $_phone = $('#chat');
  var $_lastMessage = $('#chat .message:last');
  
  if (people == 1) side = 'right';
  if (people == 2) side = 'left';
  
  var time = new Date(),
      timeString = zero(time.getHours()) + ':' + zero(time.getMinutes());
  
  if ($_lastMessage.hasClass(side)) {
    
    $_lastMessage.append(
      $('<div>').addClass('message-text').text(msg).append(
        $('<div>').addClass('message-time').text(timeString)
      )
    )
    
  } else {
    
    $_phone.append(
      $('<div>').addClass('message '+side).append(
        $('<div>').addClass('message-text').text(msg).append('<div class="message-time">' + timeString + '</div>')
      ));
  } 
  $('#chat').animate({ scrollBottom: $('#chat').height() }, 600);
}

function zero(num) {
    return ('0' + num).slice(-2);
}

/** smartest */
const displayConversation = (responseData) => {
	//create table headers
	const newTR = document.createElement('TR');
	const newTHQuestion = document.createElement('TH');
	const newTHAnswer = document.createElement('TH');
	newTHQuestion.append("Query");
	newTHAnswer.append("Doc Bot's Response");
	newTR.append(newTHQuestion);
	newTR.append(newTHAnswer);
	conversationTable.append(newTR);
	addRow(userInput, responseData);
  conversationTable.style.backgroundColor = "#F5FAFA";
}

const addRow = (userInput, responseData) => {
	const newRow = document.createElement('TR');
	const newQuestionTD = document.createElement('TD');
	const newAnswerTD = document.createElement('TD');
	newQuestionTD.append(userInput);
	newAnswerTD.append(responseData);
	newRow.append(newQuestionTD);
	newRow.append(newAnswerTD);
	conversationTable.append(newRow);
}