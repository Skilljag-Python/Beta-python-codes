<template>
  <div>
    <div>{{text}}</div>
    <chat-window
      style="z-index: 0"
      height="calc(100vh - 115px)"
      class="my-md-5"
      :currentUserId="currentUserId"
      :rooms="rooms"
      :messages="messages"
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

export default {
  components: {
    ChatWindow,
  },
  data() {
    return {
      text:"Test",
      rooms: [
        {
          roomId: 1,
          roomName: 'Austin',
          avatar: 'assets/imgs/people.png',
          unreadCount: 4,
          index: 3,
          users: [
            {
              _id: 4321,
              username: 'Austin',
              avatar: 'assets/imgs/snow.png',
            }
          ],
        }
      ],
      messages: [
      {
        _id: 7890,
        content: 'message 1',
        sender_id: 4321,
        username: 'John Doe',
        date: '13 November',
        timestamp: '10:20',
        system: false,
        disable_actions: true,
        disable_reactions: true,
        file: {
          name: 'My File',
          type: 'png',
          url: 'https://yt3.ggpht.com/ytc/AAUvwnjE8Rr34euMGiWeb8C5Q7K0WA8hx7-Cdm0oY4PoZw=s900-c-k-c0x00ffffff-no-rj'
        },
      }
    ],
      currentUserId: 1
    }
  },
  methods: {
    setText(text) {
      this.text = text
    },
    getRooms() {
      axios.get('/api/chats/')
      .then(response => {
        console.log(response)
        var rooms = []
        response.data.results.forEach(element => {
          var room = Object()
          room.roomId = element.id
          room.users = []
          element.participants.forEach(e => {
            var user = []
            user._id = e.id
            user.username = e.firstname
            user.avatar = e.avatar
            room.users.push(user)
            if(e.id != this.currentUserId)
            {
              room.roomName = user.username
            }
          })
          console.log(room)
          rooms.push(room)
        });
        console.log(rooms)
        this.rooms = rooms;
      })
    }
  },
  mounted () {
    //this.getRooms()
    this.setText("hello")
    let v = this
    const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + 'hai'
            + '/'
        );

    chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            console.log(data.message);
            v.setText(data.message);
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