import * as React from 'react'
import logo from './logo.svg'
import './App.css'
import { SearchLikedTweet } from './api/Twitter'

function App() {
  const [count, setCount] = React.useState(0)

  React.useEffect(()=>{
    const getLiked=async()=>{
      const respone=await SearchLikedTweet("1365833961918722048")
      const responeJson=await respone.json()
      console.log("liked tweets",responeJson)
    }

    //getLiked()
  },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hello Vite + React!</p>
        <p>
          <button type="button" onClick={() => setCount((count) => count + 1)}>
            count is: {count}
          </button>
        </p>
        <p>
          Edit <code>App.tsx</code> and save to test HMR updates.
        </p>
        <p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          {' | '}
          <a
            className="App-link"
            href="https://vitejs.dev/guide/features.html"
            target="_blank"
            rel="noopener noreferrer"
          >
            Vite Docs
          </a>
        </p>
      </header>
    </div>
  )
}

export default App