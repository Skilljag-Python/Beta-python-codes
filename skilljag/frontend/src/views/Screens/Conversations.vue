<template>
  <div>
    <chat-window
      style="z-index: 0"
      height="calc(100vh - 115px)"
      class="my-md-5"
      :currentUserId="currentUserId"
      :rooms="rooms"
      :messages="messages"
      :textMessages="textMessages"
      @sendMessage="sendMessage"
      :theme="$vuetify.theme.isDark ? 'dark' : 'light'"
    />
    <v-dialog
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
      </template>
      <v-card>
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
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import ChatWindow from "vue-advanced-chat";
import "vue-advanced-chat/dist/vue-advanced-chat.css";

export default {
  components: {
    ChatWindow,
  },
  methods: {
    sendRequest() {
      this.requestDialog = false;
      this.messages.push({
        _id: 7890,
        content: this.requestMessage,
        sender_id: 1234,
        username: "Harikrishnan R",
        date: "13 November",
        timestamp: "10:20",
        saved: true,
        distributed: true,
        seen: !true,
        disable_actions: false,
        disable_reactions: false,
      });
      this.rooms[0].lastMessage = {
        content: this.requestMessage,
        sender_id: 1234,
        username: "Harikrishnan R",
        timestamp: "10:30",
        date: 123242424,
        saved: true,
        distributed: false,
        seen: false,
        new: true,
      };
    },
    assertMaxChars: function () {
      if (this.request.topic.length >= 30) {
        this.request.topic = this.request.topic.substring(0, 30);
        return false;
      }
    },
    limit(event, dataProp, limit) {
      if (this["request"][dataProp].length >= limit) {
        event.preventDefault();
      }
    },
    async sendMessage({ content, roomId, file, replyMessage }) {
      var d = new Date();

      const message = {
        _id: 7890,
        content: content,
        sender_id: this.currentUserId,
        username: "John Doe",
        date: "13 November",
        timestamp: d.getHours() + ":" + d.getMinutes(),
        saved: !true,
        distributed: !true,
        seen: !true,
        disable_actions: false,
        disable_reactions: false,
      };

      if (file) {
        message.file = {
          name: file.name,
          size: file.size,
          type: file.type,
          url: file.localUrl,
        };
      }
      if (replyMessage) {
        message.replyMessage = {
          _id: replyMessage._id,
          content: replyMessage.content,
          sender_id: replyMessage.sender_id,
        };
        if (replyMessage.file) {
          message.replyMessage.file = replyMessage.file;
        }
      }
      // const { id } = await this.messagesRef(roomId).add(message);
      if (file) this.uploadFile({ file, messageId: id, roomId });
      this.messages.push(message);
    },
  },
  computed: {
    requestSendDisabled() {
      return this.request.topic.length > 30 || this.request.topic.length < 4;
    },
    requestMessage() {
      return (
        `Hello. I would like to discuss about ${this.request.topic} for my new work. Could you mentor me on this?` +
        (this.request.date ? ` Could we connect on ${this.request.date}?` : "")
      );
    },
  },
  mounted: function () {
    setTimeout(() => {
      this.requestDialog = true;
    }, 500);
  },
  data() {
    return {
      requestDialog: !true,
      dateModal: false,
      request: {
        topic: "",
        date: "",
      },
      rooms: [
        {
          roomId: 1,
          avatar: "",
          roomName: "John",
          unreadCount: 0,
          // lastMessage: {
          //   content: "Yes",
          //   sender_id: 1234,
          //   username: "John Doe",
          //   timestamp: "10:20",
          //   date: 123242424,
          //   saved: true,
          //   distributed: false,
          //   seen: false,
          //   new: true,
          // },
          users: [
            {
              _id: 1234,
              username: "John Doe",
              status: {
                state: "online",
                last_changed: "today, 14:30",
              },
            },
            {
              _id: 4321,
              username: "John",
              status: {
                state: "offline",
                // last_changed: "14 July, 20:00",
                last_changed: "",
              },
            },
          ],
          typingUsers: [4321],
        },
      ],
      messages: [],
      messages1: [
        {
          _id: 7890,
          content: "message 1",
          sender_id: 1234,
          username: "John Doe",
          date: "13 November",
          timestamp: "10:20",
          saved: true,
          distributed: true,
          seen: true,
          disable_actions: false,
          disable_reactions: false,
          file: {
            name: "My File",
            size: 67351,
            type: "png",
            url: "http://skilljag.test/images/p3.jpg",
          },
          reactions: {
            wink: [
              1234, // USER_ID
              4321,
            ],
            laughing: [1234],
          },
        },
        {
          _id: 7891,
          content: "Yes",
          sender_id: 1235,
          username: "Doe John",
          date: "13 November",
          timestamp: "10:20",
          saved: true,
          distributed: true,
          seen: true,
          disable_actions: false,
          disable_reactions: false,
          reactions: {
            laughing: [1234],
          },
        },
      ],
      textMessages: { ROOMS_EMPTY: "No Conversations" },
      currentUserId: 1234,
    };
  },
};
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