import React, { useState } from 'react';

export default function Topleft() {
  const [chatButtonImage, setChatButtonImage] = useState('Button-Chat-1.svg');
  const [chatVideoImage, setChatVideoImage] = useState('Button-Video-1.svg');
  const [chatBotImage, setChatBotImage] = useState('Button-Bot-1.svg')

  const handleChatButtonClick = () => {
    setChatButtonImage('Button-Chat-2.svg');
    setChatVideoImage('Button-Video-1.svg');
    setChatBotImage('Button-Bot-1.svg');
  };

  const handleVideoButtonClick = () => {
    setChatButtonImage('Button-Chat-1.svg');
    setChatVideoImage('Button-Video-2.svg');
    setChatBotImage('Button-Bot-1.svg');
  };

  const handleChatBotImageClick = () => {
    setChatButtonImage('Button-Chat-1.svg');
    setChatVideoImage('Button-Video-1.svg');
    setChatBotImage('Button-Bot-2.svg');
  };

  return (
    <div id='Topleft'>
      <div
        id="Button-Notification"
        style={{
          backgroundImage: `url(/Button-Notification.svg)`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: '60px 40px',
          backgroundPositionX: 'right',
          userSelect: 'none',
          cursor: 'pointer',
        }}
      ></div>

      <div
        id="Button-Chat-1"
        style={{
          backgroundImage: `url(/${chatButtonImage})`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: '40px 25px',
          backgroundPositionX: 'right',
          userSelect: 'none',
          cursor: 'pointer',
        }}
        onClick={handleChatButtonClick}
      ></div>

      <div
        id="Button-Video-1"
        style={{
          backgroundImage: `url(/${chatVideoImage})`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: '40px 25px',
          backgroundPositionX: 'right',
          userSelect: 'none',
          cursor: 'pointer',
        }}
        onClick={handleVideoButtonClick}
      ></div>

      <div id="Button-Bot-1" style={{
        backgroundImage: `url(/${chatBotImage})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: '40px 25px',
        backgroundPositionX: 'right',
        userSelect: 'none',
        cursor: 'pointer',
      }}
      onClick={handleChatBotImageClick}
      ></div>
    </div>
  )
}