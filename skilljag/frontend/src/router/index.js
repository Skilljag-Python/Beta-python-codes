/* import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () => import('../views/FeedView.vue'),
      children: [
        {
          path: '/recent',
          component: () => import('../components/RecentView.vue'),
          name: 'RecentView'
        },
        {
          path: '/trending',
          component: () => import('../components/TrendingView.vue'),
          name: 'TrendingView'
        }
      ]
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/form',
      name: 'ProfileForm',
      component: () => import('../components/ProfileForm.vue')
    },
    {
      path: '*',
      name: 'ErrorView',
      component: () => import('../views/ErrorView.vue')
    }
  ]
})
 */
import VueRouter from 'vue-router'
import Vue from 'vue'
import store from '../store'


Vue.component('home-screen', require('../views/HomeScreen.vue').default);
Vue.component('post', require('../views/Partials/DefaultPost.vue').default);
Vue.component('nt-post', require('../views/Partials/NewTPost.vue').default);
Vue.component('dark-switch-item', require('../views/Partials/DarkSwitchItem.vue').default);
Vue.component('search-dialog', require('../views/Partials/SearchDialog.vue').default);
Vue.component('conversations-icon', require('../views/Partials/ConversationsIcon.vue').default);
Vue.component('avatar-menu', require('../views/Partials/AvatarMenu.vue').default);
Vue.component('avatar', require('../views/Partials/Avatar.vue').default);
Vue.component('ad', require('../views/Partials/Ad.vue').default);
Vue.component('badge', require('../views/Partials/Badge.vue').default);
Vue.component('edit-button', require('../views/Partials/EditButton.vue').default);


import Online from '../views/Screens/OnlineTab.vue'
import Recommended from '../views/Screens/RecommendedTab.vue'
import You from '../views/Screens/YouTab.vue'
import Newtechs from '../views/Screens/NewTechsTab.vue'
import MyProfile from '../views/Screens/MyProfile.vue'
import Profile from '../views/Screens/Profile.vue'
import Search from '../views/Screens/SearchResults.vue'
import Conversations from '../views/Screens/Conversations.vue'
import Conversations1 from '../views/Screens/Conversations1.vue'
import AdditionalInfo from '../views/Screens/Additionalinfo.vue'


const routes = [
  {
    path: '/online',
    component: Online
  },
  {
    path: '/recommended',
    component: Recommended
  },
  {
    path: '/you',
    component: You
  },
  {
    path: '/newtechs',
    component: Newtechs
  },
  {
    path: '/profile',
    component: MyProfile
  },
  {
    path: '/user/:username',
    component: Profile
  },
  {
    path: '/search',
    component: Search
  },
  {
    path: '/conversations',
    component: Conversations
  },
  {
    path: '/conversations1',
    component: Conversations1
  }
]

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'hash',
  routes,
  scrollBehavior() {
    return {
      x: 0,
      y: 0
    }
  }
})