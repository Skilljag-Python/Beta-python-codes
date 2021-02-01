<template>
  <div>
    <v-list-item :key="item.title">
      <v-list-item-avatar :size="$vuetify.breakpoint.mdAndUp ? 49 : 45">
        <v-img :src="item.avatar"></v-img>
      </v-list-item-avatar>

      <v-list-item-content class="mr-3">
        <v-list-item-title
          v-html="item.title"
          class="my-2"
          style="border-bottom: 1px solid #ccc"
        ></v-list-item-title>
        <v-list-item-subtitle
          style="-webkit-line-clamp: 15; white-space: pre-wrap"
          v-html="item.subtitle"
        ></v-list-item-subtitle>
        <div class="mt-3" style="width: 100%">
          <template>
            <v-img
              :src="item.images[0].image"
              style="
                width: 95%;
                height: 245px;
                border-radius: 10px;
                object-fit: cover;
              "
            ></v-img>
            <v-slide-group
              style="width: 95%"
              v-if="item.images.length > 1"
              v-model="slideGroup"
              class="pa-4"
              mandatory
              show-arrows
            >
              <v-slide-item
                v-for="(item, index) in item.images"
                :key="item"
                v1-slot="{ active, toggle }"
              >
                <v-img
                  style="border-radius: 4px"
                  :class="'mx-2' + (index == 0 ? ' ml-0' : '')"
                  :src="item.image"
                  width="30"
                  aspect-ratio="1.8"
                ></v-img>
              </v-slide-item>
            </v-slide-group>
          </template>
        </div>
        <v-col v-if="false" cols="12" class="py-2">
          <v-btn
            @click="
              (e) => {
                item.interested = !item.interested;
              }
            "
            value="left"
            text
            :color="item.interested ? 'yellow darken-2' : ''"
          >
            <v-icon class="mr-1">mdi-alert-decagram-outline</v-icon>
            Interesting ({{ 0 }})
          </v-btn>
          <v-btn value="center" text @click="respondDialog = true">
            <v-icon class="mr-1">mdi-comment-outline</v-icon>
            Respond
          </v-btn>

          <v-btn value="right" text>
            <v-icon class="mr-1">mdi-share-outline</v-icon>
            Share
          </v-btn>

          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn v-bind="attrs" v-on="on" icon text v-ripple="false">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title>Report</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-col>
      </v-list-item-content>

      <v-dialog v-model="respondDialog" max-width="750px">
        <v-card>
          <v-card-title>
            <v-radio-group v-model="response.type">
              <template v-slot:label>
                <div>Your <strong>response</strong></div>
              </template>
              <v-radio value="contribute">
                <template v-slot:label>
                  <div>
                    I want to
                    <strong class="success--text">contribute</strong> to the
                    idea
                  </div>
                </template>
              </v-radio>
              <v-radio value="work">
                <template v-slot:label>
                  <div>
                    I want to
                    <strong class="primary--text">work</strong>
                    in the startup / project
                  </div>
                </template>
              </v-radio>
              <v-radio value="invest">
                <template v-slot:label>
                  <div>
                    I want to
                    <strong class="primary--text"> invest</strong>
                  </div>
                </template>
              </v-radio>
              <v-radio value="dispute">
                <template v-slot:label>
                  <div>
                    <strong class="primary--text">Dispute</strong>
                  </div>
                </template>
              </v-radio>
            </v-radio-group>
          </v-card-title>
          <v-card-text>
            <v-textarea
              hide-details
              rows="6"
              solo
              name="input-7-4"
              :label="responseLabels[response.type]"
            ></v-textarea>
            <small
              >This will be sent as a message to post creators. They will review
              it.</small
            >
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="blue darken-1" text @click="respondDialog = false">
              Send
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-overlay
        dark="false"
        :value="overlay"
        v-if="overlay"
        style="backdrop-filter: blur(3px)"
      >
        <v-container>
          <v-row justify="center" no-gutters @click="overlay = !overlay">
            <v-col cols="7">
              <v-sheet rounded="sm" min-height="268" style="min-height: 268px">
                <v-img
                  :src="item.images[0].image"
                  width="100%"
                  height="86vh"
                  aspect-ratio1="1.8"
                ></v-img>
              </v-sheet>
            </v-col>
            <v-col cols="5">
              <v-sheet height="86vh" dark="false">
                <v-list-item :key="item.title">
                  <v-list-item-avatar>
                    <v-img :src="item.avatar"></v-img>
                  </v-list-item-avatar>

                  <v-list-item-content class="mr-3">
                    <v-col>
                      <v-list-item-title v-html="item.title"></v-list-item-title
                      ><v-list-item-subtitle
                        style="color: #385898"
                        v-html="
                          `Follow <span class='px-5' style='color:#888;'>12 November</span>`
                        "
                      ></v-list-item-subtitle>
                    </v-col>
                    <v-col cols="auto">
                      <v-btn icon color="grey">
                        <v-icon>mdi-dots-vertical</v-icon>
                      </v-btn>
                    </v-col>
                  </v-list-item-content>
                </v-list-item>
                <p class="pa-5">
                  <v-list-item-subtitle
                    style="-webkit-line-clamp: 6; color: #1c1e21"
                    v-html="item.subtitle"
                  ></v-list-item-subtitle>
                </p>
                <v-divider></v-divider>
                <span class="pa-3 px-4 caption">
                  You and 545 others found this interesting.
                </span>
                <v-divider></v-divider>
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-overlay>
    </v-list-item>
    <v-col cols="12" class="py-2 text-center">
      <v-btn
        @click="
          (e) => {
            item.interested = !item.interested;
          }
        "
        value="left"
        text
        :color="item.interested ? 'yellow darken-2' : ''"
      >
        <v-icon class="mr-1">mdi-alert-decagram-outline</v-icon>
        Interesting
        <span style="width: 40px; color: #000"
          >({{ abbreviate_number(interesting_count) }})</span
        >
      </v-btn>
      <v-btn value="center" text @click="respondDialog = true">
        <v-icon class="mr-1">mdi-comment-outline</v-icon>
        Respond
      </v-btn>

      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon text v-ripple="false">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-icon class="mr-1">mdi-share-outline</v-icon>
            Share
          </v-list-item>
          <v-list-item>
            <v-list-item-title>Report</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-col>
  </div>
</template>

<script>
export default {
  props: ["item"],
  data: () => ({
    slideGroup: "",
    overlay: false,
    respondDialog: false,
    interesting_count: 0,
    response: {
      type: "contribute",
    },
    responseLabels: {
      contribute: "Tell us, how will you contribute to the idea?",
      work: "Why work",
      invest: "Why invest",
      dispute:
        "Enter the reason for dispute and the organization will review, note: the query will only be visible to the post authors",
    },
  }),
  methods: {
    abbreviate_number(num, fixed) {
      if (num === null) {
        return null;
      } // terminate early
      if (num === 0) {
        return "0";
      } // terminate early
      fixed = !fixed || fixed < 0 ? 0 : fixed; // number of decimal places to show
      var b = num.toPrecision(2).split("e"), // get power
        k = b.length === 1 ? 0 : Math.floor(Math.min(b[1].slice(1), 14) / 3), // floor at decimals, ceiling at trillions
        c =
          k < 1
            ? num.toFixed(0 + fixed)
            : (num / Math.pow(10, k * 3)).toFixed(1 + fixed), // divide by power
        d = c < 0 ? c : Math.abs(c), // enforce -0 is 0
        e = d + ["", "K", "M", "B", "T"][k]; // append power
      return e;
    },
  },
  computed: {},
  watch1: {
    overlay(val) {
      val &&
        setTimeout(() => {
          this.overlay = false;
        }, 3000);
    },
  },
};
</script>