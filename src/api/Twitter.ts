

export const SearchLikedTweet = async (ID:string): Promise<Response> => {
    const bearerToken= import.meta.env.VITE_TWITTER_BEARER_TOKEN
    const header = new Headers()

    header.append("Content-Type", "application/json")
    header.append("Authorization", 'Bearer' + bearerToken)
    const response = await fetch("https://api.twitter.com/2/users/" + ID + "/liked_tweets", {
        method: "GET",
        mode:'cors',
        credentials:'include',
        headers: header,
    })

    return response
}