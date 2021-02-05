<template>
  <div>
    <div>Hai {{text}}</div>
    <chat-window
      style="z-index: 0"
      height="calc(100vh - 115px)"
      class="my-md-5"
      :show-audio=false
      :show-files=false
      :show-emojis=false
      :show-reaction-emojis=false
      :current-user-id="user.id"
      :rooms="rooms"
      :messages="messages"
      :message-actions = []
      @send-message="sendMessage"
      @fetch-messages="fetchMessages"
    />
   <!--  <chat-window
      style="z-index: 0"
      height="calc(100vh - 115px)"
      class="my-md-5"
      :currentUserId="currentUserId"
      :rooms="rooms"
      :messages="messages"
      :textMessages="textMessages"
      @sendMessage="sendMessage"
      :theme="$vuetify.theme.isDark ? 'dark' : 'light'"
    /> -->
    <!-- <v-dialog
      transition="dialog-top-transition"
      v-model="requestDialog"
      overlay-opacity=".6"
      max-width="575px"
    >
      <template v-slot:activator="{ on, attrs }">
        <template v-if="iconOnly">
          <v-btn v-bind="attrs" v-on="on" icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn></template
        >
      </template> -->
      <!-- <v-card>
        <v-card-title>Send conversation request to John!</v-card-title>
        <v-card-text>
          <p class="text-subtitle">
            Hello. I would like to discuss about
            <strong class="primary--text">{{
              request.topic || '"topic"'
            }}</strong>
            for my new work. Could you mentor me on this?
            <span v-if="request.date"
              >Could we connect on
              <strong class="primary--text">{{ request.date }}</strong
              >?</span
            >
          </p>

          <v-responsive>
            <v-text-field
              v-model="request.topic"
              @input="assertMaxChars"
              @keydown="limit($event, 'topic', 30)"
              placeholder="Topic for conversation"
              dense
              flat1
              hide-details
              rounded
              filled
              solo1
              clearable
              autofocus
            ></v-text-field>
          </v-responsive>
          <v-row>
            <v-col cols="12"
              ><span class="sub-title" style="position: relative; top: 8px"
                >Date</span
              ></v-col
            >
            <v-col>
              <v-dialog
                ref="dialog"
                v-model="dateModal"
                :return-value.sync="request.date"
                width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="request.date"
                    label="Choose a day?"
                    prepend-icon="mdi-calendar"
                    readonly
                    solo
                    clearable
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  @input="
                    $refs.dialog.save(request.date);
                    dateModal = false;
                  "
                  v-model="request.date"
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="dateModal = false">
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.dialog.save(request.date)"
                  >
                    Okay
                  </v-btn>
                </v-date-picker>
              </v-dialog>
            </v-col>
          </v-row>
          <small
            >You can only continue the conversation once John replies
            back.</small
          >
          <v-row>
            <v-col> </v-col>
            <v-spacer></v-spacer>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Cancel
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            :disabled="requestSendDisabled"
            @click="sendRequest"
          >
            Send
          </v-btn>
        </v-card-actions>
      </v-card> -->
    <!-- </v-dialog> -->
  </div>
</template>

<script>
import ChatWindow from "vue-advanced-chat";
import "vue-advanced-chat/dist/vue-advanced-chat.css";
const chatSocket = []


export default {
  components: {
    ChatWindow,
  },
  data() {
    return {
      text:"Test",
      rooms: [ ],
      messages: [ ],
      roomId: null,
      chatSocket: null,
      count: 0,
    }
  },
  methods: {
    setText(text) {
      this.text = text
    },
    getRooms() {
      axios.get('/api/rooms/')
      .then(response => {
        console.log(response)
        var rooms = []
        response.data.results.forEach(element => {
          var room = Object()
          room.roomId = element.id
          room.users = []
          element.participants.forEach(e => {
            var user = Object()
            user._id = e.id
            user.username = e.firstname
            user.avatar = e.avatar
            room.users.push(user)
            if(e.id != this.user.id)
            {
              room.roomName = user.username
            }
          })
          room.messages = []
          element.messages.forEach(e => {
            var message = Object()
            message._id = e.id
            message.content = e.content
            message.sender_id = e.created_by
            message.timestamp = e.timestamp
            message.system=false
            room.messages.push(message)
          })
          rooms.push(room)
        });
        console.log(rooms)
        this.rooms = rooms;
        if(this.roomId){
          this.getMessages(this.roomId)
        }
      })
    },
    getMessages(roomId){
      this.rooms.forEach(element => {
        if(element.roomId == roomId){
          this.messages = element.messages;
        }
      })
    },
    sendMessage ({ roomId, content, file, replyMessage }) { 
      this.chatSocket.send(JSON.stringify({
                'message': content,
                'room_id':roomId
            }));
     axios.post('/api/messages/',{room:roomId, content:content})
      .then(response => {
        if(response.status == 201)
        {        
          /* var message = Object()
          message._id = e.id
          message.content = e.content
          message.sender_id = e.created_by
          message.timestamp = e.timestamp
          message.system=false
          this.rooms.forEach(element => {
            if(element.roomId == roomId){
              element.messages.push(message)
              this.messages.push(message)
            }
          }) */
         }
      }) 
    } ,
    fetchMessages({room, options}){
      this.roomId = room.roomId
      this.getMessages(this.roomId)
      /* if(options && options.reset){
        this.getMessages(room.roomId)
      }
      else{
        this.getMessages(room.roomId)
      } */
    },
  },
  computed :{
    user(){
      return this.$store.state.user
    }
  },
  mounted () {
    this.getRooms()
  },
  beforeDestroy()
  {
    this.chatSocket.close()
  },
  created () {
    let v = this
    this.chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + 'qwe/'
    );
    this.chatSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      console.log(data)
      var message = Object()
      message._id = "temp"+v.count;
      v.count = v.count +1;
      var roomId = data.room_id
      message.content = data.message
      message.sender_id = data.created_by
      message.timestamp = data.timestamp
      message.system=false
      v.rooms.forEach(element => {
        if(element.roomId == roomId){
          element.messages.push(message)
          //v.messages.push(message)
        }
      }) 
      
    };
  }
}
</script>

<style>
.dialog-top-transition-enter,
.dialog-top-transition-leave-to {
  transform: translateY(-100%);
}
.room-footer {
  opacity: 0.25;
}
.infinite-status-prompt {
  opacity: 0;
}
</style>