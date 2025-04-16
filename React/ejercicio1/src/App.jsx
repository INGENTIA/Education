import { useState } from 'react'
import Card from './Components/Card'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const items =["React","Vite","JavaScript"];

  return (
    <section>
      <h1>!Hola Mundo!</h1>
      <Card title="Card1" description="This is a description" />
      <Card title="Card2" description="This is a description" />
      <ul>
        {
          items.map((item, index) => (
            <li key={index}>{item}</li>
          ))
        }
      </ul>
    </section>
  );
}

export default App
