<template>
  <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="firstname"
        :counter="30"
        :rules="nameRules"
        label="First Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="lastname"
        :counter="30"
        :rules="nameRules"
        label="Last Name"
        required
      ></v-text-field>

      <v-radio-group v-model="gender">
          <v-radio
              label="Male"
              :value="M"   
          >Male</v-radio>
          <v-radio
              label="Female"
              :value="F"   
          ></v-radio>
      </v-radio-group>

      <v-date-picker v-model="birthdate"></v-date-picker>

      <v-select
        v-model="skills"
        :items="skillsList"
        :rules="skillRules"
        label="Skills"
        multiple
        chips
        required
      ></v-select>

      <v-select
        v-model="values"
        :items="valuesList"
        :rules="valueRules"
        label="Values"
        multiple
        chips
        required
      ></v-select>

      <v-select
        v-model="languages"
        :items="languagesList"
        :rules="languageRules"
        label="Languages"
        multiple
        chips
        required
      ></v-select>

      <v-textarea
        v-model="bio"
        :rules="bioRules"
        label="Bio"
        required
      ></v-textarea>
      <v-file-input
      v-model="avatar"
      :rules="avatarRules"
      accept="image/png, image/jpeg, image/bmp"
      prepend-icon="mdi-camera"
      label="Avatar"
    ></v-file-input>
  
      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
      >
        Validate
      </v-btn>
  
      <v-btn
        color="error"
        class="mr-4"
        @click="reset"
      >
        Reset Form
      </v-btn>
  
      <v-btn
        color="warning"
        @click="resetValidation"
      >
        Reset Validation
      </v-btn>
    </v-form>
</template>

<script>
export default {
    data: () => ({
        gender:null,
    valid: true,
    firstname: '',
    lastname: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length > 2) || 'Name must be less than 30 characters',
    ],
    skills: null,
    skillsList: [
      'Skill 1',
      'Skill 2',
      'Skill 3',
      'Skill 4',
    ],
    skillRules: [
      v => !!v || 'Skill is required'
    ],
    values:null,
    valuesList: [
      'Value 1',
      'Value 2',
      'Value 3',
      'Value 4',
    ],
    valueRules: [
      v => !!v || 'Value is required'
    ],
    languages:null,
    languagesList: [
      'language 1',
      'language 2',
      'language 3',
      'language 4',
    ],
    languageRules: [
      v => !!v || 'Language is required'
    ],
    bio:null,
    bioRules: [
      v => !!v || 'Bio is required'
    ],
    avatar:null,
    imageRules: [
      value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!'
    ],
    birthdate: new Date().toISOString().substr(0, 10),
  }),

  methods: {
    validate () {
      this.$refs.form.validate()
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
  },
}
</script>

<style>

</style>