export type Tweet={
    text:string
    id:string
    created_at: string
    attachments?: {media_keys: string[]}
    author_id: string,
    lang: string,
    media: string[]
}

export type TweetMeta={
    result_count:number
    next_token:string
}


export type FetchLiekedTweets={
    data:Tweet[]
    meta:TweetMeta
}