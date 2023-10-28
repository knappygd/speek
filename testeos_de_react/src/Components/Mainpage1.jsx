import Friends from "./Friends-Mainpage"
import Chatpage from "./ChatPage"
import Topleft from "./Top-left"
import Topright from "./Top-right"
import SearchFriends from "./Search_friends"

export default function Mainpage1() {
  return (
    <div id="container-mainpage1">
      <div id="left">
        <Topleft />
        <Friends />
        <SearchFriends />
    </div>
        <div id="right">
          <Topright />
         <Chatpage />
      </div>
    </div>
  )
}