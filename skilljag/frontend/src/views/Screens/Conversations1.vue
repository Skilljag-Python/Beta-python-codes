<template>
  <div>
    <v-sheet>
      <v-row style="min-height: 84vh" no-gutters>
        <v-col cols="3" style="border-right: 1px solid #eee">
          <v-div v-model="drawer" app width="300">
            <v-navigation-drawer
              v-model="drawer"
              absolute
              color="grey lighten-3"
              mini-variant
            >
              <v-avatar
                class="d-block text-center mx-auto mt-4"
                color="grey darken-1"
                size="36"
              ></v-avatar>

              <v-divider class="mx-3 my-5"></v-divider>

              <v-avatar
                v-for="n in 6"
                :key="n"
                class="d-block text-center mx-auto mb-9"
                color="grey lighten-1"
                size="28"
              ></v-avatar>
            </v-navigation-drawer>
            <v-system-bar color="orange" dark height="30">
              <v-icon>mdi-message</v-icon>
              <span class="text-subtitle-2">Recent</span>
              <v-spacer></v-spacer>
            </v-system-bar>
            <v-list style="overflow: auto" max-height="79vh" two-line1>
              <template v-for="(item, index) in recent">
                <v-subheader
                  v-if="item.header"
                  :key="item.header"
                  v-text="item.header"
                ></v-subheader>

                <v-divider
                  v-else-if="item.divider"
                  :key="index"
                  :inset="item.inset"
                ></v-divider>

                <v-list-item v-else :key="item.title" link>
                  <v-list-item-avatar>
                    <v-img :src="item.avatar"></v-img>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title v-html="item.title"></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="item.subtitle"
                    ></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </template>
            </v-list>
          </v-div>
        </v-col>

        <v-col style="position: relative" class="pa-3 pt-0 d-flex flex-column">
          <v-toolbar app1 clipped-right1 flat class="flex-grow-0" height="72">
            <v-spacer></v-spacer>

            <v-responsive max-width="156">
              <v-text-field
                dense
                flat
                hide-details
                rounded
                solo-inverted
              ></v-text-field>
            </v-responsive>
          </v-toolbar>
          <div class="flex-grow-1">
            <div data-v-3c464994="" class="container-scroll">
              <!---->
              <div data-v-3c464994="" class="messages-container">
                <div data-v-3c464994="" class="">
                  <div data-v-3c464994="" class="text-started">
                    Conversation started on 23 November 2020
                  </div>
                  <div
                    data-v-46b21138=""
                    data-v-3c464994=""
                    class="infinite-loading-container"
                  >
                    <div
                      data-v-46b21138=""
                      class="infinite-status-prompt"
                      style="display: none"
                    >
                      <div data-v-3c464994="" data-v-46b21138="">
                        <div
                          data-v-a3061d78=""
                          data-v-3c464994=""
                          class="container-top"
                          data-v-46b21138=""
                        >
                          <div data-v-a3061d78="" id="circle"></div>
                        </div>
                      </div>
                    </div>
                    <div
                      data-v-46b21138=""
                      class="infinite-status-prompt"
                      style=""
                    >
                      <div data-v-3c464994="" data-v-46b21138=""></div>
                    </div>
                    <div
                      data-v-46b21138=""
                      class="infinite-status-prompt"
                      style="display: none"
                    >
                      <div data-v-3c464994="" data-v-46b21138=""></div>
                    </div>
                    <div
                      data-v-46b21138=""
                      class="infinite-status-prompt"
                      style="
                        color: rgb(102, 102, 102);
                        font-size: 14px;
                        padding: 10px 0px;
                        display: none;
                      "
                    >
                      Opps, something went wrong :(
                      <br data-v-46b21138="" />
                      <button data-v-46b21138="" class="btn-try-infinite">
                        Retry
                      </button>
                    </div>
                  </div>
                  <span data-v-3c464994=""
                    ><div data-v-3c464994="">
                      <div data-v-e8c9dade="" data-v-3c464994="">
                        <!---->
                        <div data-v-e8c9dade="" class="line-new">
                          New messages
                        </div>
                        <div data-v-e8c9dade="" class="message-box">
                          <div data-v-e8c9dade="" class="message-container">
                            <div
                              data-v-e8c9dade=""
                              class="message-card message-highlight"
                            >
                              <!----><!---->
                              <div data-v-e8c9dade="">
                                <div data-v-e8c9dade="" class="">
                                  <div>
                                    <span target="_blank" class=""
                                      ><!---->ciyiheb114@ibrilo.comm</span
                                    >
                                  </div>
                                </div>
                              </div>
                              <div data-v-e8c9dade="" class="text-timestamp">
                                <!----><span data-v-e8c9dade="">17:43</span
                                ><!---->
                              </div>
                              <div
                                data-v-e8c9dade=""
                                class="options-container"
                                style="width: 70px"
                              >
                                <span data-v-e8c9dade=""
                                  ><div
                                    data-v-e8c9dade=""
                                    class="blur-container"
                                  ></div>
                                  <div
                                    data-v-e8c9dade=""
                                    class="svg-button message-options"
                                  >
                                    <svg
                                      data-v-e8c9dade=""
                                      xmlns="http://www.w3.org/2000/svg"
                                      xmlns:xlink="http://www.w3.org/1999/xlink"
                                      version="1.1"
                                      width="24"
                                      height="24"
                                      viewBox="0 0 24 24"
                                    >
                                      <path
                                        id="chat-icon-dropdown-message"
                                        d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"
                                      ></path>
                                    </svg>
                                  </div>
                                  <div
                                    data-v-0b9bd2d4=""
                                    data-v-e8c9dade=""
                                    class="wrapper message-reactions"
                                    style="right: 30px"
                                  >
                                    <div data-v-0b9bd2d4="">
                                      <div
                                        data-v-0b9bd2d4=""
                                        class="svg-button button-reaction"
                                      >
                                        <svg
                                          data-v-0b9bd2d4=""
                                          xmlns="http://www.w3.org/2000/svg"
                                          xmlns:xlink="http://www.w3.org/1999/xlink"
                                          version="1.1"
                                          width="24"
                                          height="24"
                                          viewBox="0 0 24 24"
                                        >
                                          <path
                                            id="chat-icon-emoji-reaction"
                                            d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"
                                          ></path>
                                        </svg>
                                      </div>
                                      <!---->
                                    </div>
                                  </div></span
                                >
                              </div>
                              <!---->
                            </div>
                            <span data-v-e8c9dade=""></span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div data-v-3c464994="">
                      <div data-v-e8c9dade="" data-v-3c464994="">
                        <!----><!---->
                        <div
                          data-v-e8c9dade=""
                          class="message-box offset-current"
                        >
                          <div
                            data-v-e8c9dade=""
                            class="message-container message-container-offset"
                          >
                            <div
                              data-v-e8c9dade=""
                              class="message-card message-current"
                            >
                              <!----><!---->
                              <div data-v-e8c9dade="">
                                <div data-v-e8c9dade="" class="">
                                  <div>
                                    <span target="_blank" class=""
                                      ><!---->ciyiheb114@ibrilo.comm</span
                                    >
                                  </div>
                                </div>
                              </div>
                              <div data-v-e8c9dade="" class="text-timestamp">
                                <!----><span data-v-e8c9dade="">19:51</span
                                ><span data-v-e8c9dade=""
                                  ><svg
                                    data-v-e8c9dade=""
                                    xmlns="http://www.w3.org/2000/svg"
                                    xmlns:xlink="http://www.w3.org/1999/xlink"
                                    version="1.1"
                                    width="24"
                                    height="24"
                                    viewBox="0 0 24 24"
                                    class="icon-check"
                                  >
                                    <path
                                      id="chat-icon-checkmark"
                                      d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"
                                    ></path></svg
                                ></span>
                              </div>
                              <div
                                data-v-e8c9dade=""
                                class="options-container"
                                style="width: 70px"
                              >
                                <span data-v-e8c9dade=""></span>
                              </div>
                              <!---->
                            </div>
                            <span data-v-e8c9dade=""></span>
                          </div>
                        </div>
                      </div></div
                  ></span>
                </div>
              </div>
            </div>
          </div>

          <v-footer absolute color="transparent" height="72" inset>
            <v-text-field
              background-color="grey lighten-1"
              dense
              flat
              hide-details
              rounded
              solo
            ></v-text-field>
          </v-footer>
        </v-col>
        <v-col cols="3" style="border-left: 1px solid #eee">
          <v-div app clipped right>
            <v-system-bar color="purple" dark height="30">
              <v-icon>mdi-heart</v-icon>
              <span class="text-subtitle-2">Saved</span>
              <v-spacer></v-spacer>
            </v-system-bar>
            <v-list style="overflow: auto" max-height="79vh" two-line1>
              <template v-for="(item, index) in saved">
                <v-subheader
                  v-if="item.header"
                  :key="item.header"
                  v-text="item.header"
                ></v-subheader>

                <v-divider
                  v-else-if="item.divider"
                  :key="index"
                  :inset="item.inset"
                ></v-divider>

                <v-list-item v-else :key="item.title" link>
                  <v-list-item-avatar>
                    <v-img :src="item.avatar"></v-img>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title v-html="item.title"></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="item.subtitle"
                    ></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </template>
            </v-list>
          </v-div>
        </v-col>
      </v-row>
    </v-sheet>
    <div></div>
  </div>
</template>

<script>
import ChatWindow from "vue-advanced-chat";
import "vue-advanced-chat/dist/vue-advanced-chat.css";

export default {
  components: { ChatWindow },
  data() {
    return {
      recent: [
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
          title: "Brunch this weekend?",
          subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
          title: "Oui oui",
          subtitle:
            '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
          title: "Birthday gift",
          subtitle:
            '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
          title: "Recipe to try",
          subtitle:
            '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
      saved: [
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
          title: "Brunch this weekend?",
          subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
          title: "Oui oui",
          subtitle:
            '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
          title: "Birthday gift",
          subtitle:
            '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        { divider: true, inset: true },
        {
          avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
          title: "Recipe to try",
          subtitle:
            '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
      drawer: null,
      
      alwaysScrollToBottom: false, 
      messageStyling: true,
    };
  },
  methods: {

  },
};
</script>
