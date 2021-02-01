   <template>
  <v-dialog v-model="dialog" overlay-opacity=".8" max-width="650px">
    <template v-slot:activator="{ on, attrs }">
      <template v-if="iconOnly">
        <v-btn v-bind="attrs" v-on="on" icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn></template
      >
      <template v-else>
        <v-responsive
          ripple
          dark
          v-bind="attrs"
          v-on="on"
          max-width="260"
          style="position: absolute; right: 108px"
        >
          <v-text-field
            placeholder="Search experts"
            prepend-inner-icon="mdi-magnify"
            readonly
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </template>
    </template>
    <v-card>
      <v-card-title> </v-card-title>
      <v-card-text>
        <v-container pa-0>
          <v-responsive class="pb-5">
            <v-text-field
              v-model="q"
              placeholder="Search for skill, person's name..."
              prepend-inner-icon="mdi-magnify"
              dense
              flat
              hide-details
              rounded
              solo-inverted
              clearable
              autofocus
              @keypress.enter="search"
            ></v-text-field>
          </v-responsive>

          <v-row>
            <v-col md="3" cols="12"
              ><span class="sub-title" style="position: relative; top: 8px"
                >Values required</span
              ></v-col
            >
            <v-col>
              <v-autocomplete
                rounded
                v-model="values"
                :items="valueStore"
                item-text="name"
                item-value="id"
                dense
                :search-input.sync="valuesInput"
                @change="
                  valuesInput = '';
                  values.length > 4 ? values.pop() : '';
                "
                :rules="[(v) => v.length <= 4 || 'Maximum limit of four.']"
                chips
                small-chips
                hide-details
                label="Values required"
                multiple
                solo
                clearable
              ></v-autocomplete>
            </v-col>
          </v-row>
          <v-row>
            <v-col md="3" cols="12"
              ><span class="sub-title" style="position: relative; top: 8px"
                >Location</span
              ></v-col
            >
            <v-col
              ><v-autocomplete
                v-model="location"
                loading="false"
                :items="locationStore"
                item-text="name"
                item-value="id"
                :search-input.sync="locationInput"
                cache-items
                solo
                rounded
                dense
                hide-no-data
                hide-details
                clearable
                label="Location"
              ></v-autocomplete
            ></v-col>
          </v-row>
        </v-container>
        <v-row>
          <v-col> </v-col>
          <v-spacer></v-spacer>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="dialog = false">
          Close
        </v-btn>
        <v-btn
          color="blue darken-1"
          text
          :disabled="searchDisabled"
          @click="search"
        >
          Search
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    valuesInput: null,
    locationInput: null,

    q: "",
    values: [],
    location: "",
  }),
  computed: {
    searchDisabled() {
      return !this.q || !this.q.length;
    },
    valueStore() {
      return this.$store.state.values;
    },
    locationStore() {
      var states = this.$store.state.states,
        cities = this.$store.state.cities,
        locationStore = [];
      if (!states.length || !cities.length) {
        return;
      }

      states.forEach(function (o) {
        locationStore.push({
          id: "s-" + o.id,
          name: o.name,
        });
      });
      cities.forEach(function (o) {
        locationStore.push({
          id: "c-" + o.id,
          name: o.name,
        });
      });

      return locationStore;
    },
  },
  methods: {
    search() {
      this.dialog = false;
      this.$router.push({
        path: "/search",
        query: { q: this.q, v: this.values.join(","), l: this.location },
      });
    },
  },
  mounted: function () {},
  props: { iconOnly: { type: Boolean, default: false } },
};
</script>