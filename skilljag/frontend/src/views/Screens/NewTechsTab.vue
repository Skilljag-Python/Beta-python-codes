<template>
  <v-row :no-gutters="$vuetify.breakpoint.smAndDown">
    <v-col cols="12" sm="2">
      <v-sheet
        rounded="lg"
        min-height="268"
        style="
          min-height: 268px;
          position: sticky;
          top: 75px;
          overflow-y: auto;
          max-height: 84vh;
        "
        v-if="false"
      >
        <div class="text-subtitle-1 pa-3">Trending Posts</div>
        <v-list three-line>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="7">
      <v-sheet rounded="lg" class="mb-3 pa-1 px-3">
        <v-row justify="center">
          <v-dialog v-model="dialog" max-width="700px">
            <template v-slot:activator="{ on, attrs }">
              <v-container class="px-10">
                <v-row align="center" ripple dark v-bind="attrs" v-on="on">
                  <v-col class="flex-grow-0">
                    <avatar size="40"></avatar>
                  </v-col>
                  <v-col
                    ><h1
                      class="heading"
                      style="text-align: center; width: 100%"
                    >
                      <v-textarea
                        hide-details
                        rows="2"
                        no-resize
                        readonly
                        solo
                        name="input-7-4"
                        label="Post your NEW TECH..."
                      ></v-textarea>
                    </h1>
                  </v-col>
                </v-row>
              </v-container>
            </template>
            <v-card>
              <v-card-title>
                <v-row align="center" class="spacer" no-gutters>
                  <v-col cols="4" sm="2" md="1">
                    <avatar size="40"></avatar>
                  </v-col>

                  <v-col>
                    <strong style="font-size:16px">{{ $store.state.user.firstname }}</strong>
                  </v-col>

                  <v-col class="d-flex mx-2 px-0 mr-0">
                    <v-autocomplete
                      :items="categoryStore"
                      item-value="id"
                      item-text="name"
                      label="Category Select"
                      dense
                      flat
                      hide-details
                      solo-inverted
                      rounded
                    ></v-autocomplete>
                  </v-col>
                </v-row>
              </v-card-title>
              <v-card-text>
                <v-divider></v-divider>
                <v-container>
                  <v-textarea
                    hide-details1
                    rows="6"
                    solo
                    autofocus
                    name="input-7-4"
                    counter="400"
                    label="Description (max 400 words)..."
                  ></v-textarea>
                  <v-row v-if="newPost.images">
                    <v-col cols="6" v-for="n in newPost.images" :key="n">
                      <v-img
                        style="border-radius: 4px"
                        :src="n"
                        :src1="item"
                        width="100%"
                        aspect-ratio1="1.8"
                      ></v-img>
                    </v-col>
                  </v-row>
                </v-container>
                <small
                  >This info will be subject to review before it is visible to
                  others.</small
                >
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="dummy.imagesOn = true" icon color="black">
                  <v-icon>mdi-paperclip</v-icon>
                </v-btn>
                <v-btn color="blue darken-1" text @click="dialog = false">
                  Close
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    dummy.enabled = true;
                    dialog = false;
                  "
                >
                  Post
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </v-sheet>
      <v-sheet rounded="lg" class="mb-3">
        <v-container class="ma-0 py-0">
          <v-row align="center" class="px-4">
            <!-- <v-col cols="12" class="py-2" :key="index"> -->

            <v-responsive max-width="190">
              <v-select
                v-model="listType"
                :items="listTypes"
                menu-props="auto"
                label="Type"
                single-line
                solo-inverted
                flat
                rounded
                dense
                hide-no-data
                hide-details
              ></v-select
            ></v-responsive>

            <v-responsive class="my-1 mx-2" max-width="210">
              <v-text-field
                placeholder="Search"
                prepend-inner-icon="mdi-magnify"
                dense
                flat
                hide-details
                solo-inverted
                rounded
              ></v-text-field>
            </v-responsive>
            <v-col class="d-flex mx-2 px-0 mr-0">
              <v-autocomplete
                :items="filters"
                label="Filter"
                dense
                flat
                hide-details
                solo-inverted
                rounded
              ></v-autocomplete>
            </v-col> </v-row
        ></v-container>
      </v-sheet>

      <v-sheet min-height="70vh" style="overflow: hidden">
        <v-list three-line>
          <template v-if="dummy.enabled">
            <nt-post :item="dummy"></nt-post>
            <v-divider :inset="true"></v-divider>
          </template>
          <template v-for="(item, index) in items">
            <v-subheader
              v-if="item.header"
              :key="item.header + index"
              v-text="item.header"
            ></v-subheader>

            <v-divider
              v-else-if="item.divider"
              :key="index"
              :inset="item.inset"
            ></v-divider>

            <nt-post v-else :item="item" :key="index"></nt-post>
          </template>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="3">
      <v-sheet
        rounded="lg"
        min-height="268"
        style="
          min-height: 468px;
          position: sticky;
          top: 75px;
          overflow-y: auto;
          max-height: 84vh;
          opacity: 0.6;
        "
      >
        <h5 class="pa-10" v-show="false">Ad</h5>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
export default {
  data: () => ({
    dummy: {enabled:true, imagesOn:true },
    dialog: false,
    items: [
      {
        interesting: false,
        images: ["/images/p3.jpg"],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Marcus Das",
        subtitle: `<div class="text--primary">Building automatic electric car</div> Why wait for Tesla to come to India? I have been researching on lithium ion battery for past 3 years and have devoloped a stable battery that can pull a car. I am planning to make the car we have been longing for. If you have the same vision as mine and have the skill to contribute towards the idea.`,
      },
      { divider: true, inset: true },
      {
        interesting: true,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Oui oui",
        subtitle:
          '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 8,
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Birthday gift",
        subtitle:
          '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Recipe to try",
        subtitle:
          '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      },
      {
        interesting: false,
        images: [],
        imagecount: 9,
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Brunch this weekend?",
        subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Oui oui",
        subtitle:
          '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Birthday gift",
        subtitle:
          '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Recipe to try",
        subtitle:
          '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Brunch this weekend?",
        subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Oui oui",
        subtitle:
          '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Birthday gift",
        subtitle:
          '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Recipe to try",
        subtitle:
          '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Brunch this weekend?",
        subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Oui oui",
        subtitle:
          '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Birthday gift",
        subtitle:
          '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        images: [],
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Recipe to try",
        subtitle:
          '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      },
    ],
    items10: [
      { header: "#Top 10" },
      {
        interesting: false,
        imageless: false,
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Brunch this weekend?",
        subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
      },
      { divider: true, inset: true },
      {
        interesting: true,
        imageless: false,
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
        subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
      },
      { divider: true, inset: true },
      {
        interesting: false,
        imageless: true,
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Oui oui",
        subtitle:
          '<span class="text--primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        imageless: false,
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Birthday gift",
        subtitle:
          '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
      },
      { divider: true, inset: true },
      {
        interesting: false,
        imageless: false,
        imagecount: 1,
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Recipe to try",
        subtitle:
          '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
      },
    ],
    listTypes: ["Trending", "Recent", "Featured"],
    listType: "Recent",
    newPost: {
      body: "",
      values: [],
      skills: [],
      skillStore: ["Robotics", "Artificial Intellegence"],
      valueStore: ["Innovative", "Hard Working"],
    },
  }),
  methods: {
  },
  computed: {
    categoryStore() {
      return this.$store.state.categories;
    },
  },
};
</script>