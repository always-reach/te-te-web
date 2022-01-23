import * as React from 'react'
import './App.css'

import Box from '@mui/material/Box'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'

import {FetchLiekedTweets,Tweet} from '../types/index'
import tweetInit from './test.json'


function App() {
  const [likedTweets,setlikedTweets]=React.useState<FetchLiekedTweets|null>(null)

  React.useEffect(()=>{
    /* const getLiked=async()=>{
      const respone=await SearchLikedTweet("000")
      const responeJson=await respone.json()
      console.log("liked tweets",responeJson)
    } */

    //getLiked()
    setlikedTweets(tweetInit as FetchLiekedTweets)
  },[])

  return (
    <Box>
      {likedTweets?.data.map((tweetElements:Tweet)=>{
        return(
        <Card key={tweetElements.text} variant="outlined">
          <CardContent>
            <Typography>{tweetElements.text}</Typography>
            {tweetElements.media?.map((url)=>{
                return(
                    <CardMedia
                    key={url}
                    component="img"
                    image={url}
                    alt="twitter_image"
                    />
                )
            })}
          </CardContent>
        </Card>)
      })}
    </Box>
  )
}

export default App
