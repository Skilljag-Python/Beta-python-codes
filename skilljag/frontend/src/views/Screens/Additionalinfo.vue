<template>
  <v-app>
    <v-app-bar app :color="$vuetify.theme.dark ? '' : 'white'" flat>
      <v-toolbar-title class="mx-3"
        ><router-link
          style1="position: absolute; top: 1px; left: 155px; z-index: 5"
          to="/online"
          ><v-img src="/images/text.png" max-width="116"></v-img></router-link
      ></v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn @click="logout" depressed text light>Logout</v-btn>
    </v-app-bar>

    <v-main class="">
      <v-container
        fluid
        :class="{ 'pa-0 ma-0': $vuetify.breakpoint.smAndDown }"
      >
        <v-stepper v-model="step">
          <v-stepper-header>
            <v-stepper-step step="1" :complete="step > 1">
              Basic Info.
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="2" :complete="step > 2">
              Almost Done
            </v-stepper-step>

            <v-divider></v-divider>
            <v-stepper-step step="3" :complete="step > 3">
              Profile
            </v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="4"> Complete </v-stepper-step>
          </v-stepper-header>
        </v-stepper>
        <v-card class="mx-auto mt-3 mb-10" max-width="700" v-if="dataLoading">
          <v-skeleton-loader
            type="article, image, actions"
          ></v-skeleton-loader>
        </v-card>
        <v-card
          v-show="!dataLoading"
          class="mx-auto mt-3 mb-10"
          max-width="700"
        >
          <v-card-title class="title font-weight-regular justify-space-between">
            <span>{{ currentTitle }}</span>
            <v-avatar
              color="primary lighten-2"
              class="subheading white--text"
              size="24"
              v-text="step"
            ></v-avatar>
          </v-card-title>

          <v-window touchless v-model="step">
            <v-window-item :value="1">
              <v-card-text>
                <v-form ref="form" v-model="validbasics1" lazy1-validation1>
                  <v-row>
                    <v-col cols="md-6">
                      <v-text-field
                        v-model="firstname"
                        :rules="nameRules"
                        label="First name*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="md-6">
                      <v-text-field
                        v-model="lastname"
                        :rules="nameRules"
                        label="Last name*"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-text-field
                    v-model="phone"
                    counter="10"
                    :rules="phoneRules"
                    label="Phone Number*"
                    required
                  >
                    <template v-slot:prepend>
                      <span style="padding-top: 4px">+91</span></template
                    >
                  </v-text-field>

                  <v-row>
                    <v-col cols="12" md="6"
                      ><v-autocomplete
                        v-model="state"
                        :items="states"
                        :disabled="statesLoading"
                        :loading="statesLoading"
                        @change="loadCities"
                        item-value="id"
                        item-text="title"
                        :rules="[(v) => !!v || 'State is required']"
                        label="State"
                        required
                      ></v-autocomplete
                    ></v-col>
                    <v-col cols="12" md="6"
                      ><v-autocomplete
                        v-model="city"
                        :items="cities"
                        :disabled="!cities.length"
                        :loading="citiesLoading"
                        item-value="id"
                        item-text="title"
                        :rules="[(v) => !!v || 'City is required']"
                        label="City"
                        required
                      ></v-autocomplete
                    ></v-col>
                  </v-row>

                  <v-text-field
                    v-model="education"
                    :rules1="phoneRules"
                    label="Highest Education (optional)"
                  ></v-text-field>
                  <v-text-field
                    v-model="institution"
                    :rules1="phoneRules"
                    label="Institution (optional)"
                  ></v-text-field>

                  <v-checkbox
                    v-model="checkbox"
                    :rules="[(v) => !!v || 'You must agree to continue!']"
                    label="Agree to terms and conditions*"
                    required
                  ></v-checkbox>
                </v-form>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-text>
                <v-radio-group required class="mb-3" v-model="q1work" row>
                  <template v-slot:label>
                    <div class="text-body-1">
                      Are you willing to work in a startup, projects, MSMEs or
                      other small ventures?
                    </div>
                  </template>
                  <v-radio label="No" value=false></v-radio>
                  <v-radio label="Yes" value=true></v-radio>
                  <v-scale-transition
                    ><v-icon
                      class="mx-0"
                      v-if="q1work=='true'"
                      color="yellow darken-3"
                      >mdi-check-bold
                    </v-icon>
                  </v-scale-transition>
                  <div
                    v-if="q1work=='true'"
                    class="text-body-2 mt-3 text-center w-100 grey--text"
                  >
                    Companies or individuals may find you for hire.
                  </div>
                </v-radio-group>
                <v-radio-group
                  class="mb-3"
                  @change="
                    (v) => {
                      if (v=='false') q3pay ='false';
                    }
                  "
                  v-model="q2mentor"
                  row
                >
                  <template v-slot:label>
                    <div class="text-body-1">
                      Are you willing to mentor startups and projects with your
                      intellectual skills and knowledge?
                    </div>
                  </template>
                  <v-radio label="No" value=false></v-radio>
                  <v-radio label="Yes" value=true></v-radio>
                  <v-scale-transition
                    ><v-icon class="mx-0" v-if="q2mentor" color="blue"
                      >mdi-check-bold
                    </v-icon>
                  </v-scale-transition>
                  <div
                    v-if="q2mentor=='true'"
                    class="text-body-2 mt-3 text-center w-100 grey--text"
                  >
                    Companies or individuals may ask you for help.
                  </div>
                </v-radio-group>
                <v-scale-transition>
                  <v-radio-group
                    class="mb-3"
                    v-if="q2mentor=='true'"
                    v-model="q3pay"
                    row
                  >
                    <template v-slot:label>
                      <div class="text-body-1">
                        Are you willing to mentor for free or paid?
                      </div> </template
                    ><br />
                    <v-radio label="No" value=false></v-radio>
                    <v-radio label="Yes" value=true></v-radio>
                    <v-scale-transition>
                      <v-icon class="mx-0" v-if="q3pay=='true'" color="green"
                        >mdi-check-bold</v-icon
                      ></v-scale-transition
                    >
                    <div
                      v-if="q3pay=='true'"
                      class="text-body-2 mt-3 text-center w-100 grey--text"
                    >
                      Companies or individuals may ask your guidance for free.
                    </div>
                  </v-radio-group></v-scale-transition
                >
                <v-fade-transition>
                  <div
                    v-if="(q1work=='true')||(q2mentor=='true')||(q3pay=='true')"
                    class="text-subtitle-1 text-center w-100"
                  >
                    Your badge
                    <span class="badge-icons mx-2">
                      <v-icon
                        v-if="q1work=='true'"
                        :color="['yellow darken-3', 'blue', 'green'][0]"
                        >mdi-check-bold</v-icon
                      >
                      <v-icon
                        v-if="q2mentor=='true'"
                        :color="['yellow darken-3', 'blue', 'green'][1]"
                        >mdi-check-bold</v-icon
                      >
                      <v-icon
                        v-if="q3pay=='true'"
                        :color="['yellow darken-3', 'blue', 'green'][2]"
                        >mdi-check-bold</v-icon
                      >
                    </span>
                  </div></v-fade-transition
                >
              </v-card-text>
            </v-window-item>
            <v-window-item :value="3">
              <v-card-text>
                <v-row class="text-center" align="center"
                  ><v-col cols="12">
                    <v-avatar
                      :color="avatar ? '' : 'grey darken-1 shrink'"
                      size="150"
                    >
                      <v-img v-if="avatar" :src="avatar"></v-img
                      ><span v-else class="white--text text-h4">{{
                        avatarText
                      }}</span>
                    </v-avatar>
                  </v-col>
                  <v-col cols="12">
                    <v-btn id="set-avatar" click
                      >{{ this.avatar ? "Update" : "Add" }} profile
                      picture</v-btn
                    >
                    <avatar-cropper
                      :labels="{ submit: 'Save', cancel: 'Cancel' }"
                      trigger="#set-avatar"
                      upload-url="/api/avatars/"
                      @uploading="handleUploading"
                      @uploaded="handleUploaded"
                      @completed="handleCompleted"
                      @error="handlerError"
                      upload-form-name="avatar"
                    />
                    <!-- <avatar-cropper
                      :labels="{ submit: 'Save', cancel: 'Cancel' }"
                      trigger="#set-avatar"
                      :upload-handler="cropperHandler"
                      :output-mime="cropperOutputMime"
                      :output-quality="0.8"
                      :output-options="cropperOutputOptions"
                      :cropper-options="cropperOptions"
                    /> -->
                    <!-- <avatar-cropper
                      :labels="{ submit: 'Save', cancel: 'Cancel' }"
                      :uploaded="updateUserAvatar"
                      upload-url="/api/images/me/"
                      trigger="#set-avatar"
                    /> -->
                  </v-col>
                </v-row>
                <!-- 3 -->
                <v-form ref="formp" v-model="validbasics3" lazy1-validation1>
                  <v-row>
                    <v-col cols="12">
                      <v-text-field
                        v-model="company"
                        label="Company (optional)"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        v-model="designation"
                        label="Designation (optional)"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        v-model="bio"
                        label="Bio (optional)"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-autocomplete
                    class="my-4"
                    rounded
                    required
                    v-model="values"
                    :items="valuesStore"
                    item-value="id"
                    item-text="title"
                    dense1
                    :search-input.sync="searchInput"
                    @change="searchInput = ''"
                    chips
                    small-chips
                    hide-details1
                    label="Values*"
                    multiple
                    :rules="[
                      (v) => v.length >= 2 || 'Please select at least two',
                      (v) => v.length <= 4 || 'Maximum limit of four.',
                    ]"
                  ></v-autocomplete>
                  <v-autocomplete
                    class="my-4"
                    rounded
                    required
                    v-model="skills"
                    :items="skillsStore"
                    item-value="id"
                    item-text="title"
                    dense1
                    :search-input.sync="searchInput"
                    @change="searchInput = ''"
                    chips
                    small-chips
                    hide-details1
                    label="Core Skills*"
                    multiple
                    :rules="[
                      (v) => v.length >= 2 || 'Please select at least two',
                      (v) => v.length <= 20 || 'Not more than twenty',
                    ]"
                  ></v-autocomplete>
                  <v-autocomplete
                    class="my-4"
                    rounded
                    required
                    v-model="askills"
                    :items="askillsStore"
                    item-value="id"
                    item-text="title"
                    dense1
                    :search-input.sync="searchInput"
                    @change="searchInput = ''"
                    chips
                    small-chips
                    hide-details1
                    label="Additional Skills*"
                    multiple
                    :rules="[
                      (v) => v.length <= 20 || 'Not more than twenty',
                    ]"
                  ></v-autocomplete>
                </v-form>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="4">
              <div class="pa-4 text-center">
                <v-img
                  class="mb-4"
                  contain
                  height="128"
                  src="/media/images/logo/color/icon/icon.png"
                ></v-img>
                <h3 class="title font-weight-light mb-2">
                  Welcome to Skilljag
                </h3>
                <span class="caption grey--text">Thanks for signing up!</span>
              </div>
            </v-window-item>
          </v-window>

          <v-divider></v-divider>

          <v-card-actions>
            <v-btn :disabled="step === 1" text @click="step--"> Back </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              :loading="nextLoading"
              v-if="step != 4"
              :disabled="disabledNext"
              color="primary"
              depressed
              @click="next"
            >
              Next
            </v-btn>
            <v-btn v-else color="primary" depressed href="/home"> Home </v-btn>
          </v-card-actions>
        </v-card>

        <div v-if="step==4" class="text-h6 text-center pb-3">
          <span class="gradient-text">Made in and for India with </span>
          <v-icon class="gradient-text">mdi-heart</v-icon>
        </div>
      </v-container>
      <v-snackbar v-model="hasSnack">
        {{ snackError }}

        <template >
          <v-btn color="purple" text @click="hasSnack = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </v-main></v-app
  >
</template>
<script>
// import store from '../../store.js'
import AvatarCropper from "vue-avatar-cropper";
import { CSRF_TOKEN } from "../../common/csrf_token"
import axios from 'axios'

export default {
  components: { AvatarCropper },
  data: () => ({
    validbasics1: false,
    validbasics3: false,
    hasSnack: false,
    snackError: "",
    searchInput: null,
    userdata: {},
    firstname: "",
    lastname: "",
    avatar: "",
    company: "",
    designation: "",
    bio:"",
    skillsStore: [],
    askillsStore: [],
    valuesStore: [],
    skills: [],
    askills: [],
    values: [],
    phone: "",
    email: "",
    state: null,
    city: null,
    states: [],
    cities: [],
    education: "",
    institution: "",
    q1work: null,
    q2mentor: null,
    q3pay: null,
    checkbox: false,
    waiting: false,

    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 30) || "Name has too many characters",
    ],
    phoneRules: [
      (v) => !!v || "Phone number is required",
      (v) => (v && !isNaN(v) && v.length == 10) || "Phone does not seem valid",
    ],
    emailRules: [
      (v) => !!v || "Email is required",
      (v) => /.+@.+\..+/.test(v) || "Email must be valid",
    ],

    step: 1,

    nextLoading: false,
    citiesLoading: false,
    statesLoading: false,
    dataLoading: false,
    valuesLoading: false,
    skillsLoading: false,
    askillsLoading: false
  }),
  methods: {
    handleUploading(form, xhr) {
      /* if(this.userdata.avatar!=null && this.userdata.avatar!="")
      {
        this.waiting = true;
        this.$http.delete('/api/avatars/me/')
        .then(response => {
          console.log("Hai");
          this.waiting = false;
        })
        .catch(error => {
          console.log("hello")
          this.waiting = false;
        });
        while(this.waiting)
        {console.log("Waiting");}
      } */
      
      form.append(
        "csrfmiddlewaretoken",
        CSRF_TOKEN
      );
      form.append(
        "user",
        this.userdata.id
      );
    },
    handleUploaded(response, form, xhr) {
      // update user avatar attribute
      console.log(response);
    },
    handleCompleted(response, form, xhr) {
      // xhr.status
        this.loadData();
    },
    handlerError(message, type, xhr) {
      if (type == "upload") {
        console.log(message);
      }
    },
    logout() {
      document.body.innerHTML += `<form id="logout-form" action="/logout" method="POST" class="d-none"><input type="hidden" name="_token" value="${
        document.querySelector('meta[name="csrf-token"]').content
      }"></form>`;
      document.getElementById("logout-form").submit();
    },
    validate() {
      this.$refs.form.validate();
      if (this.step == 3) {
        this.$refs.formp.validate();
      }
    },
    async step1submit() {
      var data = {
        firstname: this.firstname,
        lastname: this.lastname,
        email: this.email,
        state: this.state,
        city: this.city,
        phone: this.phone,
        highested: this.education,
        institution: this.institution,
      };
      this.submit(`/api/profiles/me/`, data);
    },
    async step2submit() {
      this.submit(`/api/profiles/me/`, {
        q1: this.q1work,
        q2: this.q2mentor,
        q3: this.q3pay,
      });
    },
    async step3submit() {
      this.submit(`/api/profiles/me/`, {
        company: this.company,
        designation: this.designation,
        bio: this.bio,
        values: this.values.id,
        skills: this.skills.id,
        askills: this.askills.id,
        completed_at: new Date
      });
    },
    async next() {
      this.validate();
      this.nextLoading = true;
      if (this.step == 1) {
        await this.step1submit();
      }
      if (this.step == 2) {
        await this.step2submit();
      }
      if (this.step == 3) {
        await this.step3submit();
      }
    },
    async submit(resource, data) {
      this.$http
        .patch(resource, data)
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            return this.step++;
          }
        })
        .catch((error) => {
          if (error.status === 422) {
            //this.errors = error.response.data;
            var data = error.response.data;
            if (data.errors) {
              this.snackError = data.errors[Object.keys(data.errors)[0]][0];
              this.hasSnack = true;
            }
          } else {
            console.log(error);
          }
        })
        .then(() => {
          this.nextLoading = false;
        });
    },
    async loadStates() {
      this.statesLoading = true;
      await this.$http.get(`/api/states/`).then((response) => {
        if (response.data !== "") {
          this.statesLoading = false;
          this.states = response.data;
        }
      });
    },
    async loadValues() {
      this.valuesLoading = true;
      await this.$http.get(`/api/values/`).then((response) => {
        if (response.data !== "") {
          this.valuesLoading = false;
          this.valuesStore = response.data;
        }
      });
    },
    async loadSkills() {
      this.skillsLoading = true;
      await this.$http.get(`/api/skills/`).then((response) => {
        if (response.data !== "") {
          this.skillsLoading = false;
          this.skillsStore = response.data;
        }
      });
    },
    async loadAskills() {
      this.askillsLoading = true;
      await this.$http.get(`/api/skills/`).then((response) => {
        if (response.data !== "") {
          this.askillsLoading = false;
          this.askillsStore = response.data;
        }
      });
    },    
    async loadCities(noreset) {
      if (!this.state) return;
      if (this.city && !noreset) this.city = "";
      this.citiesLoading = true;
      await this.$http
        .get(`/api/citys/?state=${this.state}`)
        .then((response) => {
          if (response.data !== "") {
            this.citiesLoading = false;
            this.cities = response.data;
          }
        });
    },
    async loadData() {
      this.dataLoading = true;
      await this.$http.get(`/api/profiles/me/`).then((response) => {
        if (response.data !== "") {
          this.dataLoading = false;
          this.userdata = response.data;
          var d = response.data;
          if (d.firstname) this.firstname = d.firstname;
          if (d.lastname) this.lastname = d.lastname;
          this.email = d.email;
          this.state = d.state;
          this.city = d.city;
          if (d.phone) this.phone = d.phone;
          this.education = d.highested;
          this.institution = d.institution;
          this.company = d.company;
          this.designation = d.designation;
          this.bio = d.bio;
          this.skills = d.skills;
          this.askills = d.askills;
          this.values = d.values;
          this.avatar = d.avatar;
          try {

              this.q1work = (d.q1).toString();
              this.q2mentor = (d.q2).toString();
              this.q3pay = (d.q3).toString();
          } catch (e) {}
        }
      });
    },
  },
  async created() {
    await this.loadData();
    await this.loadStates();
    await this.loadCities(true);
    await this.loadValues();
    await this.loadSkills();
    await this.loadAskills();
  },
  computed: {
    disabledNext() {
      // return false;
      switch (this.step) {
        case 1:
          return !this.validbasics1;
        case 2:
          return false
        case 3:
          return !this.validbasics3;
        case 4:
          return !true;
        default:
          return false;
      }
    },
    avatarText() {
      if (!this.firstname || !this.lastname) {
        return "You";
      }
      return ("" + this.firstname[0] + this.lastname[0]).toUpperCase();
    },
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Basic Info.";
        case 2:
          return "Your Badge";
        case 3:
          return "Profile";
        default:
          return "Account created";
      }
    },
  },
};
</script>
>

<style>
.gradient-text {
  background-color: #888;
  background-image: linear-gradient(45deg, #a759ef, #f4a700);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
}
</style>>

