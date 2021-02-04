<template>
  <div>
    <v-list-item :key="item.title">
      <v-list-item-avatar :size="$vuetify.breakpoint.mdAndUp ? 49 : 45">
        <v-img v-if="avatar" :src="avatar"></v-img>
        <span v-else class="grey--text">{{ avatarText }}</span>
      </v-list-item-avatar>

      <v-list-item-content :class="{ 'mr-3': $vuetify.breakpoint.mdAndUp }">
        <v-list-item-title  class="my-2" style="border-bottom: 1px solid #ccc"
          ><a :href="'/#/user/' + user.id">{{ userTitle
          }}</a><span class="float-right caption grey--text">{{ item.timestamp | moment("from", "now") }}</span></v-list-item-title
        >
        <div v-if="trending"
        class="text-h6"
          style="
            position: absolute;
            font-weight: 600;
            color: #a759ef;
            top: 78px;
            left: 22px;
          "
        >#{{trending}}</div>
        <v-list-item-subtitle
          style="-webkit-line-clamp: 7"
          v-html="item.description"
        ></v-list-item-subtitle>
        <div class="mt-3" style="width: 100%">
          <template v-if="item.images.length==1">
            <v-img
              :src="item.images[0].image"
              aspect-ratio="2"
              style="border-radius: 10px"
            ></v-img>
          </template>
          <template v-else-if="item.images.length > 1">
            <post-carousel v-bind:images=item.images />
          </template>
        </div>
      </v-list-item-content>

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
        @click="interestClick"
        value="left"
        text
        :color="item.interested == 'I' ? 'yellow darken-2' : ''"
      >
       <v-icon class="mr-1">mdi-alert-decagram-outline</v-icon>
        Interesting <span style="width: 40px;color:#000">({{ abbreviate_number(item.interest_count) }})</span>
      </v-btn>

      <v-btn value="center" text @click="commentsClick">
        <v-icon class="mr-1">mdi-comment-outline</v-icon>
        Comments ({{item.comment_count}})
      </v-btn>
      <multi-comments
          :isHidden=isHidden
          :comments=item.comments
          :post_id=item.id
          /> 

      <v-menu offset-y v-if="false">
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon text v-ripple="false">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-title
              ><v-icon class="mr-1">mdi-share-outline</v-icon>
              Share</v-list-item-title
            >
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
  props: ["item","trending"],
  data: () => ({
    slideGroup:'',
    overlay: false,
    isHidden: true,
    comments:[],
  }),
  computed: {
    user() {
      return this.item.created_by;
    },
    userTitle() {
     return this.user.firstname + " " + this.user.lastname;
    },
    avatarText() {
     return ("" + this.user.firstname[0]).toUpperCase();
    },
    avatar() {
      return this.user.avatar;
    },
  },
  methods: {
    interestClick(){
      if(this.item.interested == 'I')
      {
        this.item.interested = 'X';
        this.item.interest_count --;
        axios.delete(`/api/interests/`+this.item.interest_id+'/')
      }
      else
      {
        this.item.interested = 'I';
        this.item.interest_count ++;
        axios.post(`/api/interests/`, {interest: this.item.interested, post:this.item.id})
        .then(data => {
          console.log(data);
                      this.item.interest_id = data.data.id
                      

          })

      }

    },
    commentsClick() {
      /* if (!this.item.images.length) {
        return;
      }
      this.overlay = !this.overlay; */
      this.isHidden=!this.isHidden
    },
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