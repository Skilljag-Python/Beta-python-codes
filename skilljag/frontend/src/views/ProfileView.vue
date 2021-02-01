<template>
    <div class="py-5">
        
        <v-sheet rounded="lg">
            <v-container class="px-16 py-10 p-relative">
                <edit-button
                    :active="editEnabled"
                    @on-click="editEnabled = !editEnabled"
                ></edit-button>
                <div v-if="userLoading">
                    <v-skeleton-loader
                        class="mx-au to"
                        max-width1="700"
                        type="list-item-avatar, list-item-two-line"
                        v-for="n in 1"
                        :key="n"
                    ></v-skeleton-loader>
                </div>
                <v-row v-else>
                    <v-col class="flex-grow-0 p-relative">
                        <v-avatar color="grey darken-2" size="137" rounded="lg">
                            <v-img v-if="avatar" :src="avatar"></v-img>
                            <span v-else class="white--text text-h2">{{ avatarText }}</span>
                        </v-avatar>
                        <edit-button
                            v-if="editEnabled"
                                @on-click="editEnabled = !editEnabled"
                        ></edit-button>
                    </v-col>

                    <v-col class="align-self-center p-relative">
                        <span class="text-h6">{{ fullName }}</span>
                        <div class="text-body-2 grey--text">{{ values }}</div>
                        <div v-if="user.highest_ed" class="text-body-2 grey--text">
                            <v-icon size="20" class="mr-1">mdi-school-outline</v-icon>
                            {{ user.highest_ed }}
                        </div>
                        <div v-if="user.designation" class="text-body-2 grey--text">
                        <v-icon size="20" class="mr-1">mdi-briefcase-outline</v-icon>
                            {{ user.designation }}
                        </div>
                        <div v-if="user.company" class="text-body-2 grey--text">
                        <v-icon size="20" class="mr-1">mdi-office-building-outline</v-icon>
                            {{ user.company }}
                        </div>
                        <div v-if="userState" class="text-body-2 grey--text">
                            <v-icon size="20" class="mr-1">mdi-map-marker-outline</v-icon>
                            {{ userState }}
                        </div>
                        <edit-button
                            v-if="editEnabled"
                            @on-click="editEnabled = !editEnabled"
                        ></edit-button>
                    </v-col> 

                    <v-spacer></v-spacer> 
                    <v-col cols="auto" class="align-self-center">
                        <div>
                            <v-btn depressed text color="grey darken-1">
                                {{user.followers}}
                            </v-btn>
                        </div>
                        <div>
                            <v-btn depressed text color="grey darken-1"> Followers </v-btn>
                        </div>    
                    </v-col>  
                    <div>
                        <v-col class="align-self-center flex-grow-0">
                            <badge :badge="user.badge_type"></badge>
                        </v-col>
                    </div>
                
                </v-row>
            </v-container>
        </v-sheet>

        <v-sheet rounded="lg" class="mt-5">
            
            <div v-if="userLoading">
                <v-skeleton-loader
                    class="mx-auto"
                    type="list-item-two-line"
                    v-for="n in 1"
                    :key="n"
                ></v-skeleton-loader>
            </div>
            <v-container v-else class="px-4 p-relative">
                Skills
                <div>
                    <v-chip
                        v-for="(item, index) in user.skills"
                        class="ma-2"
                        :color="index < 4 ? 'purple' : ''"
                        outlined
                        large
                        :key="index"
                    >
                        {{ item.name }}
                    </v-chip>
                </div>
                <edit-button
                    v-if="editEnabled"
                    @on-click="editEnabled = !editEnabled"
                ></edit-button>
            </v-container>   
        </v-sheet>

        <v-sheet rounded="lg" class="mt-5">
            <div v-if="userLoading">
                <v-skeleton-loader
                    class="mx-auto"
                    type="list-item-two-line"
                    v-for="n in 1"
                    :key="n"
                ></v-skeleton-loader>
            </div>
            <v-container v-else class="px-4 p-relative">
                About
                <p v-if="user.about">
                    {{ user.about }}
                </p>
                <div>
                    <v-dialog v-model="aboutDialog" max-width="600px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                v-show="!user.about"
                                v-bind="attrs"
                                v-on="on"
                                depressed
                                text
                                color="grey darken-1"
                            >
                            What should the world know about you?
                            </v-btn>
                        </template>
                        
                        <v-card>
                            <v-card-title>
                                <v-row align="center" class="spacer" no-gutters>
                                    <v-col cols="4" sm="2" md="1">
                                        <v-avatar color="grey darken-2" size="48" rounded="circle">
                                            <v-img v-if="avatar" :src="avatar"></v-img>
                                            <span v-else class="white--text text-h2">{{ avatarText }}</span>
                                        </v-avatar>
                                    </v-col>

                                    <v-col class="px-3">
                                        <strong>{{ fullName }}</strong>
                                    </v-col>
                                </v-row>
                            </v-card-title>
                            <v-card-text>
                                <v-divider></v-divider>
                                <v-container>
                                    <v-textarea
                                        hide-details
                                        rows="6"
                                        solo
                                        v-model="editor.about"
                                        >
                                        What should the world know about you?
                                    </v-textarea>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    color="purple lighten-1"
                                    text
                                    @click="aboutDialog = false"
                                    >
                                    Close
                                </v-btn>
                                <v-btn
                                    color="purple"
                                    :loading="aboutSubmitLoading"
                                    text
                                    @click="submitAbout"
                                    >
                                    Go!
                                </v-btn>
                            </v-card-actions>
                        </v-card>    
                    </v-dialog>
                </div>
                <edit-button
                    v-if="editEnabled"
                        @on-click="aboutDialog = true"
                ></edit-button>
            </v-container>
        </v-sheet>

        <v-sheet rounded="lg" class="mt-5">
            <v-container class="px-4">
                Work Gallery
            </v-container>
            <div v-if="userLoading">
                <v-skeleton-loader
                    class="mx-auto"
                    max-width1="300"
                    type="list-item-avatar, divider, card-heading, image, actions"
                    v-for="n in 2"
                    :key="n"
                ></v-skeleton-loader>
            </div>
            <v-row v-else class="pa-15">
                <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="4">
                    <v-img
                        :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                        :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                        aspect-ratio="2"
                        class="grey lighten-2"
                    >
                        <template v-slot:placeholder>
                            <v-row class="fill-height ma-0" align="center" justify="center">
                                <v-progress-circular
                                    indeterminate
                                    color="grey lighten-5"
                                ></v-progress-circular>
                            </v-row>
                        </template>
                    </v-img>
                </v-col>
            </v-row>
        </v-sheet>
    </div>
</template>

<script>
import EditButton from "../components/EditButton.vue"
import Avatar from "../components/Avatar.vue"
import Badge from "../components/Badge.vue"

export default {
    components: {EditButton, Avatar, Badge},

    props: {
        currentUser: null
    },

    data: () => ({
       editEnabled: false,
       userLoading: false,
       editor: { about: "" }, 
       aboutDialog: false,
       aboutSubmitLoading: false,
       user:null
    }),
    computed: {

        avatarText() {
            if (!this.user.firstname || !this.user.lastname) {
                return "You";
            }
            return ("" + this.user.firstname[0]).toUpperCase();
        },
        
        avatar() {
            return this.user.avatar;
        },

        fullName() {
            return this.user.firstname + " " + this.user.lastname;
        },

        values() {
            if (!this.user.values) 
                return;
            var values = [];
            this.user.values.forEach((e) => {
                values.push(e.name);
            });
            return values.join(" . ");
        }

    },
    created () {
        this.user=this.currentUser
    }

}
</script>

<style>

</style>
